import urllib.request
import json


def printResults(data):
    # Use the json module to load the string data into a dictionary
    content = json.loads(data)

    # now we can access the contents of the JSON like any other Python object
    if "metadata" in content and "title" in content["metadata"]:
        print(content["metadata"]["title"])
        print("---------------------------------------------\n")

    # output the number of events, plus the magnitude and each event name
    if "metadata" in content and "count" in content["metadata"]:
        print("{} event(s) recorded".format(content["metadata"]["count"]))
        print("---------------------------------------------\n")

    # for each event, print the place where it occurred
    if "features" in content:
        for event in content["features"]:
            if "properties" in event and "place" in event["properties"]:
                print(event["properties"]["place"])
    print("---------------------------------------------\n")

    # print the events that only have a magnitude greater than 4
    print("Events with magnitude greater than 4:\n")
    if "features" in content:
        for event in content["features"]:
            if "properties" in event and "mag" in event["properties"] and event["properties"]["mag"] > 4:
                print("{}, Magnitude {}".format(
                    event["properties"]["place"],
                    event["properties"]["mag"]
                ))
    print("---------------------------------------------\n")

    # print only the events where at least 1 person reported feeling something
    print("Events that were felt by someone:\n")
    if "features" in content:
        for event in content["features"]:
            if "properties" in event and "felt" in event["properties"]:
                felt = event["properties"]["felt"]
                if felt and int(felt) > 0:
                    print("{}, felt {} time{}".format(
                        event["properties"]["place"],
                        felt,
                        "s" if felt > 1 else ""
                    ))
    print("---------------------------------------------\n")


def main():
    # define a variable to hold the source URL
    # In this case we'll use the free data feed from the USGS
    # This feed lists all earthquakes for the last day larger than Mag 2.5
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    try:
        # Open the URL and read the data
        website = urllib.request.urlopen(url)
        httpStatus = website.getcode()
        print("GET {} {}".format(url, httpStatus))
        if httpStatus == 200:
            printResults(website.read())
        else:
            print("Received HTTP status {} from the server.".format(httpStatus))
    except Exception as e:
        print("Error opening website {}:\n{}".format(url, e))


if __name__ == "__main__":
    main()
