import os
import shortuuid
from prometheus_client import Gauge
from dataclasses import dataclass


# Properties to be set for each metric
@dataclass
class _MetricLabels:
  hostname: str = os.getenv("HOSTNAME", shortuuid.uuid())
  idx: int


def _create_labeled_metric(metric, labels: _MetricLabels):
  return metric.labels(
      hostname=labels.hostname, idx=labels.idx if labels.idx else None
  )


# Metric Definitions
# Wrapper class should be used to assure all metrics have proper tags
class JetstreamMetricsCollector:

  def __new__(cls):
    if not hasattr(cls, "instance"):
      cls.instance = super(JetstreamMetricsCollector, cls).__new__(cls)
    return cls.instance

  # Metric definitions
  __prefill_backlog = Gauge(
      name="jetstream_prefill_backlog_size",
      documentation="Size of prefill queue",
      labelnames=["hostname"],
  )
  __slots_available_percentage = Gauge(
      name="jetstream_slots_available_percentage",
      documentation="The percentage of available slots in decode batch",
      labelnames=["hostname", "idx"],
  )

  def get_prefill_backlog_metric(self):
    return _create_labeled_metric(self.__prefill_backlog, _MetricLabels())

  def get_slots_available_percentage_metric(self, idx: int):
    return _create_labeled_metric(
        self.__slots_available_percentage,
        _MetricLabels(idx=idx),
    )
