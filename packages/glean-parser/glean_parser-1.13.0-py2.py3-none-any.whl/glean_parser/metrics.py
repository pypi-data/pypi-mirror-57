# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
Classes for each of the high-level metric types.
"""

import dataclasses
from dataclasses import dataclass, field, InitVar
import enum
from typing import Dict, List, Set, Union

from . import parser
from . import util


class Lifetime(enum.Enum):
    ping = 0
    user = 1
    application = 2


@dataclass
class Metric:
    glean_internal_metric_cat = "glean.internal.metrics"
    metric_types = {}
    default_store_names = ["metrics"]

    def __init_subclass__(cls, **kwargs):
        # Create a mapping of all of the subclasses of this class
        if cls not in Metric.metric_types and hasattr(cls, "typename"):
            Metric.metric_types[cls.typename] = cls
        super().__init_subclass__(**kwargs)

    @classmethod
    def make_metric(cls, category, name, metric_info, config={}, validated=False):
        """
        Given a metric_info dictionary from metrics.yaml, return a metric
        instance.

        :param: category The category the metric lives in
        :param: name The name of the metric
        :param: metric_info A dictionary of the remaining metric parameters
        :param: config A dictionary containing commandline configuration
            parameters
        :param: validated True if the metric has already gone through
            jsonschema validation
        :return: A new Metric instance.
        """
        metric_type = metric_info["type"]
        return cls.metric_types[metric_type](
            category=category,
            name=name,
            _validated=validated,
            _config=config,
            **metric_info
        )

    def serialize(self):
        """
        Serialize the metric back to JSON object model.
        """
        d = dataclasses.asdict(self)
        # Convert enum fields back to strings
        for key, val in d.items():
            if isinstance(val, enum.Enum):
                d[key] = d[key].name
            if isinstance(val, set):
                d[key] = sorted(list(val))
        del d["name"]
        del d["category"]
        return d

    def identifier(self):
        """
        Create an identifier unique for this metric.
        Generally, category.name; however, Glean internal
        metrics only use name.
        """
        if not self.category:
            return self.name
        return ".".join((self.category, self.name))

    def __post_init__(self, _config, _validated):
        # Convert enum fields to Python enums
        for f in dataclasses.fields(self):
            if isinstance(f.type, type) and issubclass(f.type, enum.Enum):
                setattr(self, f.name, getattr(f.type, getattr(self, f.name)))
            if f.type == Set[str]:
                value = getattr(self, f.name)
                if isinstance(value, list):
                    setattr(self, f.name, set(value))

        self.validate_expires(self.expires)
        if hasattr(self, "extra_keys"):
            self.validate_extra_keys(self.extra_keys, _config)

        # _validated indicates whether this metric has already been jsonschema
        # validated (but not any of the Python-level validation).
        if not _validated:
            data = {
                "$schema": parser.METRICS_ID,
                self.category: {self.name: self.serialize()},
            }
            for error in parser.validate(data):
                raise ValueError(error)

        # Metrics in the special category "glean.internal.metrics" need to have
        # an empty category string when identifying the metrics in the ping.
        if self.category == Metric.glean_internal_metric_cat:
            self.category = ""

    type: str

    # Metadata
    category: str
    name: str
    bugs: List[Union[int, str]]
    description: str
    notification_emails: List[str]
    expires: str
    data_reviews: List[str] = field(default_factory=list)
    version: int = 0
    disabled: bool = False

    # Ping-related properties
    lifetime: Lifetime = "ping"
    send_in_pings: List[str] = field(default_factory=lambda: ["default"])

    unit: str = ""

    # The following is a Gecko-specific property for using the Glean SDK
    # with GeckoView metrics. See bug 1566356 for more context.
    gecko_datapoint: str = ""

    # Lint checks to disable for this metric.
    no_lint: List[str] = field(default_factory=list)

    # Implementation detail -- these are parameters to the constructor that
    # aren't stored in the dataclass object.
    _config: InitVar[dict] = {}
    _validated: InitVar[bool] = False

    def is_disabled(self):
        return self.disabled or self.is_expired()

    def is_expired(self):
        return util.is_expired(self.expires)

    @staticmethod
    def validate_expires(expires):
        return util.validate_expires(expires)

    def is_internal_metric(self):
        return self.category in (Metric.glean_internal_metric_cat, "")


@dataclass
class Boolean(Metric):
    typename = "boolean"


@dataclass
class String(Metric):
    typename = "string"


@dataclass
class StringList(Metric):
    typename = "string_list"


@dataclass
class Counter(Metric):
    typename = "counter"


@dataclass
class Quantity(Metric):
    typename = "quantity"


class TimeUnit(enum.Enum):
    nanosecond = 0
    microsecond = 1
    millisecond = 2
    second = 3
    minute = 4
    hour = 5
    day = 6


@dataclass
class TimeBase(Metric):
    time_unit: TimeUnit = "millisecond"


@dataclass
class Timespan(TimeBase):
    typename = "timespan"


@dataclass
class TimingDistribution(TimeBase):
    typename = "timing_distribution"


class MemoryUnit(enum.Enum):
    byte = 0
    kilobyte = 1
    megabyte = 2
    gigabyte = 3


@dataclass
class MemoryDistribution(Metric):
    typename = "memory_distribution"

    memory_unit: MemoryUnit = "byte"


class HistogramType(enum.Enum):
    linear = 0
    exponential = 1


@dataclass
class CustomDistribution(Metric):
    typename = "custom_distribution"

    range_min: int = 1
    # The defaults must be provided here to work with Python's @dataclass,
    # however, in practice, these parameters are required by the schema,
    # so they will never be used.
    range_max: int = -1
    bucket_count: int = -1
    histogram_type: HistogramType = HistogramType.exponential


@dataclass
class Datetime(TimeBase):
    typename = "datetime"


@dataclass
class Event(Metric):
    typename = "event"
    default_store_names = ["events"]

    extra_keys: Dict[str, str] = field(default_factory=dict)

    @property
    def allowed_extra_keys(self):
        # Sort keys so that output is deterministic
        return sorted(list(self.extra_keys.keys()))

    @staticmethod
    def validate_extra_keys(extra_keys, config):
        if not config.get("allow_reserved") and any(
            k.startswith("glean.") for k in extra_keys.keys()
        ):
            raise ValueError(
                "Extra keys beginning with 'glean.' are reserved for "
                "Glean internal use."
            )


@dataclass
class Uuid(Metric):
    typename = "uuid"


@dataclass
class Labeled(Metric):
    labeled = True
    # Start the labels as a List to preserve the order from `metrics.yaml`
    labels: List[str] = None

    def __post_init__(self, *args):
        ordered_labels = self.labels

        # If any, turn the labels into a Set to properly inialize the Metric object.
        # This is important because Kotlin code needs this labels as a Set
        if self.labels is not None:
            self.labels = set(ordered_labels)
        super().__post_init__(*args)

        # After initializing the Metric object, add the ordered_labels to it.
        # If we do this step before calling the __post_init__ for the Metric class,
        # the metric schema validation will fail
        self.ordered_labels = ordered_labels


@dataclass
class LabeledBoolean(Labeled, Boolean):
    typename = "labeled_boolean"


@dataclass
class LabeledString(Labeled, String):
    typename = "labeled_string"


@dataclass
class LabeledCounter(Labeled, Counter):
    typename = "labeled_counter"
