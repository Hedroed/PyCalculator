"""
For CLI usage
"""
import argparse

from .Interpretor import Interpretor

DESCRIPTION = "PyCalc"


def parse_args():
    """Arguments parsing."""
    parser = argparse.ArgumentParser(description=DESCRIPTION)

    parser.add_argument('-c',
                        '--cmd',
                        type=str,
                        help='a command to interpret put result in stdout')

    parser.add_argument('-f',
                        '--file',
                        type=str,
                        help='a specific path to a save file.')

    parser.add_argument('-v',
                        '--verbose',
                        help='verbose mode',
                        action='count',
                        default=0
                        )

    args = parser.parse_args()

    return args


if __name__ == '__main__':
    parse = parse_args()

    it = Interpretor()

    if parse.cmd:
        print(it.interpret(parse.cmd))
