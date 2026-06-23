## Functions & Closures

A function is a reusable block of code that executes a specific task

a closure is a specialized inner function that retains access to variables from its enclosing outer scope even after outer function has finished executing

Python treats functions as first-class citizens, meaning they can be passed around as arguments, assigned to variables, and returned from other functions.

What is a Closure?

a closure is formed only when three specific conditions are met:

- There is a nested function (a function defined inside another function).

- The inner function references a variable from the enclosing (outer) scope.

- The outer function returns the inner function object itself.

## The Four Scopes of LEGB

1.  Local (L): Variables defined inside the current function or a lambda expression. These are created when the function is called and destroyed when it exits

2.  Enclosing (E): Variables inside any outer (enclosing) functions. This scope is relevant when dealing with nested functions and closures.

3.  Variables defined at the topmost level of a Python file, module, or script. They are accessible anywhere within that specific module

4.  Names pre-loaded into Python’s built-in module. This includes standard keywords, functions, and exceptions like print(), len(), int, or ValueError

## Function Factories

A function that creates and returns another function

```python
def power_factory(exponent):
    # Enclosing Scope: 'exponent' is frozen here
    def power(base):
        # Local Scope: accesses 'base' from arguments and 'exponent' from E scope
        return base ** exponent
    return power  # Returns the customized function object

# Generate specialized functions
square = power_factory(2)
cube = power_factory(3)

print(square(4))  # Output: 16 (4 ** 2)
print(cube(4))    # Output: 64 (4 ** 3)

```

## Examples

API URL Configurator

```python
def api_endpoint_factory(base_url):
    def build_url(route):
        return f"{base_url.rstrip('/')}/{route.lstrip('/')}"
    return build_url

production_api = api_endpoint_factory("https://company.com")
staging_api = api_endpoint_factory("https://company.com")

print(production_api("/users"))  # Output: https://company.com/users
print(staging_api("/users"))     # Output: https://company.com/users
```
