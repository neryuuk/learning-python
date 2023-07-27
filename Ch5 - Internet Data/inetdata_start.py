import urllib.request


def main():
    # open a connection to a URL using urllib2
    url = "https://google.com"
    weburl = urllib.request.urlopen(url)

    # get the result code and print it
    print("GET {} {}".format(url, weburl.getcode()))

    # read the data from the URL and print it
    data = weburl.read()
    print("PAYLOAD {}".format(data))


if __name__ == "__main__":
    main()
