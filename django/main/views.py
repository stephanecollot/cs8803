from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.conf import settings

import logging
logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
  logger.info('It works! global ready:' + str(settings.GLOBAL_LOAD.ready))
  return render_to_response('index.html')
  #return HttpResponse("Hello, world. Here is the index.")