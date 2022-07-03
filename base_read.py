import xml.etree.ElementTree as ET


class Read_repo:

    tree = ET.parse('base.xml')
    root = tree.getroot()

    def read_flower(self):
        print("List of plants in the repository: ", '\n')
        for elm in self.root.findall("./flower"):
            print("- ", elm.attrib["name"])
        return

    def read_spec(self):

        l_flower = []
        for value in self.root.findall("./flower"):
            l_flower.append(value.attrib["name"])

        what_flower = input("Select the plant you want to see: ")

        if what_flower in l_flower:

            # anything other doesn't work! :(
            a = "./flower[@name='"
            c = "']/"
            path_flower = a+what_flower+c

            for elm in self.root.findall(path_flower):
                print(elm.tag, ": ", elm.text)
            return

        else:
            print("This plant is not in the base. Try again.")
