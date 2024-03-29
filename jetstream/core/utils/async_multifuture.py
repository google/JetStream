import asyncio
from concurrent import futures
import threading
from typing import Any, Generic, TypeVar

ValueType = TypeVar('ValueType')


class _Exception:
  """A class for propagating exceptions through a queue.

  By wrapping them with a custom private class we ensure that any type
  (including Exception) can be used as a ValueType.
  """

  def __init__(self, exception: Exception) -> None:
    self.exception = exception


class AsyncMultifuture(Generic[ValueType]):
  """AsyncMultifuture is like concurrent.futures.Future but supports returning

  multiple results. It provides an unidirectional stream with buffering and
  exception propagation.

  Supports delivering results to an async Python event loop. Must be
  constructed
  inside of the event loop.
  """

  def __init__(self) -> None:
    self._cancelled = threading.Event()
    self._done = threading.Event()
    self._loop = asyncio.get_running_loop()
    self._queue = asyncio.Queue[ValueType | _Exception]()

  def cancel(self, unused: Any = None) -> None:
    """Cancels the asyncmultifuture."""
    # Needed for compatibility with grpc.aio.ServicerContext.add_done_callback.
    del unused
    self._cancelled.set()
    self.set_exception(futures.CancelledError())

  def cancelled(self) -> bool:
    """Returns whether the asyncmultifuture has been cancelled."""
    return self._cancelled.is_set()

  def done(self) -> bool:
    """AsyncMultifuture is done when it is finalized with close() or set_exception()."""
    return self._done.is_set()

  def set_exception(self, exception: Exception) -> None:
    """Stores the given exception in the asyncmultifuture.

    The exception would be delivered after all previously added results are
    yielded. set_exception can be called multiple times, however subsequent
    calls will be ignored.

    Args:
      exception: The exception to set.
    """
    self._loop.call_soon_threadsafe(
        self._queue.put_nowait, _Exception(exception)
    )
    self._loop.call_soon_threadsafe(self._done.set)

  def add_result(self, result: ValueType) -> None:
    """Adds the result to the asyncmultifuture.

    Caller must call .close() once all results are added.

    Args:
      result: The result to add.
    """
    self._loop.call_soon_threadsafe(self._queue.put_nowait, result)

  def close(self) -> None:
    """Notifies the receiver that no more results would be added."""
    self.set_exception(StopAsyncIteration())

  def __aiter__(self) -> 'AsyncMultifuture':
    return self

  async def __anext__(self) -> ValueType:
    """Returns the next value."""
    value = await self._queue.get()
    if isinstance(value, _Exception):
      raise value.exception
    return value
