# AccuKnox Django Trainee Assignment

## Project Overview

This project contains solutions for the AccuKnox Django Trainee technical assignment.

It demonstrates Django model signals and a custom iterable Python Rectangle class.

## Technologies Used

- Python
- Django
- SQLite
- VS Code / Antigravity

## Project Structure

```text
accuknox_assignment/
│
├── config/
├── signals_demo/
│   ├── migrations/
│   ├── models.py
│   ├── signals.py
│   └── apps.py
│
├── rectangle_demo/
│   ├── rectangle.py
│   └── test_rectangle.py
│
├── manage.py
└── README.md
```

## Task 1: Django Signals

### Question 1: Are Django signals synchronous or asynchronous by default?

**Answer:** Django signals are synchronous by default.

The signal receiver executes before the model save operation returns. A time delay inside the receiver demonstrates this behaviour.

### Question 2: Do Django signals execute in the same thread as the caller?

**Answer:** Yes. By default, synchronous signal receivers execute in the same thread as the caller.

This was verified by comparing the caller thread ID and receiver thread ID.

### Question 3: Do Django signals execute in the same database transaction as the caller?

**Answer:** When a model save operation is performed inside `transaction.atomic()`, the synchronous signal receiver executes within the same active transaction.

This was verified using:

```python
transaction.get_connection().in_atomic_block
```

Both the caller and signal receiver returned `True` inside the atomic block. A rollback test also confirmed that the created record was not saved.

## Task 2: Custom Rectangle Class

### Implementation

```python
class Rectangle:

    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {"length": self.length}
        yield {"width": self.width}
```

### Test

```python
rectangle = Rectangle(10, 5)

for item in rectangle:
    print(item)
```

### Expected Output

```text
{'length': 10}
{'width': 5}
```

## How to Run the Project

1. Activate the virtual environment.
2. Install Django if required:

```bash
pip install django
```

3. Run migrations:

```bash
python manage.py migrate
```

4. Start the Django server:

```bash
python manage.py runserver
```

5. Test the Rectangle class using Django shell:

```bash
python manage.py shell
```

```python
exec(open("rectangle_demo/test_rectangle.py").read())
```

## Conclusion

Both assignment tasks have been implemented and tested successfully.