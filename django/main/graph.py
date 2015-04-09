import json
import logging
logger = logging.getLogger(__name__)

class Node(object):
  def __init__(self, id, name, rank, frequency, type):
    #logger.info('Node' + str(string))
    self.id = id
    self.name = name
    self.rank = rank
    self.frequency = frequency
    self.type = type
  
class Link(object):
  def __init__(self, source, target, weight):
    #logger.info('Link' + str(string))
    self.source = source
    self.target = target
    self.weight = weight

