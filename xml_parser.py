#!/bin/python
import xml.etree.ElementTree as ET
import sys

tree = ET.parse(sys.argv[1])
root = tree.getroot()
#print root.find('deckname').text
#main = root.find('./zone')
#for c in main.findall(path='card'):
#    print c.get('number')+c.get('name') 
for c in root[2]:
    print c.get('number') +' '+ c.get('name')

for c in root[3]:
    print 'SB: '+c.get('number') +' '+ c.get('name')
