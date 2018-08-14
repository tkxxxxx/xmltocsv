import csv
import xml.etree.cElementTree as ET
import os

file = r'C:\Users\take\Desktop\kriging\pykrige-master\pykrige-master/ContourStInfo_RJTT.xml'
tree =  ET.parse(file)
root = tree.getroot()

os.chdir(os.path.dirname(os.path.abspath(__file__)))
data_to_csv= open('output.csv','w')

list_head=[]

Csv_writer=csv.writer(data_to_csv,lineterminator='\n')

count=0
for elements in root.findall('StationInfo/Station'):
    List_node = []
    if count == 0 :

        LNG = elements.find('LNG').tag
        list_head.append(LNG)

        LAT = elements.find('LAT').tag
        list_head.append(LAT)

        Value = elements.find('Value').tag
        list_head.append(Value)

        Csv_writer.writerow(list_head)
        count = +1

    LNG= elements.find('LNG').text
    List_node.append(LNG)

    LAT = elements.find('LAT').text
    List_node.append(LAT)

    Value = elements.find('Value').text
    List_node.append(Value)

    Csv_writer.writerow(List_node)

data_to_csv.close()
