import os
import tempfile

import pytest
from database.database import Database, DepartmentTable, EmployeeTable


@pytest.fixture
def temp_employee_file():
    """Создаем временный файл для таблицы рабочих"""
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    yield temp_file.name
    os.remove(temp_file.name)


@pytest.fixture
def temp_department_file():
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    yield temp_file.name
    os.remove(temp_file.name)


@pytest.fixture
def database(temp_employee_file, temp_department_file):
    """Данная фикстура задает БД и определяет таблицы."""
    db = Database()

    employee_table = EmployeeTable()
    employee_table.FILE_PATH = temp_employee_file
    department_table = DepartmentTable()
    department_table.FILE_PATH = temp_department_file

    db.register_table("employees", employee_table)
    db.register_table("departments", department_table)

    return db


def test_insert_employee(database):
    database.insert("employees", "1 Alice 30 70000")
    database.insert("employees", "2 Bob 28 60000")

    employee_data = database.select("employees", id=["1", "2"])
    assert len(employee_data) == 2
    assert employee_data[0] == {
        "id": "1",
        "name": "Alice",
        "age": "30",
        "salary": "70000",
    }
    assert employee_data[1] == {
        "id": "2",
        "name": "Bob",
        "age": "28",
        "salary": "60000",
    }


def test_insert_department(database):
    database.insert("employees", "1 Alice 30 70000")
    database.insert("employees", "2 Alice 30 70000")
    database.insert("employees", "1 Alice 30 70000 1")
    database.insert("employees", "1 Alice 30 70000 2")
    database.insert("employees", "2 Alice 30 70000 1")
    database.insert("employees", "2 Alice 30 70000 2")

    with pytest.raises(ValueError):
        database.insert("employees", "2 Alice 30 70000 2")


def test_select_employees(database):
    database.insert("employees", "1 Alice 30 70000")
    database.insert("employees", "2 Max 21 54000")
    database.insert("employees", "3 Alice 28 77000")

    employee_data = database.select("employees", name=["Alice"])
    assert len(employee_data) == 2
    assert any(entry["id"] == "1" for entry in employee_data)
    assert any(entry["id"] == "3" for entry in employee_data)

    employee_data = database.select("employees", age=["30"])
    assert len(employee_data) == 1
    assert any(entry["id"] == "1" for entry in employee_data)


def test_join_employees_departments(database):
    database.insert("departments", "2 IU")
    database.insert("employees", "1 Alice 30 70000 2")

    join_result = database.join(
        "employees", "departments", lambda x, y: x["department_id"] == y["id"]
    )
    assert len(join_result) == 1
    assert join_result[0]["employees.id"] == "1"
    assert join_result[0]["departments.id"] == "2"
