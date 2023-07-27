#
# Example file for parsing and processing HTML
# LinkedIn Learning Python course by Joe Marini
#

from html.parser import HTMLParser

paragraphs = 0


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print("Encountered a comment: '{}'".format(data))
        pos = self.getpos()
        print("At line {}, position {}".format(pos[0], pos[1]))

    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag: '{}'".format(tag))
        pos = self.getpos()
        print("At line {}, position {}".format(pos[0], pos[1]))

        global paragraphs
        if tag == "p":
            paragraphs += 1

        if len(attrs) > 0:
            print("Attributes:")
            for att in attrs:
                print("\t{} = {}".format(att[0], att[1]))

    def handle_data(self, data):
        if (data.isspace()):
            return

        print("Encountered text data: {}".format(data))
        pos = self.getpos()
        print("At line {}, position {}".format(pos[0], pos[1]))


def main():
    # instantiate the parser and feed it some HTML
    parser = MyHTMLParser()

    f = open("samplehtml.html")
    if f.mode == "r":
        contents = f.read()  # read the entire file
        parser.feed(contents)

    print("Paragraphs tags: {}".format(paragraphs))


if __name__ == "__main__":
    main()
