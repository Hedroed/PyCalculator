# PyCalculator

Simple syntax for complex data transformations

## Requirements

[python-prompt-toolkit](https://github.com/jonathanslenders/python-prompt-toolkit)

## Install

```bash
python3 setup.py install
```

## Start

```bash
pycalc
```

## Prototype

### Data conversion

Classic Int to hex with keyword **to**
```
>>> 12345 to hex
hex: 3039
```

Base64 to ascii
```
>>> ZXhhbXBsZQ== to ascii
Ascii: example
```

Force type with key word **as**
```
>>> "30 39" as hex to int
int: 12345
```

### Automatic recognition

Hexadecimal with **0x** prefix
```
>>> 0x2a
hex: 2a
```

Binary with **0b** prefix
```
>>> 0x1010
bit: 1010
```

Base64
```
>>> ZXhhbXBsZQ==
base64: ZXhhbXBsZQ==
```

Interger
```
>>> 12345
int: 12345
```

### Math

```
>>> 1 + 1
int: 2
```

Math operation return value of type of the first operand
```
>>> 0x10 * 0b10
hex: 0x20
```

### Crypto

> **TODO:** Find syntax for the following

- RSA
  - private key generation
  - public key generation
- Hash (MD5, SHA1, SHA256, ...)
- Caesar
  - With key
  - Bruteforce
- ASCII Caesar
  - With key
  - Bruteforce
- XOR
  - With key
  - Known-plaintext attack
  - Xored plaintext attack (cf cryptopals)

### Encoding

> **TODO:** Find syntax for the following

- URL encode / decode
- Double encode
- Base64
- Base32
- Hex

### File

Load data from file
```
>>> dir/file.txt as textFile
ascii: A text file
```

And from binary file
```
>>> dir/file.txt as binFile
bytes: \x41\x20\x62\x69\x6e\x20\x66\x69\x6c\x65
```

### Variable

Save value in variable
```
>>> 1 + 1 in var1
int: 2 (var1)
```

Use value from varable
```
>>> $var1 * 0xa
int: 20
```

List all varables
```
>>> $
int: 2 (var1)
bin: 1010 (tmp)
unicode: a string (f)
```

### Types

List of possible data types:
 - Int
 - Ascii
 - Unicode
 - Bytes
 - Bitarray / Bits
 - Hex
 - Base64
 - Base32
 - Octal ?
 - binFile
 - textFile

### Operator

There are 3 types of operators:
 - modifiers (as, to, in)
 - computers with one operand (factorial)
 - computers with tow operand(+, -, xor, rsa...)


List of possible operator:
 - `+`
 - `-`
 - `/`
 - `*`
 - `to` / `.`
 - `as`
 - `xor` / `^`
 - `rsa`

### Types definition

Un **Type** est une class *Python* qui hérite d'une class particulière

Idée de méthodes à redéfinir:
 - toString: appelé quand une donnée de ce type est la valeur de retour
 - format: appelé par **as**
 - detect: appelé pour détecter automatiquement si un string est de ce type. Si `detect` retourn `True` alors la donnée est de ce type est la méthode `format` est appelé.
 (Systeme de priorité)
 - toBytes and fromBytes: for default convertion

Un type aura un nom pour le differencier des autres types, par default il prendra le nom de ça class mais il sera possible de le redefinir

Il faudrat ajouter ce type aux registres des types connus
Exemple:

```python
from pycalclib import registerType, TypeBase
import re

class PCInt(TypeBase):
    name = 'Int'

    def format(self, value):
        return int(value)

    def detect(self, value):
        return re.test(r'(0|[1-9][0-9]*)', value)  # ex: 12345 (/!\ 01 not work)

    def toString(self, value):
        return value

# Register an Object
registerType(Int())
```

### Operator definition

Un **Operator* est une class *Python* qui hérite d'une class particulière

Une operation doit avoir un type par defaut pour effectuer son calcule
Il sera possible de specifier un comportement en fonction de **Type** particulier

Il faudra definir le *symbol* qui permet de reconnaitre l'operation, il pourrait y en avoir plusieurs (`xor` et `^`)

Exemple:
```python
from pycalclib import registerOperator, OperatorBase

class Addition(OperatorBase):
    default = 'Int'
    symbols = ['+']

    def __init__(self):
        self.registerOperationFor('Hex', self.hexOp)


    def compute(self, first, second):
        return first + second

    def hexOp(self, first, second):
        return first + second

# Register an Object
registerOperator(Addition())
```

### Stockage des données

Une donnée sera stocké dans un object **Data**
Il contiendra:
 - la valeur sous n'importe quelle forme
 - le nom du type de cette valeur

Les variable seront stockées dans un dictionnaire avec :
 - comme clé le nom de la variable
 - comme valeur l'object **Data**


### Interpretor

Ex: convert int to base64, save in variable and write in text file
```
>>> 12345678 to base64 in myVar write /tmp/file.txt as textFile
base64: vGFO (myVar)
```

Cut operation:
 - 12345678 to base64:
 1) Call `detect` of all **Type** and make list of possible **Type**: Here there is only 'Int'
 2) Call format method of `Int` and save data in **Data** object as *current value*
 3) Find operator: is `to` for convertion
 4) Find **Type** to convert: is `base64`
 5) Find if there is specific method in `Int` to convert to `base64`
 6) No specific method, so convert `Int` to default **Type**: `Bytes`
 7) Call `toBytes` method of `Int`
 8) Call `fromBytes` method of `base64`
 9) A data of **Type** `base64` is created

 - ... in myVar
 1) Find next operator: is `in` for variable
 2) Get varable name: `myVar`
 3) Save *current value* in variable dictionnary

 - ... write ...
 1) Find next operator: is `write`, is not a built in operator
 2) compute the ***Second*** operand, start after `write` and stop at the next *not a built in operator* or the end of the line

 - /tmp/file.txt as textFile
 1) Detect the `as` operator
 2) Find the **Type**: is `textFile`
 3) Call format of `textFile`
 4) A data of **Type** `textFile` is created

Return at `write` operator

 - ... write ...
 1) `base64` write in `textFile`
 2) Search for specific method for `base64` in `write` operator: there is not
 3) Call `compute` of `write`
 4) get the return and continue: for write the return is the first operand

 - No more operations
 1) get the *current value*
 2) call toString
 3) print the type name
 4) print a column (:)
 5) print return of toString

