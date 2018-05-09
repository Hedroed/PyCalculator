#!/usr/bin/env python3
# coding: utf-8

from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.formatted_text import ANSI
import re


p_xor = re.compile(r'([^\s]+)\s*\^\s*([^\s]+)')
p_quotes = re.compile(r'^([^"\']+):.*')
p_b64 = re.compile(r'[A-Za-z0-9+/]+={0,2}')
p_int = re.compile(r'[0-9]+')
p_hex = re.compile(r'(\\x|0x)?[0-9a-fA-F]+')


def detectType(arg):

    availables_type = ['str', 'int', 'float', 'b64', 'b32', 'hex']

    # Manual type
    m = p_quotes.match(arg)
    if m:
        arg_type = m.group(1)
        if arg_type in availables_type:
            return arg_type
        # Else: continue to automatic detection

    # Automatic type detection
    if p_int.match(arg):
        return 'int'

    if p_hex.match(arg):
        return 'hex'

    # Default
    return 'str'


def parse(cmd):

    m = p_xor.match(cmd)
    if m:
        arg1 = m.group(1)
        arg2 = m.group(2)
        print("%s: %s" % (arg1, detectType(arg1)))
        print("%s: %s" % (arg2, detectType(arg2)))
        return 1

    # Default = error
    return 0


if __name__ == '__main__':

    history = InMemoryHistory()
    status_color = "\033[92m"

    while True:
        try:
            cmd = prompt(ANSI(status_color + ">> "), history=history)
        except KeyboardInterrupt:
            continue  # Control-C pressed. Try again.
        except EOFError:
            break  # Control-D pressed.

        if parse(cmd):
            # Success
            status_color = "\033[92m"
        else:
            # Error
            status_color = "\033[91m"
