# Ch-1_OOP: Object-Oriented Programming Fundamentals

This folder contains comprehensive examples and demonstrations of Object-Oriented Programming (OOP) concepts in Python. The files progress from basic concepts to more advanced patterns and best practices.

## 📁 Folder Structure

### Python Files (Concepts Progress)

#### 1. **1_basics.py** - Enterprise-Grade OOP Fundamentals
The most advanced file showcasing industry-level OOP best practices:
- **Enums**: `PersonType` enum for type safety
- **Dataclasses**: Immutable `PersonInfo` dataclass with validation
- **Abstract Base Classes**: `Communicator` ABC with abstract methods
- **Properties**: Read-only property accessors
- **Context Managers**: Custom context managers for session management
- **Caching**: `@lru_cache` for performance optimization
- **Design Patterns**: Factory pattern with `PersonFactory`
- **Class & Static Methods**: Class-level and utility methods
- **Logging**: Enterprise logging setup and usage
- **Magic Methods**: `__repr__`, `__str__`, `__enter__`, `__exit__`

**Key Classes:**
- `Person`: Main class with full lifecycle management
- `ConsoleCommunicator`: Concrete implementation of Communicator
- `PersonFactory`: Factory for creating pre-configured Person instances

---

#### 2. **2_constructors.py** - Constructors & Instance Variables
Introduces the constructor (`__init__`) method and how objects are initialized:
- **Class Variables**: Variables shared across all instances (`var1`, `var2`)
- **Instance Variables**: Variables unique to each object (`dyn1`, `dyn2`, `dyn3`)
- **Constructor Method**: `__init__` method called when object is created
- **Object Instantiation**: Creating objects and calling methods

**Concepts:**
- Difference between class and instance variables
- Dynamic initialization of objects at runtime
- Two ways to call instance methods: `obj.func()` and `ClassName.func(obj)`

---

#### 3. **3_encapsulation.py** - Data Encapsulation & Access Modifiers
Demonstrates encapsulation and visibility levels of instance variables:
- **Public Variables**: Prefixed with nothing (e.g., `self.dyn1`)
  - Can be accessed and modified freely from outside
- **Private Variables**: Prefixed with double underscore (e.g., `self.__dyn2`)
  - Name mangling prevents direct access; attempts create new attributes
  - True data hiding in Python
- **Protected Variables**: Prefixed with single underscore (e.g., `self._dyn3`)
  - Convention-based; technically accessible but signals "don't use outside class"

**Key Insight:**
Shows how Python's name mangling works: `obj.__var` becomes `obj._ClassName__var` internally

---

#### 4. **4_DataExt_Class.py** - File Data Extraction Utility
Real-world example of a class for reading multiple file formats using pandas:
- **Multiple File Format Support**: CSV, JSON, Parquet
- **Pandas Integration**: Uses pandas DataFrame for data handling
- **Flexible Constructor**: Takes file path as parameter
- **Specialized Methods**: Different methods for different file types
  - `fetch_text()`: Reads text-based files (CSV, TSV) with custom separators
  - `fetch_json()`: Reads JSON files
  - `fetch_parquet()`: Reads Parquet files

**Data Files Used:**
- orders.csv, orders.json, orders.parquet, orders.tsv (in `Files/` folder)

---

#### 5. **5_methods.py** - Methods & Special Methods
Explores different types of methods in Python:
- **Magic/Dunder Methods**: Special methods starting with `__`
  - `__init__`: Constructor method
  - `__str__`: String representation for users
- **Class Methods**: Methods that operate on the class itself
  - `@classmethod` decorator
  - Access class variables and modify class state
- **Static Methods**: Utility methods that don't need instance or class state
  - `@staticmethod` decorator
  - Behave like regular functions but belong to the class namespace

**Concepts Shown:**
- How different method types are called and what parameters they receive
- Using decorators to define method behavior

---

#### 6. **practice.py** - Simple Practice Class
A beginner-friendly example combining basic OOP concepts:
- Simple `morning` class with constructor
- Class variables and instance variables
- Instance methods for greeting and displaying name
- Good starting point for understanding OOP basics

---

### 📊 Files Folder
Contains sample data files used in the learning materials:
- `orders.csv` - CSV format (comma-separated values)
- `orders.json` - JSON format (JavaScript Object Notation)
- `orders.parquet` - Parquet format (columnar storage, efficient for data science)
- `orders.tsv` - TSV format (tab-separated values)

---

## 🎓 Learning Path

**Recommended progression:**

1. **Start with `practice.py`** → Understand basic class structure
2. **Move to `2_constructors.py`** → Learn about initialization and instance variables
3. **Study `3_encapsulation.py`** → Understand data hiding and access control
4. **Explore `5_methods.py`** → Learn different method types
5. **Practice with `4_DataExt_Class.py`** → Real-world application example
6. **Master `1_basics.py`** → Advanced patterns and enterprise practices

---

## 🔑 Key OOP Concepts Covered

| Concept | File | Description |
|---------|------|-------------|
| Classes & Objects | 2_constructors.py | Creating and using classes |
| Constructors | 2_constructors.py | `__init__` method |
| Instance Variables | 2_constructors.py | Per-object state |
| Class Variables | 2_constructors.py | Shared across all instances |
| Encapsulation | 3_encapsulation.py | Data hiding with public/private/protected |
| Methods | 5_methods.py | Instance, class, and static methods |
| Magic Methods | 1_basics.py, 5_methods.py | Special methods like `__init__`, `__str__` |
| Abstract Classes | 1_basics.py | ABC and abstract methods |
| Dataclasses | 1_basics.py | Modern way to define data containers |
| Properties | 1_basics.py | Read-only attributes with `@property` |
| Context Managers | 1_basics.py | Resource management with `with` statement |
| Design Patterns | 1_basics.py | Factory pattern implementation |
| Logging | 1_basics.py | Professional logging setup |

---

## 🚀 How to Run

Each file can be executed independently:

```python
# Run any Python file
python 1_basics.py
python 2_constructors.py
python 3_encapsulation.py
python 4_DataExt_Class.py
python 5_methods.py
python practice.py
```

**Note:** `4_DataExt_Class.py` requires pandas library to be installed:
```bash
pip install pandas
```

---

## 💡 Key Takeaways

- **OOP in Python is flexible**: Multiple ways to achieve the same thing
- **Start simple, build up**: Basic classes → constructors → encapsulation → advanced patterns
- **Best practices matter**: `1_basics.py` shows production-ready code with logging, validation, and design patterns
- **Real-world applications**: `4_DataExt_Class.py` demonstrates practical file handling
- **Python conventions**: Use single `_` and double `__` prefixes as signals to other developers

---

## 📝 Notes

- All code follows Python naming conventions (snake_case for functions/variables, PascalCase for classes)
- Comments and docstrings explain the purpose and usage of each concept
- The progression in file numbers (1→5) represents increasing complexity and advanced concepts
- `practice.py` serves as a simple starting point for hands-on practice
