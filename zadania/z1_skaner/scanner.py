from sys import argv


def main():
    if len(argv) == 1:
        print("No input file specified")
        return
    filenames = argv[1:]


main()
