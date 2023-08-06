# Fortuna: A Collection of Random Value Generators for Python3
Fortuna's main goal is to provide a quick and easy way to build custom random-value generators for your data. Fortuna also offers a variety of high-performance dice functions and random number generators.

The core functionality of Fortuna is based on the Storm c++ library. While Storm has a high quality, hardware seeded random engine - it is not appropriate for cryptography of any kind. Fortuna is meant for games, data science, A.I. and experimental programming, not security.


### Quick Install `$ pip install Fortuna`


### Installation may require the following:
- Python 3.6 or later with dev tools (setuptools, pip, etc.)
- Cython: Bridge from C/C++ to Python.
- Modern C++17 Compiler and Standard Library.


### Sister Projects (included but documented separately):
- RNG: Python3 API for the C++ Random Library. https://pypi.org/project/RNG/
- Pyewacket: Drop-in replacement for the Python3 random module. https://pypi.org/project/Pyewacket/
- MonkeyScope: Framework for testing non-deterministic generators. https://pypi.org/project/MonkeyScope/


---

### Table of Contents:
- Numeric Limits
- Project Terminology
- Random Generators:
    - Value Generators
        - `RandomValue(Collection) -> Callable -> Value`
        - `TruffleShuffle(Collection) -> Callable -> Value`
        - `QuantumMonty(Collection) -> Callable -> Value`
        - `CumulativeWeightedChoice(Table) -> Callable -> Value`
        - `RelativeWeightedChoice(Table) -> Callable -> Value`
        - `FlexCat(Matrix) -> Callable -> Value`
    - Integer Generators
        - `random_below(Integer) -> Integer`
        - `random_int(Integer, Integer) -> Integer`
        - `random_range(Integer, Integer, Integer) -> Integer`
        - `d(Integer) -> Integer`
        - `dice(Integer, Integer) -> Integer`
        - `plus_or_minus(Integer) -> Integer`
        - `plus_or_minus_linear(Integer) -> Integer`
        - `plus_or_minus_gauss(Integer) -> Integer`
    - Index Generators: 
        - ZeroCool Specification: `f(N) -> [0, N)` or `f(-N) -> [-N, 0)`
        - `random_index(Integer) -> Integer`
        - `front_gauss(Integer) -> Integer`
        - `middle_gauss(Integer) -> Integer`
        - `back_gauss(Integer) -> Integer`
        - `quantum_gauss(Integer) -> Integer`
        - `front_poisson(Integer) -> Integer`
        - `middle_poisson(Integer) -> Integer`
        - `back_poisson(Integer) -> Integer`
        - `quantum_poisson(Integer) -> Integer`
        - `front_linear(Integer) -> Integer`
        - `middle_linear(Integer) -> Integer`
        - `back_linear(Integer) -> Integer`
        - `quantum_linear(Integer) -> Integer`
        - `quantum_monty(Integer) -> Integer`
    - Float Generators
        - `canonical() -> Float`
        - `random_float(Float, Float) -> Float`
        - `triangular(Float, Float, Float) -> Float`
    - Boolean Generator
        - `percent_true(Float) -> Boolean`
    - Inplace Shuffle (Knuth B)
        - `shuffle(List) -> None`
    - Utilities
        - `flatten(Object, *args, Boolean, **kwargs) -> Object`
        - `smart_clamp(Integer, Integer, Integer) -> Integer`
- Development Log
- Test Suite Output
- Legal Information


#### Numeric Limits:
- Integer: 64 bit signed integer.
    - Range: ±9223372036854775807, approximately ±9.2 billion billion
- Float: 64 bit floating point.
    - Range: ±1.7976931348623157e+308
    - Epsilon Delta: 5e-324


#### Project Terminology:
- Value: Almost any object in Python can be considered a Value.
    - Expressions, Generators, and F-strings can be wrapped in a lambda for dynamic evaluation.
- Callable: Any callable object, function, method or lambda.
- Collection: A group of Values.
    - List, Tuple, Set, etc... Any object that can be converted into a list via `list(some_object)`.
    - Comprehensions that produce a Collection also qualify.
    - Fortuna classes that wrap a Collection can wrap a Collection, Sequence or Generator.
    - Fortuna functions that take a Collection as input will always require a Sequence.
- Sequence: An ordered Collection.
    - List, tuple or list comprehension.
    - A Sequence is an ordered Collection that can be indexed like a list, without conversion.
    - All Sequences are Collections but not all Collections are Sequences. When in doubt, use a list.
- Pair: Sequence of two Values.
- Table: Sequence of Pairs.
- Matrix: Dictionary of Collections.
- Inclusive Range.
    - `[1, 10] -> 1, 2, 3, 4, 5, 6, 7, 8, 9, 10`
- Partially Exclusive Ranges.
    - `[1, 11) -> 1, 2, 3, 4, 5, 6, 7, 8, 9, 10`
    - `(0, 10] -> 1, 2, 3, 4, 5, 6, 7, 8, 9, 10`
- Automatic Flattening.
    - Works with: RandomValue, TruffleShuffle, QuantumMonty, WeightedChoice & FlexCat.
    - Lazy Evaluation. All Random Value Generator Classes in Fortuna will recursively call or "flatten" callable objects returned from the data at call time, so long as all required parameters are provided.
    - Mixing callable objects with un-callable objects is fully supported, but can become messy.
    - Nested callable objects are fully supported. Because `lambda(lambda) -> lambda` fixes everything for arbitrary values of 'because', 'fixes' and 'everything'.
    - To disable flattening, pass the optional keyword argument `flat=False` to the constructor.
    
----

## Random Value Generators

### Fortuna.RandomValue
`Fortuna.RandomValue(collection: Collection, flat=True) -> Callable -> Value`
- @param collection :: Collection of Values. Tuple recommended.
- @param flat :: Bool. Default: True. Option to automatically flatten callable values with lazy evaluation.
- @return :: Callable Object. `Callable(*args, zero_cool=random_index, range_to=0, **kwargs) -> Value`
    - @param zero_cool :: Optional ZeroCool Method, kwarg only. Default = random_index().
    - @param range_to :: Optional Integer in range [-N, N] where N is the magnitude of the range in the Collection. 
        - Default = 0, kwarg only. Parameter for ZeroCool Method. `range_to=0` indicates the intent to use the whole collection.
        - Negative values of range_to indicate ranging from the back of the Collection. 
    - @param *args, **kwargs :: Optional arguments used to flatten the return Value (below) if Callable.
    - @return Value or Value(*args, **kwargs) if Callable.

```python
from Fortuna import RandomValue, front_linear, back_linear

# Data Setup
random_apple = RandomValue((
    "Delicious", 
    "Empire", 
    "Granny Smith", 
    "Honey Crisp", 
    "Macintosh",
))
random_fruit = RandomValue((
    lambda: f"Apple, {random_apple()}",
    "Banana",
    "Cherry",
    "Grapes",
    "Orange",
))

# Usage
print(random_fruit())
# prints a random fruit with the default flat uniform distribution

print(random_fruit(zero_cool=back_linear))
# prints a random fruit with a back_linear distribution (ascending probability)

print(random_fruit(zero_cool=front_linear))
# prints a random fruit with a front_linear distribution (descending probability)

print(random_fruit(range_to=3))
# prints a random fruit of the first 3

print(random_fruit(zero_cool=front_linear, range_to=-3))
# prints a random fruit of the last 3 with a front_linear distribution.
```


#### RandomValue with Auto Flattening Callable Objects
```python
from Fortuna import RandomValue


auto_flat = RandomValue([lambda: 1, lambda: 2, lambda: 3])
print(auto_flat())  # will print the value 1, 2 or 3.
# Note: the lambda will not be called until call time and stays dynamic for the life of the object.

auto_flat_with = RandomValue([lambda x: x, lambda x: x + 1, lambda x:  x + 2])
print(auto_flat_with(2))  # will print the value 2, 3 or 4
# Note: if this is called with no args it will simply return the lambda in an uncalled state.

un_flat = RandomValue([lambda: 1, lambda: 2, lambda: 3], flat=False)
print(un_flat()())  # will print the value 1, 2 or 3, 
# mind the double-double parenthesis, they are required to manually unpack the lambdas

auto_un_flat = RandomValue([lambda x: x, lambda x: x + 1, lambda x:  x + 2], flat=False)
# Note: flat=False is not required here because the lambdas can not be called without input x satisfied.
# It is recommended to specify flat=False if non-flat output is intended.
print(auto_un_flat()(1))  # will print the value 1, 2 or 3, mind the double-double parenthesis
```

