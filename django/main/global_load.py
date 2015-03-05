import glob
import os

from document import Document, DocumentList

import logging
logger = logging.getLogger(__name__)

class GlobalLoad:
  ready = False
  docList = DocumentList()

  def __init__(self):
    logger.info('GlobalLoad init ++++++++')
         
    directory = "../stego_dataset/"
    os.chdir(directory)
    for file in glob.glob("*.txt"):
      with open(directory+file, 'r') as content_file:
        self.docList.addDoc(content_file.read(), file)
    
    self.docList.debugDocs()
    logger.info('GlobalLoad init --------')
    self.ready = True
