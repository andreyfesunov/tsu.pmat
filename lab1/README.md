# Лабораторная работа 1, способы запуска:

## Программа 1 - ./divider.py
1. В первую очередь, убедитесь, что файл исполняемый, для этого:
```bash
cd ./lab1
```
2. Сделайте файл исполняемым:
```bash
chmod +x ./divider.py
```
3. Запустите скрипт:
```bash
./divider.py
```
4. Введите число.
5. Кроме того, есть возможность передать число через pipeline (повторяем всё до 2 шага включительно). Запустите скрипт и передайте в него данные (например, через echo):
```bash
echo 2 | ./divider.py
```

## Программа 2 - ./randomizer.py
1. По аналогии с программой 1, убедитесь, что файл исполняемый. Запустите скрипт:
```bash
./randomizer.py
```

## Программа 3 - ./sqrt.py
1. По аналогии с программой 1, убедитесь, что файл исполняемый. Запустите скрипт:
```bash
./sqrt.py
```
(Я думал о том, чтобы сделать возможность работать через перенаправление, но работать стал чётко по заданию.)

## Тесты
1. Убедитесь в том, что на компьютере установлен pytest (если же нет, установите через пакетный менеджер):
2. В корне репозитория запустите:
```bash
pytest .
```