#### Mixing Static Objects with Callable Objects
```python
from Fortuna import RandomValue


""" With automatic flattening active, `lambda() -> int` can be treated as an `int`. """
mixed_flat = RandomValue([1, 2, lambda: 3])
print(mixed_flat())  # will print 1, 2 or 3

""" Anti-pattern """
mixed_un_flat = RandomValue([1, 2, lambda: 3], flat=False) # this pattern is not recommended.
print(mixed_flat())  # will print 1, 2 or "Function <lambda at some_address>"
# This pattern is not recommended because you wont know the nature of what you get back.
# This is almost always not what you want, and it can give rise to messy logic in other areas of your code.
```

#### Dynamic Strings
To successfully express a dynamic string, and keep it dynamic for the duration of the program, at least one level of indirection is required. Without a lambda - the f-string would collapse into a static string too soon.

```python
from Fortuna import RandomValue, d


# d() is a simple dice function, d(n) -> [1, n] flat uniform distribution.
dynamic_string = RandomValue((
    # while the probability of all A == all B == all C, individual probabilities of each possible string will differ based on the number of possible outputs of each category.
    lambda: f"A{d(2)}",  # -> A1 - A2, each are twice as likely as any particular B, and three times as likely as any C.
    lambda: f"B{d(4)}",  # -> B1 - B4, each are half as likely as any particular A, and 3/2 as likely as any C.
    lambda: f"C{d(6)}",  # -> C1 - C6, each are 1/3 as likely as any particular A and 2/3 as likely of any B.
))

print(dynamic_string())  # prints a random dynamic string, generated at call time.
```

#### Nesting Dolls
```python
from Fortuna import RandomValue

# Data Setup
nesting_dolls = RandomValue((
    RandomValue(("A", "B", "C", "D", "E")),
    RandomValue(("F", "G", "H", "I", "J")),
    RandomValue(("K", "L", "M", "N", "O")),
    RandomValue(("P", "Q", "R", "S", "T")),
))

# Usage
print(nesting_dolls())  
# prints one of the letters A-T, flat uniform distribution of each category and within each category.
```


### TruffleShuffle
`Fortuna.TruffleShuffle(collection: Collection, flat=True) -> Callable -> Value`
- @param collection :: Collection of Values. Set recommended but not required.
- @param flat :: Bool. Default: True. Option to automatically flatten callable values with lazy evaluation.
- @return :: Callable Object. `Callable(*args, **kwargs) -> Value`
    - @param *args, **kwargs :: Optional arguments used to flatten the return Value (below) if Callable.
    - @return :: Random value from the collection with a Wide Uniform Distribution. 
    
Wide Uniform Distribution: "Wide" refers to the average distance between consecutive occurrences of the same value. The average width of the output distribution will naturally scale up with the size of the collection. The goal of this type of distribution is to keep the output sequence free of clumps or streaks of the same value, while maintaining randomness and uniform probability. This is not the same as a flat uniform distribution. The two distributions over time will be statistically similar for any given set, but the repetitiveness of the output sequence will be very different.

#### TruffleShuffle, Basic Use
```python
from Fortuna import TruffleShuffle

# Data Setup
list_of_values = { 1, 2, 3, 4, 5, 6 }
truffle_shuffle = TruffleShuffle(list_of_values)

# Usage
print(truffle_shuffle())  # this will print one of the numbers 1-6, 
# repeated calls will produce a wide distribution.
```


### QuantumMonty
`Fortuna.QuantumMonty(collection: Collection, flat=True) -> Callable -> Value`
- @param collection :: Collection of Values. Tuple recommended.
- @param flat :: Bool. Default: True. Option to automatically flatten callable values with lazy evaluation.
- @return :: Callable Object with Monty Methods for producing various distributions of the data.
    - @param *args, **kwargs :: Optional arguments used to flatten the return Value (below) if Callable.
    - @return :: Random value from the data. The instance will produce random values from the list using the selected distribution model or "monty". The default monty is the Quantum Monty Algorithm.

```python
from Fortuna import QuantumMonty

# Data Setup
list_of_values = [1, 2, 3, 4, 5, 6]
monty = QuantumMonty(list_of_values)

# Usage
print(monty())               # prints a random value from the list_of_values.
                             # uses the default Quantum Monty Algorithm.

print(monty.flat_uniform())  # prints a random value from the list_of_values.
                             # uses the "flat_uniform" monty.
                             # equivalent to random.choice(list_of_values).
```
The QuantumMonty class represents a diverse collection of strategies for producing random values from a sequence where the output distribution is based on the method you choose. Generally speaking, each value in the sequence will have a probability that is based on its position in the sequence. For example: the "front" monty produces random values where the beginning of the sequence is geometrically more common than the back. Given enough samples the "front" monty will always converge to a 45 degree slope down for any list of unique values.

There are three primary method families: linear, gaussian, and poisson. Each family has three base methods; 'front', 'middle', 'back', plus a 'quantum' method that incorporates all three base methods. The quantum algorithms for each family produce distributions by overlapping the probability waves of the other methods in their family. The Quantum Monty Algorithm incorporates all nine base methods.

```python
import Fortuna

# Data Setup
monty = Fortuna.QuantumMonty(
    ["Alpha", "Beta", "Delta", "Eta", "Gamma", "Kappa", "Zeta"]
)

# Usage
# Each of the following methods will return a random value from the sequence.
# Each method has its own unique distribution model.
""" Flat Base Case """
monty.flat_uniform()        # Flat Uniform Distribution
""" Geometric Positional """
monty.front_linear()        # Linear Descending, Triangle
monty.middle_linear()       # Linear Median Peak, Equilateral Triangle
monty.back_linear()         # Linear Ascending, Triangle
monty.quantum_linear()      # Linear Overlay, 3-way monty.
""" Gaussian Positional """
monty.front_gauss()         # Front Gamma
monty.middle_gauss()        # Scaled Gaussian
monty.back_gauss()          # Reversed Gamma
monty.quantum_gauss()       # Gaussian Overlay, 3-way monty.
""" Poisson Positional """
monty.front_poisson()       # 1/4 Mean Poisson
monty.middle_poisson()      # 1/2 Mean Poisson
monty.back_poisson()        # 3/4 Mean Poisson
monty.quantum_poisson()     # Poisson Overlay, 3-way monty.
""" Quantum Monty Algorithm """
monty()                     # Quantum Monty Algorithm, 9-way monty.
monty.quantum_monty()       #  same as above
```

### Weighted Choice: Base Class
Weighted Choice offers two strategies for selecting random values from a sequence where programmable rarity is desired. Both produce a custom distribution of values based on the weights of the values.

The choice to use one strategy over the other is purely about which one suits you or your data best. Relative weights are easier to understand at a glance. However, many RPG Treasure Tables map rather nicely to a cumulative weighted strategy.

#### Cumulative Weighted Choice
`Fortuna.CumulativeWeightedChoice(weighted_table: Table, flat=True) -> Callable -> Value`
- @param weighted_table :: Table of weighted pairs. Tuple of Tuples recommended.
- @param flat :: Bool. Default: True. Option to automatically flatten callable values with lazy evaluation.
- @return :: Callable Instance
    - @param *args, **kwargs :: Optional arguments used to flatten the return Value (below) if Callable.
    - @return :: Random value from the weighted_table, distribution based on the weights of the values.

_Note: Logic dictates Cumulative Weights must be unique!_

```python
from Fortuna import CumulativeWeightedChoice

# Data Setup
cum_weighted_choice = CumulativeWeightedChoice((
    (7, "Apple"),
    (11, "Banana"),
    (13, "Cherry"),
    (23, "Grape"),
    (26, "Lime"),
    (30, "Orange"),  # same as relative weight 4 because 30 - 26 = 4
))
# Usage
print(cum_weighted_choice())  # prints a weighted random value
```

#### Relative Weighted Choice
`Fortuna.RelativeWeightedChoice(weighted_table: Table) -> Callable -> Value`
- @param weighted_table :: Table of weighted pairs. Tuple of Tuples recommended.
- @param flat :: Bool. Default: True. Option to automatically flatten callable values with lazy evaluation.
- @return :: Callable Instance
    - @param *args, **kwargs :: Optional arguments used to flatten the return Value (below) if Callable.
    - @return :: Random value from the weighted_table, distribution based on the weights of the values.

```python
from Fortuna import RelativeWeightedChoice

# Data
population = ["Apple", "Banana", "Cherry", "Grape", "Lime", "Orange"]
rel_weights = [7, 4, 2, 10, 3, 4]

# Setup
rel_weighted_choice = RelativeWeightedChoice(zip(rel_weights, population))

# Usage
print(rel_weighted_choice())  # prints a weighted random value
```

### FlexCat
`Fortuna.FlexCat(matrix_data: Matrix, key_bias="front_linear", val_bias="truffle_shuffle", flat=True) -> Callable -> Value`
- @param matrix_data :: Dictionary of Sequences.
- @parm key_bias :: Default is "front_linear". String indicating the name of the algorithm to use for random key selection.
- @parm val_bias :: Default is "truffle_shuffle". String indicating the name of the algorithm to use for random value selection.
- @param flat :: Bool. Default is True. Option to automatically flatten callable values with lazy evaluation.
- @return :: Callable Instance
    - @param cat_key :: Optional String. Default is None. Key selection by name. If specified, this will override the key_bias for a single call.
    - @param *args, **kwargs :: Optional arguments used to flatten the return Value (below) if Callable.
    - @return :: Value. Returns a random value generated with val_bias from a random sequence generated with key_bias.

