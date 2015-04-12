from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.conf import settings

from document import Document
from document import DocumentList
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from serializers import DocumentSerializer
import json

import logging
logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
  logger.info('It works! global ready:' + str(settings.GLOBAL_LOAD.ready))
  return render_to_response('index.html')
  #return HttpResponse("Hello, world. Here is the index.")

"""
def search(request):
  print "Received search request"
  get_arg1 = request.GET.get('arg1', None)
  result = "{\"lol\": \"lolol\"}"
  response = HttpResponse(result, content_type='application/json')
  response.__setitem__("Access-Control-Allow-Origin", "*") #enables CORS (required to use json)
  return response
"""

def search(request, text):
  print "Received search request: " + text
  #result = "{\"lol\": \"" + text + "\"}"
  #result = '{"id":[147, 19, 28]}'
  result = settings.GLOBAL_LOAD.docList.search(text)
  result_json = json.dumps(result, default=lambda o: o.__dict__)
  response = HttpResponse(result_json, content_type='application/json')
  response.__setitem__("Access-Control-Allow-Origin", "*") #enables CORS (required to use json)
  return response

def openDocument(request, id):
  print "Opening document " + id
  doc = getHtml(settings.GLOBAL_LOAD.docList.docs[int(id)])
  response = HttpResponse(doc, content_type='text/html')
  response.__setitem__("Access-Control-Allow-Origin", "*") #enables CORS (required to use json)
  return response

def getHtml(document):
  entities = document.entities
  html = '<link rel="stylesheet" type="text/css" href="http://127.0.0.1:8000/s/entities.css">' + document.content
  html = html.replace("\n", "<br>")
  for e in entities:
    html = html.replace(e.name, '<span class="'+e.type +'">' + e.name + '</span>')
  return html


class DocumentViewSet(APIView):

  def get(self, request, *args, **kw):
    # Process any get params that you may need
    # If you don't need to process get params,
    # you can skip this part
    get_arg1 = request.GET.get('arg1', None)
    get_arg2 = request.GET.get('arg2', None)

    id = int(kw['id'])
    print "["+str(id)+"]"

    # Any URL parameters get passed in **kw
    doc = settings.GLOBAL_LOAD.docList.docs[id]
    print doc.fileName
    result = doc.toJSON()
    print result + "qsf"
    response = HttpResponse(result, content_type='application/json')
    response.__setitem__("Access-Control-Allow-Origin", "*")
    return response
    
class GraphViewSet(APIView):

  def get(self, request, *args, **kw):
    settings.GLOBAL_LOAD.computeGraph()
    nodes = settings.GLOBAL_LOAD.nodes
    links = settings.GLOBAL_LOAD.links

    result = '{ "nodes": '
    result += json.dumps([ob.__dict__ for ob in nodes])
    result += ', "links": '
    result += json.dumps([ob.__dict__ for ob in links])
    result += '} '
    #print result
    response = HttpResponse(result, content_type='application/json')
    return response
