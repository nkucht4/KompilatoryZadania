from sys import argv

class Scanner:
    def __init__(self):
        #importujemy json z tokenami        1 line
        raise NotImplementedError

    def run(self, file):
        #run
        raise NotImplementedError

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

if __name__ == "__main__":
    main()
