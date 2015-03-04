import logging
logger = logging.getLogger(__name__)

class GlobalLoad:
  ready = False

  def __init__(self):
    logger.info('GlobalLoad init ------------------------')
    self.ready = True
