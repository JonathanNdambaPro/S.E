import typing as t
from dataclasses import dataclass, field

import pytest


@dataclass
class PathFaker:
    suffix: str = "csv"
    state: bool = True

    def is_file(self):
        return self.state


def generate_fake_columns():
    return ["column_1", "column_2", "column_3"]


@dataclass
class DataFrameFaker:
    columns: t.List = field(default_factory=generate_fake_columns)


@pytest.fixture()
def path_faker():
    path_faker = PathFaker()
    return path_faker


@pytest.fixture()
def path_faker_false():
    path_faker = PathFaker(state=False)
    return path_faker


@pytest.fixture()
def dataframe_faker():
    dataframe_faker = DataFrameFaker()
    return dataframe_faker
