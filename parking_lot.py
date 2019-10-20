from service.park_service import EntryService, ExitService
from argparse import ArgumentParser, ArgumentError
import sys

from input_processor import ProcessInput

def main(args):
    arglen = len(args)
    
    pi = ProcessInput()
    
    if arglen == 1:
        # Interactive Mode
        pi.interactive_mode()
    elif arglen == 2:
        # File Input Mode
        pi.file_input_mode(args[1])


if __name__ == '__main__':
    args = sys.argv
    main(args)