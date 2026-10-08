# 🐍 KodNest Python Learning Repository

Welcome to the **KodNest Python Learning Repository**. This repository contains structured, well-commented, and formatted practice programs covering fundamental to intermediate Python concepts.

---

## 📁 Repository Structure

```tree
Kodnest/
│
├── 📂 Module_01_Python_Basics/
│   ├── 01_first_program.py            # Basic print() functions and f-strings
│   ├── 02_variables.py                # Variables, assignment & string formatting
│   ├── 03_datatypes.py                # Primitive datatypes (int, float, str, bool, complex)
│   ├── 04_input_handling.py           # User input handling & typecasting
│   ├── 05_conditional_statements.py   # If, if-else, nested if, and match-case
│   ├── 06_looping_statements.py       # For loops, while loops, jump statements & functions
│   └── 07_pseudocode_and_logic.py     # Algorithms, pseudocode & core logic problems
│
└── 📂 Module_02_Data_Structures/
    ├── 📂 01_Strings/
    │   ├── 01_string_basics.py        # String literals, multiline quotes & concatenation
    │   ├── 02_string_immutability.py  # Immutability, memory IDs and 'is' vs '=='
    │   ├── 03_string_methods.py       # Inbuilt methods (upper, find, split, join, etc.)
    │   ├── 04_positive_slicing.py     # Comprehensive positive slicing practice
    │   └── 05_negative_slicing.py     # Negative indexing and reverse slicing
    │
    ├── 📂 02_Lists/
    │   ├── 01_list_basics.py          # List operations, append, extend, insert, pop, sort
    │   ├── 02_list_mutation.py        # List mutation vs reassignment
    │   └── 03_shallow_and_deep_copy.py# Normal reference vs shallow copy vs deepcopy
    │
    ├── 📂 03_Tuples/
    │   ├── 01_tuple_basics.py         # Tuples, packing, unpacking, immutability
    │   └── 02_tuple_slicing.py        # 30 Comprehensive tuple slicing exercises
    │
    └── 📂 04_Sets/
        ├── 01_set_basics.py           # Set definition, uniqueness, add, discard, frozenset
        └── 02_set_methods.py          # Union, intersection, difference, subset methods
```

---

## 🚀 Topics Covered

### 🔹 Module 1: Python Fundamentals & Control Flow
1. **First Program & Output**: Understanding `print()` syntax, string interpolation with f-strings.
2. **Variables & Data Types**: Dynamic typing, type discovery with `type()`, integer, float, string, boolean, and complex types.
3. **Input Handling**: Reading input from standard input, converting string input to numbers with `int()`.
4. **Conditional Statements**: Decision making with `if`, `elif`, `else`, nested conditions, and pattern matching with `match-case`.
5. **Loops & Iteration**: Iterating using `for` with `range()`, `while` loops, jumping statements (`break`, `continue`, `pass`), and basic function creation.
6. **Pseudocode & Algorithms**: Translating logical flowcharts and algorithms into Python code.

### 🔹 Module 2: Data Structures
1. **Strings (`str`)**:
   - Quotes, string operations, and identity testing (`id()`, `is`, `==`).
   - Built-in methods (`upper()`, `lower()`, `find()`, `replace()`, `split()`, `join()`, etc.).
   - Slicing syntax: `string[start:stop:step]` (positive and negative indices).
2. **Lists (`list`)**:
   - Ordered, mutable collections.
   - Adding/removing items (`append`, `extend`, `insert`, `pop`, `remove`, `clear`).
   - Aliasing vs Deep Copying (`copy.deepcopy()`).
3. **Tuples (`tuple`)**:
   - Ordered, immutable collections.
   - Tuple packing and extended unpacking (`*rest`).
   - Slicing and multi-dimensional tuple indexing.
4. **Sets (`set` & `frozenset`)**:
   - Unordered, unindexed collections with unique elements.
   - Mathematical set operations: Union (`|`), Intersection (`&`), Difference (`-`), Symmetric Difference (`^`).
   - Set relationship tests: `isdisjoint()`, `issubset()`, `issuperset()`.

---

## 💻 How to Run Any Script

Open your terminal or command prompt in the `Kodnest` root directory and execute:

```bash
# Example: Run Python Basics
python Module_01_Python_Basics/01_first_program.py

# Example: Run String Slicing Practice
python Module_02_Data_Structures/01_Strings/04_positive_slicing.py

# Example: Run Set Methods
python Module_02_Data_Structures/04_Sets/02_set_methods.py
```
