# ag.funutils
Fun functional utilities for python. This library provides a `chain` method and several operators that you can chain together to create pipelines of functional transformations, like with Lodash's chain or Clojure's threading macros.

The provided functions are "sugary". They do NOT provide performance optimizations, error handling, or guarantees of statelessness.

Each operator will take a transformation and return a function that applies that transformation to an iterable. Because most operators are wrappers around built-in functions like of the same name, they return iterables and the results of most chains will need to be converted to a list to be immediately useful. The documentation for associated standard library functions should largely be applicable to the provided operators.

## Examples
Also see the tests.

```python
from ag.funutils import fun

add_one = fun.map(lambda x: x + "1")
upper = fun.map(str.upper)
    
fun.chain(
    ["a", "b", "c", "d"],
    add_one,
    upper,
    list
) # => ["A1", "B1", "C1", "D1"]

big_transform = [add_one, upper]

fun.chain(
    ["a", "b", "c", "d"],
    *big_transform,
    list
) # => ["A1", "B1", "C1", "D1"])

fun.chain(
    ["a", "b", "c", "d"],
    fun.tap(print), # => "[a, b, c, d]"
    *big_transform,
    fun.tap(print), # => "[A1, B1, C1, D1]"
    fun.sort(reverse=True),
    list
) # => ["D1", "C1", "B1", "A1"]

fun.chain(
    ["a", "b", "c", "d"],
    *big_transform,
    fun.reduce(lambda acc, x: acc + x)
) # => "A1B1C1D1"

# Values that are tuples will be spread into the transformations,
# which lets you work with dicts.

data = {
    'beep': 1,
    'boop': 2,
    'buup': 3,
}

add_one = fun.map(lambda k, v: (k, v + 1))
evens = fun.filter(lambda k, v: v % 2 == 0)
beep_buup = fun.reduce(lambda acc, k, v: f'{acc}{k}{v}', '')

result = fun.chain(
    data.items(),
    add_one,
    evens,
    add_one,
    beep_buup
) # => 'beep3buup5'
```

# Reference
- `ag.funutils.chain(data, *transforms)`:
  - Provides `data` as an argument to the first `transform`, then the result of each `transform` to the following one. Each `transform` should be a function that takes a single, iterable argument and returns an iterable. The exception is the `reduce` operator, which can return a single value if it is the last operator in the chain.
- `ag.funutils.map(transform)`:
  - returns a function which takes an iterable and applies `transform` to each item of the iterable
- `ag.funutils.filter(condition)`:
  - returns a function which takes an iterable and returns an iterable with only items matching the condition
- `ag.funutils.sort(key=None, reverse=False)`:
  - returns a function which takes an iterable and return an iterable sorted according to the value returned by the `key` function. Compares items directly by default.
- `ag.funutils.reduce(transform, initial=None)`:
  - returns a function which takes an iterable and reduces it to a single value. If no `initial` value is provided, the first item is used as the initial value.
- `ag.funutils.tap(fn)`:
  - returns a function which takes a single argument, passes it to `fn`, and returns it. Intended for debugging purposes, in particular: `ag.funutils.tap(print)`.

# Development

Requires pipenv and python 3.7.

```bash
$ ./scripts/setup.sh
$ ./scripts/test.sh
```

