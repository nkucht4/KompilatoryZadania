import sys
import json
class Scanner:
    def __init__(self):
        with open("tokens/tokens.json", "r") as file:
            self.tokens = json.load(file)

    def run(self, in_filename, out_filename):
        file = open(in_filename, "r")
        while True:
            symbol = file.read(1)
            if not symbol:
                break
            token = self.scan(symbol, file)
        file.close()

    def scan(self, symbol, file):
        raise NotImplementedError

def main():
    if len(sys.argv) == 1:
        print("No input file specified")
        return
    elif len(sys.argv) == 2:
        print("No output file specified")
        return

    filenames = sys.argv[1:]
    file_scanner = Scanner()
    file_scanner.run(filenames[0], filenames[1])

if __name__ == "__main__":
    main()