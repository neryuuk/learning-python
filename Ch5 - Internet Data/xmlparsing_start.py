import xml.dom.minidom


def main():
    # use the parse() function to load and parse an XML file
    doc = xml.dom.minidom.parse("samplexml.xml")
    print(doc.nodeName)
    print(doc.firstChild.tagName)
    print("---------------------------------------------\n")

    # print out the document node and the name of the first child tag
    skills = doc.getElementsByTagName("skill")
    print("{} skills are listed".format(skills.length))
    for skill in skills:
        print(skill.getAttribute("name"))
    print("---------------------------------------------\n")

    # get a list of XML tags from the document and print each one
    newSkill = doc.createElement("skill")
    newSkill.setAttribute("name", "jQuery")
    doc.firstChild.appendChild(newSkill)

    # create a new XML tag and add it into the document
    skills = doc.getElementsByTagName("skill")
    print("{} skills are listed".format(skills.length))
    for skill in skills:
        print(skill.getAttribute("name"))


if __name__ == "__main__":
    main()
