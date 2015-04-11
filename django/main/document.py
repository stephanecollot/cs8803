import json
import logging
logger = logging.getLogger(__name__)

class Entity(object):
  def __init__(self, name, type):
    #logger.info('Entity' + str(string))
    self.name = name      # Entity value, String
    self.type = type      # Entity type from NLP, String
  
class Document(object):
  def __init__(self, content, id, fileName):
    #logger.info('Doc' + str(id))
    
    self.content = unicode(content, 'ISO-8859-1')
    self.id = id
    self.fileName = fileName
    #Debug
    self.entities = []
    self.entities.append(Entity('date','10/120/2014'))
    self.entities.append(Entity('name','Stephane'))
    self.entities.append(Entity('name','Jason'))
    
  def toJSON(self):
    return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    
class DocumentList:
  def __init__(self):
    logger.info('Doc List')
    self.docs = []
    
  def addDoc(self, content, fileName):
    doc = Document(content, len(self.docs), fileName)
    self.docs.append(doc)
    #logger.info('Doc List Add')
    
  def debug(self):
    logger.debug('Doc at 1:' + str(self.docs[1].id) + self.docs[1].fileName)
    for doc in self.docs:
      #logger.info('Doc Listing' + doc.content)
      pass
      
  def search(self, text):

    for doc in self.docs:
      if text in doc.content:
        logger.info('Doc id:' + str(doc.id) + ' contains: ' + text)
      
  def entityExtraction(self):
    logger.info('entityExtraction +')
    # Jason ;) you can start here, may be you can create a similar architecture of document.py but entity.py
    # and may be this function can output an EntityList, then stored in GlobalLoad (singleton accesible everywhere)
    for doc in self.docs:
      #logger.info('Doc Listing' + doc.content)
      pass
      
    logger.info('entityExtraction -')
