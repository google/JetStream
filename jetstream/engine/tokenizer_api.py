# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Defines the JetStream Tokenizer API."""

import abc
from typing import Tuple, Union

import numpy as np
import jax

from jetstream.engine import engine_api


class Tokenizer(abc.ABC):
  """Tokenizer to convert strings to token ids and vice-versa."""

  @abc.abstractmethod
  def encode(
      self, s: str, **kwargs
  ) -> Tuple[Union[jax.Array, np.ndarray], int]:
    """Tokenize a string.

    Args:
        s: String to tokenize.
        **kwargs: Additional keyword arguments

    Returns:
        tokens: Tokenized into integers.
        true_length: Actual length of the non-padded sequence
          if padding is used.
    """

  @abc.abstractmethod
  def decode(
      self,
      slot: int,
      slot_max_length: int,
      result_tokens: engine_api.ResultTokens,
      complete: np.ndarray,
      **kwargs,
  ) -> Tuple[list[list[int]], np.ndarray]:
    """Processes a result tokens into a list of token ids, handling multiple
    samples.

    Args:
      slot: The slot at which to draw tokens from.
      slot_max_length: Max length for a sample in the slot.
      result_tokens: The tokens to access by slot.
      complete: Array representing the completion status of each sample in the
        slot.
      **kwards: Additional keyword arguments.

    Returns:
      sample_return: List of strings, one per sample.
      complete: Updated complete.
    """
    # TODO(bbahl): Add an option to return str from decode.

  @property
  @abc.abstractmethod
  def pad_id(self) -> int:
    """ID of the pad token."""

  @property
  @abc.abstractmethod
  def eos_id(self) -> int:
    """ID of EOS token."""