FlexCat is like a multi dimensional QuantumMonty.

The constructor takes two optional keyword arguments to specify the algorithms to be used to make random selections. The algorithm specified for selecting a key need not be the same as the one for selecting values. An optional key may be provided at call time to bypass the random key selection. Keys passed in this way must exactly match a key in the Matrix.

By default, FlexCat will use key_bias="front_linear" and val_bias="truffle_shuffle", this will make the top of the data structure geometrically more common than the bottom and it will truffle shuffle the sequence values. This config is known as TopCat, it produces a descending-step, micro-shuffled distribution sequence. Many other combinations are available.

Algorithmic Options: _See QuantumMonty & TruffleShuffle for more details._
- "front_linear", Linear Descending
- "middle_linear", Linear Median Peak
- "back_linear", Linear Ascending
- "quantum_linear", Linear 3-way monty
- "front_gauss", Gamma Descending
- "middle_gauss", Scaled Gaussian
- "back_gauss", Gamma Ascending
- "quantum_gauss", Gaussian 3-way monty
- "front_poisson", Front 1/3 Mean Poisson
- "middle_poisson", Middle Mean Poisson
- "back_poisson", Back 1/3 Mean Poisson
- "quantum_poisson", Poisson 3-way monty
- "quantum_monty", Quantum Monty Algorithm, 9-way monty
- "flat_uniform", uniform flat distribution
- "truffle_shuffle", TruffleShuffle, wide uniform distribution

```python
from Fortuna import FlexCat, d


#                           |- Collection Generator, does not require lambda.
# Data                      |
matrix_data = {#            $                         |- Dynamic Value Expression
    "Cat_A": (f"A{i}" for i in range(1, 6)),  #       |  Lazy, 1 of 4 possibilities
    "Cat_B": ("B1", "B2", "B3", "B4", "B5"),  #       $  lambda required for dynamic eval
    "Cat_C": ("C1", "C2", "C3", f"C4.{d(2)}", lambda: f"C5.{d(4)}"),
}#   $       $       $              $                        $
#    |       |       |- Value       |                        |- Fair die method: d4
#    |       |                      |
#    |       |- Collection          |- Static Value Expression
#    |                              |  Eager, 1 or 2 permanently
#    |- Collection Key, "cat_key"

#                               |- Collection Algorithm     |- Value Algorithm
# Setup                         $  y-axis                   $  x-axis
flex_cat = FlexCat(matrix_data, key_bias="front_linear", val_bias="flat_uniform")
#    $       $       $
#    |       |       |- Dictionary of Collections
#    |       |
#    |       |- FlexCat Constructor
#    |       
#    |- Callable Random Value Generator

# Usage
flex_cat()  # returns a Value from the Matrix.
flex_cat(cat_key="Cat_B")  # returns a Value specifically from the "Cat_B" Collection.
```

### Random Integer Generators
`Fortuna.random_below(number: int) -> int`
- @param number :: Any Integer
- @return :: Returns a random integer in the range...
    - `random_below(number) -> [0, number)` for positive values.
    - `random_below(number) -> (number, 0]` for negative values.
    - `random_below(0) -> 0` Always returns zero when input is zero
- Flat uniform distribution.


`Fortuna.random_int(left_limit: int, right_limit: int) -> int`
- @param left_limit :: Any Integer
- @param right_limit :: Any Integer
- @return :: Returns a random integer in the range [left_limit, right_limit]
    - `random_int(1, 10) -> [1, 10]`
    - `random_int(10, 1) -> [1, 10]` same as above.
    - `random_int(A, B)` Always returns A when A == B
- Flat uniform distribution.


`Fortuna.random_range(start: int, stop: int = 0, step: int = 1) -> int`
- @param start :: Required starting point.
    - `random_range(0) -> [0]`
    - `random_range(10) -> [0, 10)` from 0 to 9. Same as `Fortuna.random_index(N)`
    - `random_range(-10) -> [-10, 0)` from -10 to -1. Same as `Fortuna.random_index(-N)`
- @param stop :: Zero by default. Optional range bound. With at least two arguments, the order of the first two does not matter.
    - `random_range(0, 0) -> [0]`
    - `random_range(0, 10) -> [0, 10)` from 0 to 9.
    - `random_range(10, 0) -> [0, 10)` same as above.
- @param step :: One by default. Optional step size.
    - `random_range(0, 0, 0) -> [0]`
    - `random_range(0, 10, 2) -> [0, 10) by 2` even numbers from 0 to 8.
    - The sign of the step parameter controls the phase of the output. Negative stepping will flip the inclusively.
    - `random_range(0, 10, -1) -> (0, 10]` starts at 10 and ranges down to 1.
    - `random_range(10, 0, -1) -> (0, 10]` same as above.
    - `random_range(10, 10, 0) -> [10]` step size or range size of zero always returns the first parameter.
- @return :: Returns a random integer in the range [A, B) by increments of C.
- Flat uniform distribution.


`Fortuna.d(sides: int) -> int`
- Represents a single roll of a given size die.
- @param sides :: Represents the size or number of sides, most commonly six.
- @return :: Returns a random integer in the range [1, sides].
- Flat uniform distribution.


`Fortuna.dice(rolls: int, sides: int) -> int`
- Represents the sum total of multiple rolls of the same size die.
- @param rolls :: Represents the number of times to roll the die.
- @param sides :: Represents the die size or number of sides, most commonly six.
- @return :: Returns a random integer in range [X, Y] where X = rolls and Y = rolls * sides.
- Geometric distribution based on the number and size of the dice rolled.
- Complexity scales primarily with the number of rolls, not the size of the dice.


`Fortuna.plus_or_minus(number: int) -> int`
- @param number :: input to determine the output distribution range.
- @return :: Returns a random integer in range [-number, number].
- Flat uniform distribution.


`Fortuna.plus_or_minus_linear(number: int) -> int`
- @param number :: input to determine the output distribution range.
- @return :: Returns a random integer in range [-number, number].
- Linear geometric, 45 degree triangle distribution centered on zero.


`Fortuna.plus_or_minus_gauss(number: int) -> int`
- @param number :: input to determine the output distribution range.
- @return :: Returns a random integer in range [-number, number].
- Stretched gaussian distribution centered on zero.


### Random Index, ZeroCool Specification
ZeroCool Methods are used to generate random Sequence indices.

ZeroCool methods must have the following properties:
- Any distribution model is acceptable such that...
- The method or function must take exactly one Integer parameter N.
- The method returns a random int in range `[0, N)` for positive values of N.
- The method returns a random int in range `[N, 0)` for negative values of N.
- This symmetry matches how python can index a list from the back for negative values or the front for positive values of N.


```python
from Fortuna import random_index


some_list = [i for i in range(100)] # [0..99]

print(some_list[random_index(10)])  # prints one of the first 10 items of some_list, [0, 9]
print(some_list[random_index(-10)])  # prints one of the last 10 items of some_list, [90, 99]
```
### ZeroCool Methods
- `Fortuna.random_index(size: int) -> int` Flat uniform distribution
- `Fortuna.front_gauss(size: int) -> int` Gamma Distribution: Front Peak
- `Fortuna.middle_gauss(size: int) -> int` Stretched Gaussian Distribution: Median Peak
- `Fortuna.back_gauss(size: int) -> int` Gamma Distribution: Back Peak
- `Fortuna.quantum_gauss(size: int) -> int` Quantum Gaussian: Three-way Monty
- `Fortuna.front_poisson(size: int) -> int` Poisson Distribution: Front 1/3 Peak
- `Fortuna.middle_poisson(size: int) -> int` Poisson Distribution: Middle Peak
- `Fortuna.back_poisson(size: int) -> int` Poisson Distribution: Back 1/3 Peak
- `Fortuna.quantum_poisson(size: int) -> int` Quantum Poisson: Three-way Monty
- `Fortuna.front_geometric(size: int) -> int` Linear Geometric: 45 Degree Front Peak
- `Fortuna.middle_geometric(size: int) -> int` Linear Geometric: 45 Degree Middle Peak
- `Fortuna.back_geometric(size: int) -> int` Linear Geometric: 45 Degree Back Peak
- `Fortuna.quantum_geometric(size: int) -> int` Quantum Geometric: Three-way Monty
- `Fortuna.quantum_monty(size: int) -> int` Quantum Monty: Nine-way Monty

