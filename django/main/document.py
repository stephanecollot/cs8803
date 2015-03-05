
import logging
logger = logging.getLogger(__name__)

class Document:
  content = ""
  id = 0
  fileName = ""

  def __init__(self, content, id, fileName):
    #logger.info('Doc' + str(id))
    
    self.content = content
    self.id = id
    self.fileName = fileName

    
class DocumentList:
  docs = []

  def __init__(self):
    logger.info('Doc List')
    
  def addDoc(self, content, fileName):
    doc = Document(content, len(self.docs), fileName)
    self.docs.append(doc)
    #logger.info('Doc List Add')
    
  def debugDocs(self):
    logger.debug('Doc at 1:' + str(self.docs[1].id) + self.docs[1].fileName)
    for doc in self.docs:
      #logger.info('Doc Listing' + doc.content)
      pass
