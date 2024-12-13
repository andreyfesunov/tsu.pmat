import csv
import os
from abc import ABC
from enum import Enum
from typing import Any, Callable, Dict, List, Optional, Tuple, Union


class SingletonMeta(type):
    """Синглтон метакласс для Database."""

    _instances: Dict[type, "Database"] = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> "Database":
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class DatabaseAggregateMethod(str, Enum):
    AVG = "AVG"
    MAX = "MAX"
    MIN = "MIN"
    COUNT = "COUNT"


class Database(metaclass=SingletonMeta):
    """Класс-синглтон базы данных с таблицами, хранящимися в файлах."""

    def __init__(self) -> None:
        self.tables: Dict[str, "Table"] = {}

    def register_table(self, table_name: str, table: "Table") -> None:
        self.tables[table_name] = table

    def insert(self, table_name: str, data: str) -> None:
        table = self.tables.get(table_name)
        if table:
            table.insert(data)
        else:
            raise ValueError(f"Table {table_name} does not exist.")

    def select(self, table_name: str, **kwargs: Any) -> Optional[List[Dict[str, str]]]:
        table = self.tables.get(table_name)
        return table.select(**kwargs) if table else None

    # TODO refactor to token factory
    def join(
        self,
        table1_query: str | List[Dict[str, Union[str, int]]],
        table2_query: str | List[Dict[str, Union[str, int]]],
        compare_func: Callable[[Dict[str, Any], Dict[str, Any]], bool],
    ) -> List[Dict[str, Union[str, int]]]:
        table1 = (
            self.tables.get(table1_query).DATA
            if isinstance(table1_query, str)
            else table1_query
        )
        table2 = (
            self.tables.get(table2_query).DATA
            if isinstance(table2_query, str)
            else table2_query
        )
        prefix1 = f"{table1_query}." if isinstance(table1_query, str) else ""
        prefix2 = f"{table2_query}." if isinstance(table2_query, str) else ""

        if not table1 or not table2:
            raise ValueError("One or both tables do not exist.")

        results = []

        for entry1 in table1:
            for entry2 in table2:
                if compare_func(entry1, entry2):
                    merged_dict = {f"{prefix1}{k}": entry1[k] for k in entry1}
                    merged_dict.update({f"{prefix2}{k}": entry2[k] for k in entry2})

                    results.append(merged_dict)

        return results

    def aggregate(
        self,
        method: DatabaseAggregateMethod,
        table: str | List[Dict[str, Union[str, int]]],
        column: str,
    ) -> int | float:
        table = self.tables.get(table).DATA if isinstance(table, str) else table

        if not table:
            raise ValueError("Table not exists")

        values = [float(entry[column]) for entry in table]

        match method:
            case DatabaseAggregateMethod.AVG:
                return sum(values) / len(values)
            case DatabaseAggregateMethod.MAX:
                return max(values)
            case DatabaseAggregateMethod.MIN:
                return min(values)
            case DatabaseAggregateMethod.COUNT:
                return len(values)


class Table(ABC):
    """Абстрактный базовый класс для таблиц с вводом/выводом файлов CSV."""

    ATTRS: Tuple[str] = "id"
    UNIQUE_ATTRS: Tuple[str] = "id"
    NAME = None
    DATA: List[Dict[str, Union[str, int]]] = []

    def insert(self, data: str) -> None:
        entry = dict(zip(self.ATTRS, data.split()))
        if not self.check_uniqueness(entry):
            raise ValueError(
                f"Entry with unique attribute {self.UNIQUE_ATTRS} already exists."
            )
        self.DATA.append(entry)
        self.save()

    def select(self, **kwargs: Any) -> List[Dict[str, Union[str, int]]]:
        results = self.DATA
        for key, value in kwargs.items():
            if key in self.ATTRS:
                results = [entry for entry in results if entry[key] in value]
        return results

    def check_uniqueness(self, entry: Dict[str, Any]) -> bool:
        for data in self.DATA:
            if all(
                (attr in data and attr in entry and entry[attr] == data[attr])
                for attr in self.UNIQUE_ATTRS
            ):
                return False
        return True


class CSVTable(Table):
    FILE_PATH: str = None

    def __init__(self) -> None:
        self.load()

    def save(self) -> None:
        with open(self.FILE_PATH, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.ATTRS)
            writer.writeheader()
            writer.writerows(self.DATA)

    def load(self) -> None:
        if os.path.exists(self.FILE_PATH):
            with open(self.FILE_PATH, "r") as f:
                reader = csv.DictReader(f)
                self.DATA = [row for row in reader]
        else:
            self.DATA = []


class EmployeeTable(CSVTable):
    """Таблица сотрудников с методами ввода-вывода из файла CSV."""

    NAME = "employees"
    ATTRS: Tuple[str] = ("id", "name", "age", "salary", "department_id")
    UNIQUE_ATTRS: Tuple[str] = ("id", "department_id")
    FILE_PATH: str = "employee_table.csv"


class DepartmentTable(CSVTable):
    """Таблица подразделений с вводом-выводом в/из CSV файла."""

    NAME = "departments"
    ATTRS: Tuple[str, ...] = ("id", "department_name")
    FILE_PATH: str = "department_table.csv"


class PersonalPromosTable(CSVTable):
    """Таблица персональных скидок для сотрудников с вводом-выводом в/из CSV файла"""

    NAME = "promos"
    ATTRS: Tuple[str, ...] = ("id", "employee_id", "percent")
    FILE_PATH: str = "personal_promos_table.csv"
