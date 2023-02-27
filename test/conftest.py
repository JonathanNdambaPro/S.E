import typing as t
from dataclasses import dataclass, field


@dataclass
class PathFaker:
    suffix: str = "csv"

    def is_file(self):
        return True


def generate_fake_columns():
    return ["column_1", "column_2", "column_3"]


@dataclass
class DataFrameFaker:
    columns: t.List = field(default_factory=generate_fake_columns)
