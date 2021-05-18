from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
from models import HookModel

def hook(request):
    head=request.META
    body = request.body
    path =request.get_full_path()
    method= request.method
    HookModel.objects.create(head=head,body=body,path=path,method=method)
    return HttpResponse(json.dumps({'status':'success'}),content_type="application/json")