```python
from Fortuna import front_gauss, middle_gauss, back_gauss, quantum_gauss


some_list = [i for i in range(100)]

# Each of the following prints one of the first 10 items of some_list with the appropriate distribution
print(some_list[front_gauss(10)])
print(some_list[middle_gauss(10)])
print(some_list[back_gauss(10)])
print(some_list[quantum_gauss(10)])

# Each of the following prints one of the last 10 items of some_list with the appropriate distribution
print(some_list[front_gauss(-10)])  
print(some_list[middle_gauss(-10)])  
print(some_list[back_gauss(-10)])  
print(some_list[quantum_gauss(-10)])
```

### Random Float Generators
`Fortuna.canonical() -> float`
- @return :: random float in range [0.0, 1.0), flat uniform.

`Fortuna.random_float(a: Float, b: Float) -> Float`
- @param a :: Float input
- @param b :: Float input
- @return :: random Float in range [a, b), flat uniform distribution.

`Fortuna.triangular(low Float, high Float, mode Float) -> Float`
- @param low :: Float, minimum output
- @param high :: Float, maximum output
- @param mode :: Float, most common output, mode must be in range `[low, high]`
- @return :: random number in range `[low, high]` with a linear distribution about the mode.


### Random Truth Generator
`Fortuna.percent_true(truth_factor: Float = 50.0) -> bool`
- @param truth_factor :: The probability of True as a percentage. Default is 50 percent.
- @return :: Produces True or False based on the truth_factor.
    - Always returns False if num is 0 or less
    - Always returns True if num is 100 or more.


### Shuffle Algorithm
`Fortuna.shuffle(array: list) -> None`
- Knuth B shuffle algorithm. Destructive, in-place shuffle.
- Far more cache-friendly than the builtin Random.shuffle()
- @param array :: List to be shuffled.
- @return :: None


### Utilities
`Fortuna.flatten(maybe_callable, *args, flat=True, **kwargs) -> flatten(maybe_callable(*args, **kwargs))`
- Recursively calls the input object and returns the result. The arguments are only passed in on the first evaluation.
- If the maybe_callable is not callable it is simply returned without error. 
- Conceptually this is somewhat like collapsing the wave function. Often used as the last step in lazy evaluation.
- @param maybe_callable :: Any Object that might be callable.
- @param flat :: Boolean, default is True. Optional, keyword only. 
    - Disables flattening if flat is set to False, conceptually turns flatten into the identity function.
- @param *args, **kwargs :: Optional arguments used to flatten the maybe_callable object.
- @return :: Recursively Flattened Object.

`Fortuna.smart_clamp(target: int, lo: int, hi: int) -> int`
- Used to clamp the target in range [lo, hi] by saturating the bounds.
- Essentially the same as median for exactly three integers.
- @return :: Returns the middle value, input order does not matter.


### MultiChoice
```
Fortuna.MultiChoice(
    query: str, 
    *,
    options: Iterable<str> = (), 
    default: str = "", 
    strict: bool = False, 
    cursor: str = ">>>",
) -> str
```

Generates multiple-choice questions for user input on the terminal. 
If there is no user input and options is not empty and there's no default - a random choice 
will be made from the options, otherwise the default will be used. 
If there is no user input and there are no options and no default - the question 
will be repeated. 
If strict is set to true - the user input string must be in the options, 
or the question will be repeated. 
Options are stored lowercase and printed title case. User input is not case sensitive.

- @param query: String.
    - Question for the user.
- @param options: Optional Iterable of Strings. Default=()
    - Options presented to the user as a numbered sequence.
    - The user may enter an answer as text or by number.
- @param default: Optional String. 
    - This is used if no user input is provided.
    - If no default is provided a random choice will be made.
- @param strict: Optional Bool. Default=False
    - True: Answer must be in the options tuple. Not case-sensitive.
    - False: Accepts any answer.
- @param cursor: Optional String. Default='>>>' 
    - Indicates user input field.


## Fortuna Development Log
##### Fortuna 3.12.2
- Installer update.
- Clarified the docs for MultiChoice.

##### Fortuna 3.12.1
- MultiChoice now accepts a default.

##### Fortuna 3.12.0
- MultiChoice added

##### Fortuna 3.10.2
- Doc string update for clarity.
- Test update
- MonkeyScope Update

##### Fortuna 3.10.1
- Documentation fix, RandomValue examples are now together.

##### Fortuna 3.10.0
- Fortuna now includes both RNG and Pyewacket.
- Documentation update.

##### Fortuna 3.9.11
- Installer Update, properly installs MonkeyScope as intended.

##### Fortuna 3.9.10
- Fixed Typos

##### Fortuna 3.9.9
- Docs Update

##### Fortuna 3.9.8
- Test Update

##### Fortuna 3.9.7
- Tests for RNG and Pyewacket are now included in `fortuna_extras` package.

##### Fortuna 3.9.6
- Documentation update.

##### Fortuna 3.9.5
- Storm 3.2.2 Update.

##### Fortuna 3.9.4
- Documentation update.

##### Fortuna 3.9.3
- MonkeyScope update, 10% test suite performance improvement.

##### Fortuna 3.9.2
- Documentation update.

##### Fortuna 3.9.1
- `flatten_with` has been renamed to `flatten`. This should be non-breaking, please report any bugs.

##### Fortuna 3.9.0, internal
- Added many doc strings.
- Corrected many typos in Docs.
- The `flatten` function has been fully replaced by `flatten_with`. 
    - All classes that support automatic flattening can now accept arbitrary arguments at call time.
    - `flatten_with` will be renamed to `flatten` in a future release.

##### Fortuna 3.8.9
- Fixed some typos.

##### Fortuna 3.8.8
- Fortuna now supports Python notebooks, python3.6 or higher required.

##### Fortuna 3.8.7
- Storm Update

##### Fortuna 3.8.6
- Attempting to make Fortuna compatible with Python Notebooks. 

##### Fortuna 3.8.5
- Installer Config Update

##### Fortuna 3.8.4
- Installer Config Update

##### Fortuna 3.8.3
- Storm Update 3.2.0

##### Fortuna 3.8.2
- More Typo Fix

##### Fortuna 3.8.1
- Typo Fix

##### Fortuna 3.8.0
- Major API Update, several utilities have been deprecated. See MonkeyScope for replacements.
    - distribution
    - distribution_timer
    - timer

##### Fortuna 3.7.7
- Documentation Update

##### Fortuna 3.7.6
- Install script update.

##### Fortuna 3.7.5 - internal
- Storm 3.1.1 Update
- Added triangular function.

##### Fortuna 3.7.4
- Fixed: missing header in the project manifest, this may have caused building from source to fail.

##### Fortuna 3.7.3
- Storm Update

##### Fortuna 3.7.2
- Storm Update

##### Fortuna 3.7.1
- Bug fixes

##### Fortuna 3.7.0 - internal
- flatten_with() is now the default flattening algorithm for all Fortuna classes.

##### Fortuna 3.6.5
- Documentation Update
- RandomValue: New flatten-with-arguments functionality.

##### Fortuna 3.6.4
- RandomValue added for testing

##### Fortuna 3.6.3
- Developer Update

##### Fortuna 3.6.2
- Installer Script Update

##### Fortuna 3.6.1
- Documentation Update

##### Fortuna 3.6.0
- Storm Update
- Test Update
- Bug fix for random_range(), negative stepping is now working as intended. This bug was introduced in 3.5.0.
- Removed Features
    - lazy_cat(): use QuantumMonty class instead.
    - flex_cat(): use FlexCat class instead.
    - truffle_shuffle(): use TruffleShuffle class instead.

##### Fortuna 3.5.3 - internal
- Features added for testing & development
    - ActiveChoice class
    - random_rotate() function

##### Fortuna 3.5.2
- Documentation Updates

##### Fortuna 3.5.1
- Test Update

##### Fortuna 3.5.0
- Storm Update
- Minor Bug Fix: Truffle Shuffle
- Deprecated Features
    - lazy_cat(): use QuantumMonty class instead.
    - flex_cat(): use FlexCat class instead.
    - truffle_shuffle(): use TruffleShuffle class instead.

##### Fortuna 3.4.9
- Test Update

##### Fortuna 3.4.8
- Storm Update

##### Fortuna 3.4.7
- Bug fix for analytic_continuation.

##### Fortuna 3.4.6
- Docs Update

##### Fortuna 3.4.5
- Docs Update
- Range Tests Added, see extras folder.

##### Fortuna 3.4.4
- ZeroCool Algorithm Bug Fixes
- Typos Fixed

##### Fortuna 3.4.3
- Docs Update

##### Fortuna 3.4.2
- Typos Fixed

##### Fortuna 3.4.1
- Major Bug Fix: random_index()

##### Fortuna 3.4.0 - internal
- ZeroCool Poisson Algorithm Family Updated

##### Fortuna 3.3.8 - internal
- Docs Update

##### Fortuna 3.3.7
- Fixed Performance Bug: ZeroCool Linear Algorithm Family

