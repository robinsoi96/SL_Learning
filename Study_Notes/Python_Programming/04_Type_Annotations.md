# Type Annotations in Python

Type annotations in Python are primarily **for static analysis and documentation**, they are **ignored by the Python interpreter at runtime** and **do not enforce type checking during program execution**.

- Type annotations provide valuable metadata that can be used by static analysis tool (like `MyPy`), IDEs and other libraries to **improve code readability**, **facilitate error detection during development** and **enhance code completion**

## Variable Annotation

Syntax:

```python
variable_name: data_type = initial_value
```

## Function Parameter Annotation

Syntax:

```python
def function_name(parameter_name: data_type) -> return_type:
    # function body
```

- `-> return_type` syntax is known as `return type annotation`, written after the function parameters **specifies the expected type of value returned by the function**