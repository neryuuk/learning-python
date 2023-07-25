# Create directory results
# Create file results.txt within directory
# Write into the created file
#   total byte count of all files
#   the listing of files from current directory

from os import listdir, mkdir, path


def main():
    createDirectory("results")
    writeData(computeData("./"), "results/results.txt")


def createDirectory(name):
    try:
        mkdir(name)
    except FileExistsError:
        print("Folder '{}' already exists".format(name))
    except Exception as e:
        print("Could not create directory: {}".format(e))
        exit(1)


def writeData(data, filePath):
    with open(filePath, "w+") as results:
        if results.mode == "w+":
            results.write("Total bytecount: {}\n".format(data[0]))
            results.write("Files list:\n")
            results.write("--------------\n")
            results.write("{}\n".format("\n".join(data[1])))
        results.close()


def computeData(dir):
    bytecount = 0
    files = []
    for item in listdir(dir):
        if path.isfile(item):
            bytecount += path.getsize(item)
            files.append(item)
    return bytecount, files


if __name__ == "__main__":
    main()
