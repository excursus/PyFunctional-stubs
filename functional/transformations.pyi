from collections import namedtuple
from functional.execution import ExecutionStrategies as ExecutionStrategies
from typing import Any, Optional

Transformation = namedtuple('Transformation', ['name', 'function', 'execution_strategies'])
CACHE_T: Any

def name(function: Any): ...
def map_t(func: Any): ...
def select_t(func: Any): ...
def starmap_t(func: Any): ...
def filter_t(func: Any): ...
def where_t(func: Any): ...
def filter_not_t(func: Any): ...
def reversed_t(): ...
def slice_t(start: Any, until: Any): ...
def distinct_t(): ...
def distinct_by_t(func: Any): ...
def sorted_t(key: Optional[Any] = ..., reverse: bool = ...): ...
def order_by_t(func: Any): ...
def drop_right_t(n: Any): ...
def drop_t(n: Any): ...
def drop_while_t(func: Any): ...
def take_t(n: Any): ...
def take_while_t(func: Any): ...
def flat_map_impl(func: Any, sequence: Any) -> None: ...
def flat_map_t(func: Any): ...
def flatten_t(): ...
def zip_t(zip_sequence: Any): ...
def zip_with_index_t(start: Any): ...
def enumerate_t(start: Any): ...
def cartesian_t(iterables: Any, repeat: Any): ...
def init_t(): ...
def tail_t(): ...
def inits_t(wrap: Any): ...
def tails_t(wrap: Any): ...
def union_t(other: Any): ...
def intersection_t(other: Any): ...
def difference_t(other: Any): ...
def symmetric_difference_t(other: Any): ...
def group_by_key_impl(sequence: Any): ...
def group_by_key_t(): ...
def reduce_by_key_impl(func: Any, sequence: Any): ...
def reduce_by_key_t(func: Any): ...
def accumulate_impl(func: Any, sequence: Any): ...
def accumulate_t(func: Any): ...
def count_by_key_impl(sequence: Any): ...
def count_by_key_t(): ...
def count_by_value_impl(sequence: Any): ...
def count_by_value_t(): ...
def group_by_impl(func: Any, sequence: Any): ...
def group_by_t(func: Any): ...
def grouped_impl(wrap: Any, size: Any, sequence: Any) -> None: ...
def grouped_t(wrap: Any, size: Any): ...
def sliding_impl(wrap: Any, size: Any, step: Any, sequence: Any) -> None: ...
def sliding_t(wrap: Any, size: Any, step: Any): ...
def partition_impl(wrap: Any, predicate: Any, sequence: Any): ...
def partition_t(wrap: Any, func: Any): ...
def inner_join_impl(other: Any, sequence: Any): ...
def join_impl(other: Any, join_type: Any, sequence: Any): ...
def join_t(other: Any, join_type: Any): ...