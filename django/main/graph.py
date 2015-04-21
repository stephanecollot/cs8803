import json
from django.conf import settings
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
    self.docs = self.getHtmlLinks(docs)

  def getHtmlLinks(self, docs):
    html = ""
    for docId in docs:
      doc = settings.GLOBAL_LOAD.docList.docs[int(docId)]
      html += '<a href="#" onClick="openDocument('+str(doc.id)+'); hideMenu(); return false;">' + doc.fileName + '</a><br>'
    return html
