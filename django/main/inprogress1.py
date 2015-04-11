import os
from aylienapiclient import textapi
import time
import json


files = os.listdir("Dataset")
os.chdir(str(os.getcwd())+'/Dataset')

c = textapi.Client("17efde2e", "24e1f4e37448224db5358a7a2acec493")
dataset = {}

for file in files:
	dataset[file] = open(file).read()
# all files and contents are now in dataset dictionary

enti = {}
files = open("haxxor","w")
for keys in dataset:
	#files.write(str(c.Entities({'text': dataset[keys]})))
	time.sleep(2) 
	ask = c.Entities({'text': dataset[keys]})
	#enti[keys] = json.loads(ask)
	files.write(str(ask['entities']))
	files.write("\n")



print len(enti)	