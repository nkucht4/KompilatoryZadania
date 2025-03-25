import sys
import json
class Scanner:
    def __init__(self, in_filename, out_filename):
        with open("tokens/tokens.json", "r") as file:
            self.tokens = json.load(file)
            file = open(in_filename, "r")
            while True:
                symbol = file.read(1)
                if not symbol:
                    break
                token = self.next(symbol, file)
            file.close()

    def run(self):
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