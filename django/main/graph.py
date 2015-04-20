import json
import logging
logger = logging.getLogger(__name__)

class Node(object):
  def __init__(self, name, type, id = 0, rank = 0, frequency = 0, counter = 1):
    #logger.info('Node' + str(string))
    self.name = name
    self.type = type
    self.id = id
    self.rank = rank
    self.frequency = frequency
    self.counter = 1
  
 
class Link(object):
  def __init__(self, source, target, weight = 1, docs = []):
    #logger.info('Link' + str(string))
    self.source = source
    self.target = target
    self.weight = weight
    self.docs = docs

