import xml.dom.minidom
from bs4 import BeautifulSoup

class Add_del_repo():

    domtree = xml.dom.minidom.parse('base.xml')
    group = domtree.documentElement
    flowers = group.getElementsByTagName('flowers')

    def add_flower(self):

        new_name = input("Enter the name of the new plant: ")
        new_species = input("What species is the new plant?: ")
        new_type = input("Enter the type of new plant (indoor, outdoor): ")
        new_position = input("Describe the optimal position for the new plant (sunny / shade / partial shade): ")
        new_humidity = input("What is the optimal air humidity for a new plant? (High / low): ")
        new_fertilize = input("How often should I fertilize new plant?: ")
        new_temperature = input("What is the optimal temperature for this plant to live? (in Celsius): ")

        new_flower = self.domtree.createElement('flower')
        new_flower.setAttribute('name', new_name)

        new_namee = self.domtree.createElement('name')
        new_namee.appendChild(self.domtree.createTextNode(new_name))

        new_speciess = self.domtree.createElement('species')
        new_speciess.appendChild(self.domtree.createTextNode(new_species))

        new_typee = self.domtree.createElement('type')
        new_typee.appendChild(self.domtree.createTextNode(new_type))

        new_positionn = self.domtree.createElement('position')
        new_positionn.appendChild(self.domtree.createTextNode(new_position))

        new_humidityy = self.domtree.createElement('humidity')
        new_humidityy.appendChild(self.domtree.createTextNode(new_humidity))

        new_fertilizee = self.domtree.createElement('fertilize')
        new_fertilizee.appendChild(self.domtree.createTextNode(new_fertilize))

        new_temperaturee = self.domtree.createElement('temperature')
        new_temperaturee.appendChild(self.domtree.createTextNode(new_temperature))

        new_flower.appendChild(new_namee)
        new_flower.appendChild(new_speciess)
        new_flower.appendChild(new_typee)
        new_flower.appendChild(new_positionn)
        new_flower.appendChild(new_humidityy)
        new_flower.appendChild(new_fertilizee)
        new_flower.appendChild(new_temperaturee)

        self.group.appendChild(new_flower)
        self.domtree.writexml(open('base.xml', 'w'))

        bs = BeautifulSoup(open('base.xml'), 'xml')
        pretty_xml = bs.prettify()

        saving = open('base.xml', "w", encoding="utf-8")
        saving.write(pretty_xml)
        saving.close()

        print("The process has been completed successfully.")