##### Fortuna 3.3.6
- Docs Update

##### Fortuna 3.3.5
- ABI Updates
- Bug Fixes

##### Fortuna 3.3.4
- Examples Update

##### Fortuna 3.3.3
- Test Suite Update

##### Fortuna 3.3.2 - internal
- Documentation Update

##### Fortuna 3.3.1 - internal
- Minor Bug Fix

##### Fortuna 3.3.0 - internal
- Added `plus_or_minus_gauss(N: int) -> int` random int in range [-N, N] Stretched Gaussian Distribution

##### Fortuna 3.2.3
- Small Typos Fixed

##### Fortuna 3.2.2
- Documentation update.

##### Fortuna 3.2.1
- Small Typo Fixed

##### Fortuna 3.2.0
- API updates:
    - QunatumMonty.uniform -> QunatumMonty.flat_uniform
    - QunatumMonty.front -> QunatumMonty.front_linear
    - QunatumMonty.middle -> QunatumMonty.middle_linear
    - QunatumMonty.back -> QunatumMonty.back_linear
    - QunatumMonty.quantum -> QunatumMonty.quantum_linear
    - randindex -> random_index
    - randbelow -> random_below
    - randrange -> random_range
    - randint   -> random_int

##### Fortuna 3.1.0
- `discrete()` has been removed, see Weighted Choice.
- `lazy_cat()` added.
- All ZeroCool methods have been raised to top level API, for use with lazy_cat()

##### Fortuna 3.0.1
- minor typos.

##### Fortuna 3.0.0
- Storm 2 Rebuild.

##### Fortuna 2.1.1
- Small bug fixes.
- Test updates.

##### Fortuna 2.1.0, Major Feature Update
- Fortuna now includes the best of RNG and Pyewacket.

##### Fortuna 2.0.3
- Bug fix.

##### Fortuna 2.0.2
- Clarified some documentation.

##### Fortuna 2.0.1
- Fixed some typos.

##### Fortuna 2.0.0b1-10
- Total rebuild. New RNG Storm Engine.

##### Fortuna 1.26.7.1
- README updated.

##### Fortuna 1.26.7
- Small bug fix.

##### Fortuna 1.26.6
- Updated README to reflect recent changes to the test script.

##### Fortuna 1.26.5
- Fixed small bug in test script.

##### Fortuna 1.26.4
- Updated documentation for clarity.
- Fixed a minor typo in the test script.

##### Fortuna 1.26.3
- Clean build.

##### Fortuna 1.26.2
- Fixed some minor typos.

##### Fortuna 1.26.1
- Release.

##### Fortuna 1.26.0 beta 2
- Moved README and LICENSE files into fortuna_extras folder.

##### Fortuna 1.26.0 beta 1
- Dynamic version scheme implemented.
- The Fortuna Extension now requires the fortuna_extras package, previously it was optional.

##### Fortuna 1.25.4
- Fixed some minor typos in the test script.

##### Fortuna 1.25.3
- Since version 1.24 Fortuna requires Python 3.7 or higher. This patch corrects an issue where the setup script incorrectly reported requiring Python 3.6 or higher.

##### Fortuna 1.25.2
- Updated test suite.
- Major performance update for TruffleShuffle.
- Minor performance update for QuantumMonty & FlexCat: cycle monty.

##### Fortuna 1.25.1
- Important bug fix for TruffleShuffle, QuantumMonty and FlexCat.

##### Fortuna 1.25
- Full 64bit support.
- The Distribution & Performance Tests have been redesigned.
- Bloat Control: Two experimental features have been removed.
    - RandomWalk
    - CatWalk
- Bloat Control: Several utility functions have been removed from the top level API. These function remain in the Fortuna namespace for now, but may change in the future without warning.
    - stretch_bell, internal only.
    - min_max, not used anymore.
    - analytic_continuation, internal only.
    - flatten, internal only.

##### Fortuna 1.24.3
- Low level refactoring, non-breaking patch.

##### Fortuna 1.24.2
- Setup config updated to improve installation.

##### Fortuna 1.24.1
- Low level patch to avoid potential ADL issue. All low level function calls are now qualified.

##### Fortuna 1.24
- Documentation updated for even more clarity.
- Bloat Control: Two naïve utility functions that are no longer used in the module have been removed.
    - n_samples -> use a list comprehension instead. `[f(x) for _ in range(n)]`
    - bind -> use a lambda instead. `lambda: f(x)`

##### Fortuna 1.23.7
- Documentation updated for clarity.
- Minor bug fixes.
- TruffleShuffle has been redesigned slightly, it now uses a random rotate instead of swap.
- Custom `__repr__` methods have been added to each class.

##### Fortuna 1.23.6
- New method for QuantumMonty: quantum_not_monty - produces the upside down quantum_monty.
- New bias option for FlexCat: not_monty.

##### Fortuna 1.23.5.1
- Fixed some small typos.

##### Fortuna 1.23.5
- Documentation updated for clarity.
- All sequence wrappers can now accept generators as input.
- Six new functions added:
    - random_float() -> float in range [0.0..1.0) exclusive, uniform flat distribution.
    - percent_true_float(num: float) -> bool, Like percent_true but with floating point precision.
    - plus_or_minus_linear_down(num: int) -> int in range [-num..num], upside down pyramid.
    - plus_or_minus_curve_down(num: int) -> int in range [-num..num], upside down bell curve.
    - mostly_not_middle(num: int) -> int in range [0..num], upside down pyramid.
    - mostly_not_center(num: int) -> int in range [0..num], upside down bell curve.
- Two new methods for QuantumMonty:
    - mostly_not_middle
    - mostly_not_center
- Two new bias options for FlexCat, either can be used to define x and/or y axis bias:
    - not_middle
    - not_center

##### Fortuna 1.23.4.2
- Fixed some minor typos in the README.md file.

##### Fortuna 1.23.4.1
- Fixed some minor typos in the test suite.

##### Fortuna 1.23.4
- Fortuna is now Production/Stable!
- Fortuna and Fortuna Pure now use the same test suite.

##### Fortuna 0.23.4, first release candidate.
- RandomCycle, BlockCycle and TruffleShuffle have been refactored and combined into one class: TruffleShuffle.
- QuantumMonty and FlexCat will now use the new TruffleShuffle for cycling.
- Minor refactoring across the module.

##### Fortuna 0.23.3, internal
- Function shuffle(arr: list) added.

##### Fortuna 0.23.2, internal
- Simplified the plus_or_minus_curve(num: int) function, output will now always be bounded to the range [-num..num].
- Function stretched_bell(num: int) added, this matches the previous behavior of an unbounded plus_or_minus_curve.

##### Fortuna 0.23.1, internal
- Small bug fixes and general clean up.

##### Fortuna 0.23.0
- The number of test cycles in the test suite has been reduced to 10,000 (down from 100,000). The performance of the pure python implementation and the c-extension are now directly comparable.
- Minor tweaks made to the examples in `.../fortuna_extras/fortuna_examples.py`

##### Fortuna 0.22.2, experimental features
- BlockCycle class added.
- RandomWalk class added.
- CatWalk class added.

##### Fortuna 0.22.1
- Fortuna classes no longer return lists of values, this behavior has been extracted to a free function called n_samples.

##### Fortuna 0.22.0, experimental features
- Function bind added.
- Function n_samples added.

##### Fortuna 0.21.3
- Flatten will no longer raise an error if passed a callable item that it can't call. It correctly returns such items in an uncalled state without error.
- Simplified `.../fortuna_extras/fortuna_examples.py` - removed unnecessary class structure.

##### Fortuna 0.21.2
- Fix some minor bugs.

##### Fortuna 0.21.1
- Fixed a bug in `.../fortuna_extras/fortuna_examples.py`

##### Fortuna 0.21.0
- Function flatten added.
- Flatten: The Fortuna classes will recursively unpack callable objects in the data set.

##### Fortuna 0.20.10
- Documentation updated.

##### Fortuna 0.20.9
- Minor bug fixes.

##### Fortuna 0.20.8, internal
- Testing cycle for potential new features.

##### Fortuna 0.20.7
- Documentation updated for clarity.

##### Fortuna 0.20.6
- Tests updated based on recent changes.

##### Fortuna 0.20.5, internal
- Documentation updated based on recent changes.

##### Fortuna 0.20.4, internal
- WeightedChoice (both types) can optionally return a list of samples rather than just one value, control the length of the list via the n_samples argument.

##### Fortuna 0.20.3, internal
- RandomCycle can optionally return a list of samples rather than just one value,
control the length of the list via the n_samples argument.

##### Fortuna 0.20.2, internal
- QuantumMonty can optionally return a list of samples rather than just one value,
control the length of the list via the n_samples argument.

##### Fortuna 0.20.1, internal
- FlexCat can optionally return a list of samples rather than just one value,
control the length of the list via the n_samples argument.

