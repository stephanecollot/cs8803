import glob
import os
import math
import numpy as np
import ntpath
from textblob import TextBlob as tb
from document import Document, DocumentList, Entity
from graph import Node, Link
from pageRank import pageRank

import logging
logger = logging.getLogger(__name__)




class GlobalLoad:
  ready = False
  docList = DocumentList()
  nodes = []
  links = []
  types = []

  def __init__(self):
    logger.info('GlobalLoad init ++++++++')
    
    #Document load, online once
    directory = "../stego_dataset/"
    for file in glob.glob(directory + "*.txt"):
      with open(directory+file, 'r') as content_file:
        self.docList.addDoc(content_file.read(), ntpath.basename(file))
    #self.docList.debug()
    logger.info('GlobalLoad Nbr docs loaded: ' + str(len(self.docList.docs)))
        
    #Entity extraction
    entitydoc = "main/some.txt"
    with open(entitydoc) as f:
      for line in f:
        lineSplit = line.split("|") #each iteration of the loop return a key value pair of doc name and entites in the document
        if len(lineSplit) == 3:
          for doc in self.docList.docs:
            if lineSplit[0] in doc.fileName:
              name = lineSplit[1]
              type = lineSplit[2].capitalize()
              ent = Entity(name, type)
              doc.entities.append( ent )
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
    
    # First list all Entities and convert them into Nodes
    allNodes = []
    for doc in self.docList.docs:
      for entity in doc.entities:
        n = Node(entity.name, entity.type)
        n.frequency = entity.tfidf
        allNodes.append(n)
        
        if not entity.type in self.types:
          self.types.append(entity.type)
				
    # Merge same Nodes together and aggregate the TFIDF
    print "allNodes len: " + str(len(allNodes))
    nodesDict = {}
    for node in allNodes:
        key = node.name + node.type
        if key not in nodesDict:
          nodesDict[key] = node
        else: #Aggregate
          nodesDict[key].counter += 1
          nodesDict[key].frequency += node.frequency
    print "Nbr of unique Nodes: " + str(len(nodesDict))
    
    #Compute the average TFIDF
    frequencies = []
    counters = []
    for key, node in nodesDict.iteritems():
      node.frequency = int(100000*(node.frequency/node.counter))
      nodesDict[key] = node
      frequencies.append(node.frequency)
      counters.append(node.counter)

    # Take only the best nodes
    frequencies.sort() # sorted by ascending order
    counters.sort() # sorted by ascending order
    numberOfNode = 40
    print "len nodesDict " + str(len(nodesDict))
    print "min freq" + str(frequencies[-numberOfNode])
    print "min counter" + str(counters[-numberOfNode])
    for key, node in nodesDict.items():
      #if node.frequency < frequencies[-numberOfNode]:
        #del nodesDict[key]
      if node.counter < counters[-numberOfNode]:
        del nodesDict[key]
    print "len nodesDict filtered" + str(len(nodesDict))
    
    # Set node's id
    i = 0
    for key, node in nodesDict.iteritems():
      nodesDict[key].id = i # TODO can be optimized and node just before in 'uniqueNodes.append(node)'
      i += 1
      
    #Todo Update rank and frequency of Nodes ...
    
    #Create links with Weight
    linksDict = {}
    for doc in self.docList.docs:
      for i in range(len(doc.entities)):
        key1 = doc.entities[i].name + doc.entities[i].type
        if not key1 in nodesDict: # Entity not selected
          continue
        for j in range(i+1, len(doc.entities)):
          key2 = doc.entities[j].name + doc.entities[j].type
          if not key2 in nodesDict: # Entity not selected
            continue
          if nodesDict[key1] < nodesDict[key2]:
            if (nodesDict[key1].id,nodesDict[key2].id) in linksDict:
              linksDict[(nodesDict[key1].id,nodesDict[key2].id)] += 1
            else:
              linksDict[(nodesDict[key1].id,nodesDict[key2].id)] = 1
          else:
            if (nodesDict[key2],nodesDict[key1]) in linksDict:
              linksDict[(nodesDict[key2].id,nodesDict[key1].id)] += 1
            else:
              linksDict[(nodesDict[key2].id,nodesDict[key1].id)] = 1
          pass

    print "linksDict len: " + str(len(linksDict))
        
    adjacency = np.zeros((len(nodesDict), len(nodesDict)))# Adjacency matrix
    links = []
    for k, v in linksDict.viewitems():
      if not k[0] == k[1]:
        links.append(Link(k[0],k[1],v))
        adjacency[k[0]][k[1]] = v
        adjacency[k[1]][k[0]] = v
    
    print "links len: " + str(len(links))
 
    print adjacency
    print " "
    pr = pageRank(adjacency, .85, .000001)
    print pr
    
    for key, node in nodesDict.iteritems():
      nodesDict[key].rank = pr[nodesDict[key].id]    
    
    self.nodes = nodesDict.values()
    self.links = links
    
