import sys
import json

class Scanner:
    def __init__(self):
        with open("tokens/tokens.json", "r") as file:
            self.tokens = json.load(file)

    def run(self, filename):
        file = open(filename, "r")
        while True:
            symbol = file.read(1)
            if not symbol:
                break
            self.next(symbol, file)
        file.close()

    def next(self, symbol, file):
        if symbol.isprintable():
            if symbol in self.tokens.values():
                # TO DO
            if symbol.isdigit():
                # TO DO
            if symbol.isnumeric():
                # TO DO
            else:
                self.handle_error(file)

    def handle_error(self, file):
        col_nr = file.tell()
        file.close()
        sys.exit(f'Incorrect token in column {col_nr}')

def main():
    if len(sys.argv) == 1:
        print("No input file specified")
        return
    filenames = sys.argv[1:]
    file_scanner = Scanner()
    for filename in filenames:
        file_scanner.run(filename)

if __name__ == "__main__":
    main()
