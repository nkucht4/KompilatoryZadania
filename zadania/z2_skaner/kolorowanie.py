import sys
import json
class Scanner:
    def __init__(self):
        with open("tokens/long_tokens.json", "r") as file:
            long_tokens = json.load(file)
        with open("tokens/one_char_tokens.json", "r") as file:
            self.one_char_tokens = json.load(file)
        self.line_counter = 0
        self.token_to_color = {}
        self.long_tokens = {}
        for k, i in long_tokens.items():
            for v in i.values():
                self.token_to_color[v] = k
            self.long_tokens.update(i)
        print(self.token_to_color)
        print(self.long_tokens)


    def run(self, in_filename, out_filename):
        self.line_counter = 0
        file = open(in_filename, "r")
        while True:
            symbol = file.read(1)
            if not symbol:
                break
            token = self.scan(symbol, file)
        file.close()

    def scan(self, symbol, file):
        if symbol == '\n':
            self.line_counter += 1
        # WHITESPACES
        if not symbol.isprintable():
            return ("WHITE", symbol)
        # DIGITS
        elif symbol.isdigit():
            nxt = self.next(file)
            is_float = False
            while nxt.isdigit() or nxt == '.':
                if nxt == '.':
                    if is_float == True:
                        self.handle_error(file, "Unexpected '.'")
                    else:
                        is_float = True
                symbol += file.read(1)
            if not nxt.isprintable() or nxt not in self.one_char_tokens:
                if is_float == False:
                    return ("LIGHT_GREEN", symbol)
                else:
                    return ("ORANGE", symbol)
        #TO DO - identyfikatory
        #TO DO jednoliterowe
        #TO DO - Stringi i komentarze
        # TO DO więcej

    def next(self, file):
        nxt_char = file.read(1)
        file.seek(file.tell() - 1)
        return nxt_char

    def handle_error(self, message):
        return ("RED", f'Lexical error at line: {self.line_counter}: {message}')

def main():
    if len(sys.argv) == 1:
        print("No input file specified")
        return
    elif len(sys.argv) == 2:
        print("No output file specified")
        return

    filenames = sys.argv[1:]
    file_scanner = Scanner()
    #file_scanner.run(filenames[0], filenames[1])

if __name__ == "__main__":
    main()