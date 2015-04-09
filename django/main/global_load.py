import glob
import os

from document import Document, DocumentList
from graph import Node, Link

import logging
logger = logging.getLogger(__name__)

class GlobalLoad:
  ready = False
  docList = DocumentList()
  nodes = []
  links = []

  def __init__(self):
    logger.info('GlobalLoad init ++++++++')
    
    #Document load, online once
    directory = "../stego_dataset/"
    owd = os.getcwd() # save current path
    #os.chdir(directory)
    for file in glob.glob(directory + "*.txt"):
      with open(directory+file, 'r') as content_file:
        self.docList.addDoc(content_file.read(), file)
    #self.docList.debug()
    os.chdir(owd) # come back to the path
    logger.info('GlobalLoad Nbr docs loaded: ' + str(len(self.docList.docs)))
        
    #Entity extraction
    self.docList.entityExtraction()
    
    #Search test
    #self.docList.search("test")
    
    #Compute graph
    self.computeGraph()
    
    logger.info('GlobalLoad init --------')
    self.ready = True
    
    
  def computeGraph(self):
    logger.info('getGraph')
    
    # First list all Entities
    allNodes = []
    for doc in self.docList.docs:
      for entity in doc.entities:
        allNodes.append(Node(entity.name, entity.type))
        
    # Get unique Nodes
    print "len1: " + str(len(allNodes))
    seen = set()
    uniqueNodes = []
    for node in allNodes:
        identifier = node.name + node.type
        if identifier not in seen:
            uniqueNodes.append(node)
            seen.add(identifier)
    print "uniqueNodes: " + str(len(uniqueNodes))
    
    # Set node's id
    for i in range(len(uniqueNodes)):
      uniqueNodes[i].id = i
      
    #Todo Update rank and frequency of Nodes ...
    
    #Create links
    links = []
    for doc in self.docList.docs:
      for i in range(len(doc.entities)):
        for j in range(i+1, len(doc.entities)):
          #links.append(Link(i,j)) # need a loop up table
          pass


    
    self.nodes = uniqueNodes
    self.links = links
    
