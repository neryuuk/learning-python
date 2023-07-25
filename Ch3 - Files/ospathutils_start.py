from os import name, path
from datetime import datetime
import time


def main():
    # Print the name of the OS
    print(name)

    # Check for item existence and type
    print("Item exists: {}".format(path.exists("textfile.txt")))
    print("Item is a file: {}".format(path.isfile("textfile.txt")))
    print("Item is a directory: {}".format(path.isdir("textfile.txt")))

    # Work with file paths
    print("Item's path is: {}".format(path.realpath("textfile.txt")))
    print("Item's path and name: {}".format(
        path.split(path.realpath("textfile.txt"))
    ))

    # Get the modification time
    t = time.ctime(path.getmtime("textfile.txt"))
    print(t)
    print(datetime.fromtimestamp(path.getmtime("textfile.txt")))

    # Calculate how long ago the item was modified
    td = datetime.now() - datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print("It has been {} since the file was modified".format(td))
    print("Or, {} seconds".format(td.total_seconds()))


if __name__ == "__main__":
    main()
