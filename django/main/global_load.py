import glob
import os
import math
import numpy as np
from textblob import TextBlob as tb
from document import Document, DocumentList, Entity
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
    entitydoc = open("main/some.txt")
    print "file open"
    for i in range(1,7798):
      x = entitydoc.readline().split("|") #each iteration of the loop return a key value pair of doc name and entites in the document
      for doc in self.docList.docs:
        #print x[0]
        #print doc.fileName
        if x[0] in doc.fileName:
          #print "inside condition"
          print i
          doc.entities.append(Entity(x[1],x[2]))
    print "done"

    #tf-idf
    def tf(word,blob):
      d = blob.lower()
      return float(d.count(word.lower()))/float(len(d))

    def n_containing(word, bloblist):
        return sum(1 for blob in bloblist if word.lower() in blob.content.lower())

    def idf(word, bloblist):
        return float(math.log(float(len(bloblist))/ float(1 + n_containing(word, bloblist))))

    def tfidfunc(word, blob, bloblist):
      try:
        return float(tf(word, blob) * idf(word, bloblist))
      except:
        return 0
      #for item in self.docList.docs.entities:
    
    x = []

    for i in self.docList.docs:
      for j in i.entities:
        j.tfidf = tfidfunc(j.name,i.content,self.docList.docs)
      #  print j.name, j.tfidf
        x.append(j.tfidf)

    y = np.array(x)

    print "25 percentile"
    print np.percentile(y,25)

    print "50 percentile"
    print np.percentile(y,50)

    print "75 percentile"
    foobar90 = np.percentile(y,75)
    print foobar90

    ct = 0
    for i in self.docList.docs:
      for j in i.entities:
        if j.tfidf>=foobar90:
          ct = ct+1

    print "Total count of entities >90th percentile" + str(ct)
















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
				n = Node(entity.name, entity.type)
				n.frequency = entity.tfidf
        n.rank = entity.rank
        allNodes.append(n)
				
    # Take only the best nodes based on tfidf == frequency
		allNodes = sorted(allNodes, key=lambda n: n.frequency, reverse=True) # Sort
		allNodes = allNodes[:(len(allNodes)*0.10)] # Take 10%
				
    # Get unique Nodes
    print "allNodes len: " + str(len(allNodes))
    seen = set()
    uniqueNodes = []
    nodeLookUp = {}
    for node in allNodes:
        identifier = node.name + node.type
        if identifier not in seen:
            uniqueNodes.append(node)
            nodeLookUp[identifier] = len(uniqueNodes)-1
            seen.add(identifier)
    print "uniqueNodes len: " + str(len(uniqueNodes))
    
    # Set node's id
    for i in range(len(uniqueNodes)):
      uniqueNodes[i].id = i # TODO can be optimized and node just before in 'uniqueNodes.append(node)'
      
    #Todo Update rank and frequency of Nodes ...
    
    #Create links with Weight
    linksDict = {}
    for doc in self.docList.docs:
      for i in range(len(doc.entities)):
        id1 = doc.entities[i].name + doc.entities[i].type
				if not id1 in nodeLookUp: # Entity not selected
					continue
        for j in range(i+1, len(doc.entities)):
          id2 = doc.entities[j].name + doc.entities[j].type
					if not id2 in nodeLookUp: # Entity not selected
						continue
          if nodeLookUp[id1] < nodeLookUp[id2]:
            if (nodeLookUp[id1],nodeLookUp[id2]) in linksDict:
              linksDict[(nodeLookUp[id1],nodeLookUp[id2])] += 1
            else:
              linksDict[(nodeLookUp[id1],nodeLookUp[id2])] = 1
          else:
            if (nodeLookUp[id2],nodeLookUp[id1]) in linksDict:
              linksDict[(nodeLookUp[id2],nodeLookUp[id1])] += 1
            else:
              linksDict[(nodeLookUp[id2],nodeLookUp[id1])] = 1
          pass

    print "linksDict len: " + str(len(linksDict))
    
    links = []
    for k, v in linksDict.viewitems():
      links.append(Link(k[0],k[1],v))
    
    print "links len: " + str(len(links))
    
    self.nodes = uniqueNodes
    self.links = links
    
