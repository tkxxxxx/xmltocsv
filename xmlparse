# -*- coding utf-8 -*-
import xml.etree.ElementTree as ET
import re
import os
import glob

os.chdir(os.path.dirname(os.path.abspath(__file__)))

for name in glob.glob('ContourStInfo_????.xml'):
	tree = ET.parse(name)
	root = tree.getroot() 
	for child in root:
		if child.tag == "AirportInfo":
			ica_data = root[0][0].text
			print(ica_data)
