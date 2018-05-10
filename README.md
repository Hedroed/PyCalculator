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

Il faudrat ajouter ce type aux registres des types connus
Exemple:

```python
from pycalclib import registerType

class Int(TypeBase):
    ...

registerType(Int)
```

