import typing as t
from dataclasses import dataclass, field

from package_2.sub_package import file_4


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


def test_file_4_read_file(mocker):
    faker_dataframe = DataFrameFaker()
    mocker.patch("package_2.sub_package.file_4.pd.read_csv", return_value=faker_dataframe)
    project_root_path = PathFaker()
    value = file_4.read_header_csv(project_root_path)

    assert value == ["column_1", "column_2", "column_3"]