##### Fortuna 0.20.0, internal
- FlexCat now accepts a standard dict as input. The ordered(ness) of dict is now part of the standard in Python 3.7.1. Previously FlexCat required an OrderedDict, now it accepts either and treats them the same.

##### Fortuna 0.19.7
- Fixed bug in `.../fortuna_extras/fortuna_examples.py`.

##### Fortuna 0.19.6
- Updated documentation formatting.
- Small performance tweak for QuantumMonty and FlexCat.

##### Fortuna 0.19.5
- Minor documentation update.

##### Fortuna 0.19.4
- Minor update to all classes for better debugging.

##### Fortuna 0.19.3
- Updated plus_or_minus_curve to allow unbounded output.

##### Fortuna 0.19.2
- Internal development cycle.
- Minor update to FlexCat for better debugging.

##### Fortuna 0.19.1
- Internal development cycle.

##### Fortuna 0.19.0
- Updated documentation for clarity.
- MultiCat has been removed, it is replaced by FlexCat.
- Mostly has been removed, it is replaced by QuantumMonty.

##### Fortuna 0.18.7
- Fixed some more README typos.

##### Fortuna 0.18.6
- Fixed some README typos.

##### Fortuna 0.18.5
- Updated documentation.
- Fixed another minor test bug.

##### Fortuna 0.18.4
- Updated documentation to reflect recent changes.
- Fixed some small test bugs.
- Reduced default number of test cycles to 10,000 - down from 100,000.

##### Fortuna 0.18.3
- Fixed some minor README typos.

##### Fortuna 0.18.2
- Fixed a bug with Fortuna Pure.

##### Fortuna 0.18.1
- Fixed some minor typos.
- Added tests for `.../fortuna_extras/fortuna_pure.py`

##### Fortuna 0.18.0
- Introduced new test format, now includes average call time in nanoseconds.
- Reduced default number of test cycles to 100,000 - down from 1,000,000.
- Added pure Python implementation of Fortuna: `.../fortuna_extras/fortuna_pure.py`
- Promoted several low level functions to top level.
    - `zero_flat(num: int) -> int`
    - `zero_cool(num: int) -> int`
    - `zero_extreme(num: int) -> int`
    - `max_cool(num: int) -> int`
    - `max_extreme(num: int) -> int`
    - `analytic_continuation(func: staticmethod, num: int) -> int`
    - `min_max(num: int, lo: int, hi: int) -> int`

##### Fortuna 0.17.3
- Internal development cycle.

##### Fortuna 0.17.2
- User Requested: dice() and d() functions now support negative numbers as input.

##### Fortuna 0.17.1
- Fixed some minor typos.

##### Fortuna 0.17.0
- Added QuantumMonty to replace Mostly, same default behavior with more options.
- Mostly is depreciated and may be removed in a future release.
- Added FlexCat to replace MultiCat, same default behavior with more options.
- MultiCat is depreciated and may be removed in a future release.
- Expanded the Treasure Table example in `.../fortuna_extras/fortuna_examples.py`

##### Fortuna 0.16.2
- Minor refactoring for WeightedChoice.

##### Fortuna 0.16.1
- Redesigned fortuna_examples.py to feature a dynamic random magic item generator.
- Raised cumulative_weighted_choice function to top level.
- Added test for cumulative_weighted_choice as free function.
- Updated MultiCat documentation for clarity.

##### Fortuna 0.16.0
- Pushed distribution_timer to the .pyx layer.
- Changed default number of iterations of tests to 1 million, up form 1 hundred thousand.
- Reordered tests to better match documentation.
- Added Base Case Fortuna.fast_rand_below.
- Added Base Case Fortuna.fast_d.
- Added Base Case Fortuna.fast_dice.

##### Fortuna 0.15.10
- Internal Development Cycle

##### Fortuna 0.15.9
- Added Base Cases for random_value()
- Added Base Case for randint()

##### Fortuna 0.15.8
- Clarified MultiCat Test

##### Fortuna 0.15.7
- Fixed minor typos.

##### Fortuna 0.15.6
- Fixed minor typos.
- Simplified MultiCat example.

##### Fortuna 0.15.5
- Added MultiCat test.
- Fixed some minor typos in docs.

##### Fortuna 0.15.4
- Performance optimization for both WeightedChoice() variants.
- Cython update provides small performance enhancement across the board.
- Compilation now leverages Python3 all the way down.
- MultiCat pushed to the .pyx layer for better performance.

##### Fortuna 0.15.3
- Reworked the MultiCat example to include several randomizing strategies working in concert.
- Added Multi Dice 10d10 performance tests.
- Updated sudo code in documentation to be more pythonic.

##### Fortuna 0.15.2
- Fixed: Linux installation failure.
- Added: complete source files to the distribution (.cpp .hpp .pyx).

##### Fortuna 0.15.1
- Updated & simplified distribution_timer in `fortuna_tests.py`
- Readme updated, fixed some typos.
- Known issue preventing successful installation on some linux platforms.

##### Fortuna 0.15.0
- Performance tweaks.
- Readme updated, added some details.

##### Fortuna 0.14.1
- Readme updated, fixed some typos.

##### Fortuna 0.14.0
- Fixed a bug where the analytic continuation algorithm caused a rare issue during compilation on some platforms.

##### Fortuna 0.13.3
- Fixed Test Bug: percent sign was missing in output distributions.
- Readme updated: added update history, fixed some typos.

##### Fortuna 0.13.2
- Readme updated for even more clarity.

##### Fortuna 0.13.1
- Readme updated for clarity.

##### Fortuna 0.13.0
- Minor Bug Fixes.
- Readme updated for aesthetics.
- Added Tests: `.../fortuna_extras/fortuna_tests.py`

##### Fortuna 0.12.0
- Internal test for future update.

##### Fortuna 0.11.0
- Initial Release: Public Beta

##### Fortuna 0.10.0
- Module name changed from Dice to Fortuna

##### Dice 0.1.x - 0.9.x
- Experimental Phase


