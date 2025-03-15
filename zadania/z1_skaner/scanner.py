from sys import argv
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
            ##print(symbol)
        file.close()

    def next(self, symbol, col_nr):
        #todo
        raise NotImplementedError

    def get_token(self, symbol):
        #get token                  easy
        raise NotImplementedError
    def handleError(self, col_nr):
        #handleerror        1 line
        raise NotImplementedError

def main():
    if len(argv) == 1:
        print("No input file specified")
        return
    filenames = argv[1:]
    file_scanner = Scanner()
    for filename in filenames:
        file_scanner.run(filename)

if __name__ == "__main__":
    main()
