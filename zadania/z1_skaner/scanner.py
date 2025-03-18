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
        if not symbol.isspace():
            if symbol in self.tokens.keys():
                print(f'TOKEN {self.tokens[symbol]}: {symbol}')

            elif symbol.isdigit():
                start_col = file.tell()
                nxt = file.read(1)
                while (nxt.isdigit()):
                    symbol += nxt
                    nxt = file.read(1)
                if nxt in self.tokens.keys() or not nxt:
                    print(f'TOKEN LICZBA: {symbol}')
                    if nxt:
                        print(f'TOKEN {self.tokens[nxt]}: {nxt}')
                else:
                    self.handle_error(file, start_col)

            elif symbol.isalpha():
                start_col = file.tell()
                nxt = file.read(1)
                while (nxt.isalnum()):
                    symbol += nxt
                    nxt = file.read(1)
                if nxt in self.tokens.keys() or not nxt:
                    print(f'TOKEN IDENTYFIKATOR: {symbol}')
                    if nxt:
                        print(f'TOKEN {self.tokens[nxt]}: {nxt}')
                else:
                    self.handle_error(file, start_col)

            else:
                col_nr = file.tell()
                self.handle_error(file, col_nr)

    def handle_error(self, file, col_nr):
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
