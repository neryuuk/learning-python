def main():
    # Open a file for writing and create it if it doesn't exist
    # myfile = open("textfile.txt", "w+")

    # Open the file for appending text to the end
    # myfile = open("textfile.txt", "a+")

    # write some lines of data to the file
    # for i in range(10):
    #     myfile.write("This is some new text\n")

    # close the file when done
    # myfile.close()

    # Open the file back up and read the contents
    myfile = open("textfile.txt", "r")
    # if myfile.mode == 'r':
    #     contents = myfile.read()
    #     print(contents)
    if myfile.mode == 'r':
        lines = myfile.readlines()
        for line in lines:
            print(line)


if __name__ == "__main__":
    main()