## Distribution and Performance Tests
```
MonkeyScope: Fortuna Quick Test

Random Sequence Values:

some_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Base Case
Output Analysis: Random.choice(some_list)
Typical Timing: 756 ± 37 ns
Statistics of 1000 samples:
 Minimum: 0
 Median: 5
 Maximum: 9
 Mean: 4.583
 Std Deviation: 2.82473202268817
Distribution of 100000 samples:
 0: 9.911%
 1: 9.938%
 2: 9.928%
 3: 10.028%
 4: 10.039%
 5: 10.158%
 6: 10.186%
 7: 9.988%
 8: 9.939%
 9: 9.885%

Output Analysis: random_value(some_list)
Typical Timing: 68 ± 5 ns
Statistics of 1000 samples:
 Minimum: 0
 Median: 5
 Maximum: 9
 Mean: 4.537
 Std Deviation: 2.87830349337939
Distribution of 100000 samples:
 0: 9.832%
 1: 10.134%
 2: 10.025%
 3: 9.935%
 4: 9.929%
 5: 9.972%
 6: 9.92%
 7: 10.029%
 8: 10.121%
 9: 10.103%

Output Analysis: TruffleShuffle(collection)()
Typical Timing: 494 ± 18 ns
Statistics of 1000 samples:
 Minimum: 0
 Median: 5
 Maximum: 9
 Mean: 4.563
 Std Deviation: 2.901384324766369
Distribution of 100000 samples:
 0: 9.958%
 1: 10.068%
 2: 10.039%
 3: 10.034%
 4: 9.921%
 5: 9.942%
 6: 10.011%
 7: 9.876%
 8: 10.126%
 9: 10.025%

Output Analysis: QuantumMonty(collection)()
Typical Timing: 535 ± 32 ns
Statistics of 1000 samples:
 Minimum: 0
 Median: 5
 Maximum: 9
 Mean: 4.629
 Std Deviation: 2.8381964343575654
Distribution of 100000 samples:
 0: 10.802%
 1: 8.845%
 2: 9.047%
 3: 9.614%
 4: 11.543%
 5: 11.68%
 6: 9.642%
 7: 9.096%
 8: 8.965%
 9: 10.766%

Output Analysis: RandomValue(collection)()
Typical Timing: 415 ± 2 ns
Statistics of 1000 samples:
 Minimum: 0
 Median: (4, 5)
 Maximum: 9
 Mean: 4.492
 Std Deviation: 2.9130629927964136
Distribution of 100000 samples:
 0: 9.979%
 1: 9.964%
 2: 9.984%
 3: 10.16%
 4: 9.865%
 5: 9.91%
 6: 10.074%
 7: 10.132%
 8: 10.041%
 9: 9.891%


Weighted Tables:

population = ('A', 'B', 'C', 'D')
cum_weights = (1, 3, 6, 10)
rel_weights = (1, 2, 3, 4)
cum_weighted_table = zip(cum_weights, population)
rel_weighted_table = zip(rel_weights, population)

Cumulative Base Case
Output Analysis: Random.choices(population, cum_weights=cum_weights)
Typical Timing: 1679 ± 62 ns
Distribution of 100000 samples:
 A: 10.156%
 B: 20.199%
 C: 29.817%
 D: 39.828%

Output Analysis: CumulativeWeightedChoice(weighted_table)()
Typical Timing: 410 ± 14 ns
Distribution of 100000 samples:
 A: 9.897%
 B: 19.943%
 C: 29.991%
 D: 40.169%

Output Analysis: cumulative_weighted_choice(tuple(zip(cum_weights, population)))
Typical Timing: 134 ± 2 ns
Distribution of 100000 samples:
 A: 9.977%
 B: 19.833%
 C: 29.861%
 D: 40.329%

Relative Base Case
Output Analysis: Random.choices(population, weights=rel_weights)
Typical Timing: 2125 ± 97 ns
Distribution of 100000 samples:
 A: 9.865%
 B: 19.75%
 C: 30.065%
 D: 40.32%

Output Analysis: RelativeWeightedChoice(weighted_table)()
Typical Timing: 412 ± 18 ns
Distribution of 100000 samples:
 A: 10.1%
 B: 20.213%
 C: 29.849%
 D: 39.838%


Random Matrix Values:

some_matrix = {'A': (1, 2, 3, 4), 'B': (10, 20, 30, 40), 'C': (100, 200, 300, 400)}

Output Analysis: FlexCat(matrix_data, key_bias, val_bias, flat)()
Typical Timing: 790 ± 29 ns
Statistics of 1000 samples:
 Minimum: 1
 Median: 20
 Maximum: 400
 Mean: 87.94
 Std Deviation: 125.1696305019712
Distribution of 100000 samples:
 1: 8.266%
 2: 8.151%
 3: 8.248%
 4: 8.376%
 10: 8.423%
 20: 8.328%
 30: 8.496%
 40: 8.264%
 100: 8.257%
 200: 8.402%
 300: 8.497%
 400: 8.292%


Random Integers:

Base Case
Output Analysis: Random.randrange(10)
Typical Timing: 866 ± 56 ns
Statistics of 1000 samples:
 Minimum: 0
 Median: 4
 Maximum: 9
 Mean: 4.51
 Std Deviation: 2.884423685937973
Distribution of 100000 samples:
 0: 9.904%
 1: 9.882%
 2: 10.015%
 3: 10.138%
 4: 10.023%
 5: 9.9%
 6: 9.93%
 7: 10.076%
 8: 10.053%
 9: 10.079%

Output Analysis: random_below(10)
Typical Timing: 67 ± 5 ns
Statistics of 1000 samples:
 Minimum: 0
 Median: 4
 Maximum: 9
 Mean: 4.437
 Std Deviation: 2.8736790008628312
Distribution of 100000 samples:
 0: 10.025%
 1: 9.919%
 2: 10.237%
 3: 9.984%
 4: 9.852%
 5: 9.992%
 6: 10.002%
 7: 10.005%
 8: 9.956%
 9: 10.028%

Output Analysis: random_index(10)
Typical Timing: 63 ± 2 ns
Statistics of 1000 samples:
 Minimum: 0
 Median: 5
 Maximum: 9
 Mean: 4.581
 Std Deviation: 2.843842295205555
Distribution of 100000 samples:
 0: 10.004%
 1: 10.02%
 2: 10.048%
 3: 10.046%
 4: 10.028%
 5: 9.984%
 6: 9.828%
 7: 10.158%
 8: 9.961%
 9: 9.923%

Output Analysis: random_range(10)
Typical Timing: 99 ± 14 ns
Statistics of 1000 samples:
 Minimum: 0
 Median: 5
 Maximum: 9
 Mean: 4.537
 Std Deviation: 2.874827125237273
Distribution of 100000 samples:
 0: 10.086%
 1: 10.032%
 2: 9.965%
 3: 9.908%
 4: 9.962%
 5: 10.051%
 6: 10.082%
 7: 9.932%
 8: 10.036%
 9: 9.946%

Output Analysis: random_below(-10)
Typical Timing: 79 ± 9 ns
Statistics of 1000 samples:
 Minimum: -9
 Median: -4
 Maximum: 0
 Mean: -4.433
 Std Deviation: 2.9260059808551313
Distribution of 100000 samples:
 -9: 10.024%
 -8: 10.018%
 -7: 10.022%
 -6: 9.918%
 -5: 9.937%
 -4: 10.082%
 -3: 10.104%
 -2: 9.825%
 -1: 9.944%
 0: 10.126%

Output Analysis: random_index(-10)
Typical Timing: 84 ± 11 ns
Statistics of 1000 samples:
 Minimum: -10
 Median: -6
 Maximum: -1
 Mean: -5.553
 Std Deviation: 2.8662154489849505
Distribution of 100000 samples:
 -10: 9.75%
 -9: 10.027%
 -8: 10.144%
 -7: 10.156%
 -6: 9.918%
 -5: 10.04%
 -4: 10.038%
 -3: 9.888%
 -2: 10.166%
 -1: 9.873%

Output Analysis: random_range(-10)
Typical Timing: 105 ± 8 ns
Statistics of 1000 samples:
 Minimum: -10
 Median: -5
 Maximum: -1
 Mean: -5.389
 Std Deviation: 2.785261029059934
Distribution of 100000 samples:
 -10: 9.871%
 -9: 9.886%
 -8: 10.107%
 -7: 10.041%
 -6: 9.859%
 -5: 10.061%
 -4: 10.083%
 -3: 9.952%
 -2: 10.071%
 -1: 10.069%

Base Case
Output Analysis: Random.randrange(1, 10)
Typical Timing: 1099 ± 52 ns
Statistics of 1000 samples:
 Minimum: 1
 Median: 5
 Maximum: 9
 Mean: 5.038
 Std Deviation: 2.5769276280097584
Distribution of 100000 samples:
 1: 11.176%
 2: 11.043%
 3: 11.128%
 4: 11.13%
 5: 11.221%
 6: 11.214%
 7: 10.978%
 8: 11.0%
 9: 11.11%

Output Analysis: random_range(1, 10)
Typical Timing: 98 ± 9 ns
Statistics of 1000 samples:
 Minimum: 1
 Median: 5
 Maximum: 9
 Mean: 4.941
 Std Deviation: 2.528145367655903
Distribution of 100000 samples:
 1: 10.967%
 2: 11.103%
 3: 11.099%
 4: 11.107%
 5: 11.352%
 6: 11.084%
 7: 11.143%
 8: 11.079%
 9: 11.066%

Output Analysis: random_range(10, 1)
Typical Timing: 103 ± 14 ns
Statistics of 1000 samples:
 Minimum: 1
 Median: 5
 Maximum: 9
 Mean: 4.901
 Std Deviation: 2.5599216784894026
Distribution of 100000 samples:
 1: 10.913%
 2: 11.298%
 3: 11.075%
 4: 11.295%
 5: 11.06%
 6: 11.185%
 7: 11.091%
 8: 11.144%
 9: 10.939%

Base Case
Output Analysis: Random.randint(-5, 5)
Typical Timing: 1204 ± 56 ns
Statistics of 1000 samples:
 Minimum: -5
 Median: 0
 Maximum: 5
 Mean: -0.137
 Std Deviation: 3.2187312717901757
Distribution of 100000 samples:
 -5: 9.045%
 -4: 9.198%
 -3: 9.11%
 -2: 9.056%
 -1: 9.122%
 0: 9.033%
 1: 9.144%
 2: 9.148%
 3: 8.952%
 4: 9.066%
 5: 9.126%

Output Analysis: random_int(-5, 5)
Typical Timing: 59 ± 2 ns
Statistics of 1000 samples:
 Minimum: -5
 Median: 0
 Maximum: 5
 Mean: 0.229
 Std Deviation: 3.105247011108778
Distribution of 100000 samples:
 -5: 9.069%
 -4: 9.028%
 -3: 9.159%
 -2: 9.043%
 -1: 9.193%
 0: 9.151%
 1: 9.066%
 2: 9.189%
 3: 8.962%
 4: 9.121%
 5: 9.019%

Base Case
Output Analysis: Random.randrange(1, 20, 2)
Typical Timing: 1323 ± 84 ns
Statistics of 1000 samples:
 Minimum: 1
 Median: 9
 Maximum: 19
 Mean: 9.902
 Std Deviation: 5.75138209476644
Distribution of 100000 samples:
 1: 9.957%
 3: 10.061%
 5: 9.99%
 7: 9.828%
 9: 10.022%
 11: 10.027%
 13: 10.05%
 15: 10.095%
 17: 10.08%
 19: 9.89%

Output Analysis: random_range(1, 20, 2)
Typical Timing: 84 ± 2 ns
Statistics of 1000 samples:
 Minimum: 1
 Median: 9
 Maximum: 19
 Mean: 9.876
 Std Deviation: 5.647001328138678
Distribution of 100000 samples:
 1: 10.074%
 3: 10.234%
 5: 10.168%
 7: 9.892%
 9: 9.866%
 11: 9.887%
 13: 10.062%
 15: 9.797%
 17: 10.044%
 19: 9.976%

Output Analysis: random_range(1, 20, -2)
Typical Timing: 95 ± 7 ns
Statistics of 1000 samples:
 Minimum: 2
 Median: 10
 Maximum: 20
 Mean: 10.882
 Std Deviation: 5.642169440915436
Distribution of 100000 samples:
 2: 9.88%
 4: 10.017%
 6: 10.077%
 8: 10.076%
 10: 10.088%
 12: 9.998%
 14: 9.921%
 16: 9.93%
 18: 10.082%
 20: 9.931%

Output Analysis: random_range(20, 1, -2)
Typical Timing: 106 ± 17 ns
Statistics of 1000 samples:
 Minimum: 2
 Median: (10, 12)
 Maximum: 20
 Mean: 10.976
 Std Deviation: 5.84255286668422
Distribution of 100000 samples:
 2: 9.939%
 4: 10.208%
 6: 9.975%
 8: 9.968%
 10: 9.923%
 12: 10.129%
 14: 10.112%
 16: 9.872%
 18: 9.86%
 20: 10.014%

Output Analysis: d(10)
Typical Timing: 62 ± 8 ns
Statistics of 1000 samples:
 Minimum: 1
 Median: 5
 Maximum: 10
 Mean: 5.396
 Std Deviation: 2.834287211981171
Distribution of 100000 samples:
 1: 9.946%
 2: 9.947%
 3: 9.96%
 4: 9.967%
 5: 10.073%
 6: 10.132%
 7: 10.022%
 8: 9.977%
 9: 9.958%
 10: 10.018%

Output Analysis: dice(3, 6)
Typical Timing: 131 ± 15 ns
Statistics of 1000 samples:
 Minimum: 3
 Median: 11
 Maximum: 18
 Mean: 10.632
 Std Deviation: 3.0183730717060144
Distribution of 100000 samples:
 3: 0.441%
 4: 1.425%
 5: 2.743%
 6: 4.694%
 7: 7.002%
 8: 9.679%
 9: 11.504%
 10: 12.674%
 11: 12.369%
 12: 11.532%
 13: 9.878%
 14: 6.776%
 15: 4.644%
 16: 2.815%
 17: 1.374%
 18: 0.45%

Output Analysis: ability_dice(4)
Typical Timing: 204 ± 12 ns
Statistics of 1000 samples:
 Minimum: 3
 Median: 13
 Maximum: 18
 Mean: 12.371
 Std Deviation: 2.9029913882063103
Distribution of 100000 samples:
 3: 0.072%
 4: 0.339%
 5: 0.796%
 6: 1.575%
 7: 2.945%
 8: 4.799%
 9: 6.849%
 10: 9.509%
 11: 11.426%
 12: 13.006%
 13: 13.305%
 14: 12.23%
 15: 10.11%
 16: 7.248%
 17: 4.194%
 18: 1.597%

Output Analysis: plus_or_minus(5)
Typical Timing: 56 ± 2 ns
Statistics of 1000 samples:
 Minimum: -5
 Median: 0
 Maximum: 5
 Mean: 0.079
 Std Deviation: 3.0946339040345303
Distribution of 100000 samples:
 -5: 9.022%
 -4: 9.194%
 -3: 8.949%
 -2: 9.128%
 -1: 9.219%
 0: 9.013%
 1: 9.107%
 2: 9.076%
 3: 9.052%
 4: 9.099%
 5: 9.141%

Output Analysis: plus_or_minus_linear(5)
Typical Timing: 83 ± 2 ns
Statistics of 1000 samples:
 Minimum: -5
 Median: 0
 Maximum: 5
 Mean: -0.009
 Std Deviation: 2.4134868965875906
Distribution of 100000 samples:
 -5: 2.779%
 -4: 5.622%
 -3: 8.338%
 -2: 11.162%
 -1: 13.719%
 0: 16.577%
 1: 14.008%
 2: 11.227%
 3: 8.159%
 4: 5.569%
 5: 2.84%

Output Analysis: plus_or_minus_gauss(5)
Typical Timing: 115 ± 14 ns
Statistics of 1000 samples:
 Minimum: -5
 Median: 0
 Maximum: 5
 Mean: -0.014
 Std Deviation: 1.584867186864565
Distribution of 100000 samples:
 -5: 0.204%
 -4: 1.117%
 -3: 4.274%
 -2: 11.564%
 -1: 20.362%
 0: 24.831%
 1: 20.362%
 2: 11.489%
 3: 4.457%
 4: 1.138%
 5: 0.202%


Random Floats:

Base Case
Output Analysis: Random.random()
Typical Timing: 42 ± 11 ns
Statistics of 1000 samples:
 Minimum: 0.0009616764620485885
 Median: (0.5068175331606152, 0.5089658155046862)
 Maximum: 0.9982838662275418
 Mean: 0.4999739344141985
 Std Deviation: 0.29211996366058657
Post-processor distribution of 100000 samples using round method:
 0: 49.785%
 1: 50.215%

Output Analysis: canonical()
Typical Timing: 43 ± 9 ns
Statistics of 1000 samples:
 Minimum: 0.0001499986206673609
 Median: (0.5256180884519401, 0.5267333326284235)
 Maximum: 0.9987776702468752
 Mean: 0.5135041970434493
 Std Deviation: 0.28767392852246
Post-processor distribution of 100000 samples using round method:
 0: 49.978%
 1: 50.022%

Output Analysis: random_float(0.0, 10.0)
Typical Timing: 36 ± 1 ns
Statistics of 1000 samples:
 Minimum: 0.00539603165477888
 Median: (5.035795403968255, 5.051762657831246)
 Maximum: 9.999362964704904
 Mean: 5.018559609048081
 Std Deviation: 2.8919006687955298
Post-processor distribution of 100000 samples using floor method:
 0: 9.916%
 1: 9.849%
 2: 10.109%
 3: 10.027%
 4: 9.989%
 5: 9.97%
 6: 10.153%
 7: 10.148%
 8: 9.948%
 9: 9.891%

Base Case
Output Analysis: Random.triangular(0.0, 10.0, 5.0)
Typical Timing: 470 ± 10 ns
Statistics of 1000 samples:
 Minimum: 0.23228334398754466
 Median: (4.898918558352428, 4.906044359130979)
 Maximum: 9.736419970638513
 Mean: 4.989299413945522
 Std Deviation: 2.0238004381748365
Post-processor distribution of 100000 samples using round method:
 0: 0.533%
 1: 3.974%
 2: 8.014%
 3: 12.173%
 4: 15.899%
 5: 18.967%
 6: 15.932%
 7: 12.034%
 8: 8.126%
 9: 3.861%
 10: 0.487%

Output Analysis: triangular(0.0, 10.0, 5.0)
Typical Timing: 55 ± 6 ns
Statistics of 1000 samples:
 Minimum: 0.13378838733443907
 Median: (4.9767533702792575, 4.983290830895762)
 Maximum: 9.699284558402505
 Mean: 4.984496860126553
 Std Deviation: 2.082676902150332
Post-processor distribution of 100000 samples using round method:
 0: 0.483%
 1: 4.046%
 2: 7.873%
 3: 11.941%
 4: 16.099%
 5: 18.717%
 6: 16.117%
 7: 12.093%
 8: 8.076%
 9: 4.052%
 10: 0.503%


Random Booleans:

Output Analysis: percent_true(33.33)
Typical Timing: 37 ± 2 ns
Statistics of 1000 samples:
 Minimum: False
 Median: False
 Maximum: True
 Mean: 0.346
 Std Deviation: 0.4756931784249171
Distribution of 100000 samples:
 False: 66.771%
 True: 33.229%


Shuffle Performance:

some_small_list = [i for i in range(10)]
some_med_list = [i for i in range(100)]
some_large_list = [i for i in range(1000)]

Base Case:
Random.shuffle()
Typical Timing: 7073 ± 329 ns
Typical Timing: 65785 ± 356 ns
Typical Timing: 690462 ± 4192 ns

Fortuna.shuffle()
Typical Timing: 308 ± 70 ns
Typical Timing: 3648 ± 38 ns
Typical Timing: 35656 ± 131 ns


-------------------------------------------------------------------------
Total Test Time: 3.291 seconds

```


## Legal Information
Fortuna © 2019 Robert W Sharp, all rights reserved.

Fortuna is licensed under a Creative Commons Attribution-NonCommercial 3.0 Unported License.

See online version of this license here: <http://creativecommons.org/licenses/by-nc/3.0/>
