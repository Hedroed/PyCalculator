# PyCalculator

Simple syntax for complex data transformations.

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


Caesar
```
>>> '57 69 59 5f 5f 55 59 57 5b 69 57 68' as bytes caesar 10 to ascii
ascii: ascii_caesar
```


Xor bin file with known key
```
>>> tmp/file.crypt as binFile xor TheSecretKey write /tmp/out as binFile
bytes: \x41\x20\x62\x69\x6e...\x20\x66\x69\x6c\x65
```


### Encoding

> **TODO:** Find syntax for the following

- URL encode / decode
- Double encode
- Base64
- Base32
- Hex


Url encode and decode
```
>>> urlEncode "' or 1=1 #"
ascii: %27%20or%201%3D1%20%23

>>> urlDecode %27%20or%201%3D1%20%23
ascii: ' or 1=1 #
```

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
 <!-- - Base64
 - Base32 -->
 - Octal ?
 - binFile
 - textFile

### Modifier

Modifiers affect a single data, it is not an operator

List of modifiers:
 - `to` / `.`
 - `as`
 - `in`

### Operator

List of possible operator:
 - `+`
 - `-`
 - `/`
 - `*`
 - `xor` / `^`
 - `rsa`
 - `abs'
 - `factorial` / `!`


Operator like python function but it can take the first parameter at this left. This allow to chain operator

```
>>> abs -42
int: 42
```

Factorial
```
>>> ! 0b101 to int
int: 120
```

chaining
```
>>> -4 abs factorial
int: 24
```

To string operator, not the same as `to ascii`
```
>>> 6162 string
ascii: 6162

>>> 6162 to ascii
ascii: ab
```
Because `to` will transform value to bytes before convert.


### computation order and priority

The interpretor read code from left to right but it is possible to use parenthesis to make action prioritary.

example:
```
>>> 42 * (a as hex - 8)
int: 84
```


### Escaping space

To escape space it is possible to use the `\` escape charactere.
Put text in `"` also escape space.

If you want to escape the first sentence and you have forgot to place a `"` at the start you can just put a `"` at the end to the sentence and the interpretor with automatically place a `"` at the start.



### Types definition

Un **Type** est une class *Python* qui hérite d'une classe particulière.

Idée de méthodes à redéfinir:
 - toString: appelée quand une donnée de ce type est la valeur de retour
 - format: appelé par **as**
 - detect: appelé pour détecter automatiquement si un string est de ce type. Si `detect` retourne `True`, alors la donnée est de ce type et la méthode `format` est appelée.
 (Systeme de priorité)
 - toBytes and fromBytes: for default conversion

Un type aura un nom pour le différencier des autres types, par défaut il prendra le nom de sa classe mais il sera possible de le redéfinir.

Il faudrat ajouter ce type aux registres des types connus
Exemple:

```python
from pycalclib import registerType, BaseType
import re

class PCInt(BaseType):
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

Un **Operator* est une classe *Python* qui hérite d'une classe particulière.

Une opération doit avoir un type par défaut pour effectuer son calcule.
Il sera possible de spécifier un comportement en fonction d'un **Type** particulier.

Il faudra définir le *symbol* qui permet de reconnaitre l'operation, il pourrait y en avoir plusieurs (`xor` et `^`)

Exemple:
```python
from pycalclib import registerOperator, BaseOperator

class Addition(BaseOperator):
    default = 'Int'
    symbols = ['+']

    def compute(self, first, second):
        return first + second

    @self.registerOp('Hex')
    def hexOp(self, first, second):
        return first + second

    @self.registerOp('Ascii')
    def asciiConcat(self, first, second):
        return first + second

# Register an Object
registerOperator(Addition())
```

### Stockage des données

Une donnée sera stockée dans un objet **Data**.

Il contiendra:
 - la valeur sous n'importe quelle forme
 - le nom du type de cette valeur

Les variable seront stockées dans un dictionnaire avec :
 - comme clé le nom de la variable
 - comme valeur l'objet **Data**


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
 3) Find modifier: is `to` for convertion
 4) Find **Type** to convert: is `base64`
 5) Find if there is specific method in `Int` to convert to `base64`
 6) No specific method, so convert `Int` to default **Type**: `Bytes`
 7) Call `toBytes` method of `Int`
 8) Call `fromBytes` method of `base64`
 9) A data of **Type** `base64` is created

 - ... in myVar
 1) Find next modifier: is `in` for variable
 2) Get varable name: `myVar`
 3) Save *current value* in variable dictionnary

 - ... write ...
 1) Find next operator: is `write`, is not a modifier
 2) compute the ***Second*** operand, start after `write` and stop at the next operator or the end of the line

 - /tmp/file.txt as textFile
 1) Detect the `as` modifier
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


### CLI integration (BASH)

Example:
```shell
KnownXorAttack.py /tmp/crypt ${pycalc -c "169846466316 to ascii"} > /tmp/file.decrypt
```