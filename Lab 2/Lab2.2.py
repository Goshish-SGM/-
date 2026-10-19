import xml.dom.minidom as minidom

xml_file = open('currency.xml')
xml_data = xml_file.read()
dom = minidom.parseString(xml_data)
dom.normalize()

nodes = dom.getElementsByTagName('Valute')

currency_dict = {}

for node in nodes:
    name = None
    char_code = None
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName == 'Name':
                if child.firstChild.nodeType == 3:
                    name = child.firstChild.data
            if child.tagName == 'CharCode':
                if child.firstChild.nodeType == 3:
                    char_code = child.firstChild.data

    if name and char_code:
        currency_dict[name] = char_code

for key in currency_dict.keys():
    print(key, currency_dict[key])

xml_file.close()