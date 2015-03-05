
import logging
logger = logging.getLogger(__name__)

class Document:
  content = ""

  def __init__(self, content):
    logger.info('Doc')
    
    self.content = content

    
class DocumentList:
  docs = []

  def __init__(self):
    logger.info('Doc List')
    
  def addDoc(self, content):
    doc = Document(content)
    self.docs.append(doc)
    logger.info('Doc List Add')
    
  def debugDocs(self):
    for doc in self.docs:
      logger.info('Doc Listing' + doc.content)
