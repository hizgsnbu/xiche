from django.shortcuts import render
from django.http import HttpResponse
import json
from django.contrib.auth.models import User
# Create your views here.
from models import HookModel,UserCarModel,WashSessionModel,CarWashLocalModel
import qrcode
from io import BytesIO
from django.conf import settings
from django.utils import timezone
from ex import get_or_none


def hook(request):
    head=request.META
    body = request.body
    path =request.get_full_path()
    method= request.method
    HookModel.objects.create(head=head,body=body,path=path,method=method)
    return HttpResponse(json.dumps({'status':'success'}),content_type="application/json")

def new_session(request):
    chepai=request.GET.get('chepai')
    customer_id=request.GET.get('customer')
    local_id=request.GET.get('local')
    customer=None
    if chepai:
        customer=get_or_none(User,usercarmodel__car_no=chepai)
    if customer_id:
        customer=get_or_none(User, pk=customer_id)
        
    local = CarWashLocalModel.objects.get(no=local_id)
    if customer:
        session=WashSessionModel.objects.create(user=customer,local=local)
        return HttpResponse(json.dumps({'session':session.pk}),content_type="application/json")
    else:
        return HttpResponse(json.dumps({'session':None}),content_type="application/json")

def qr(request):
    customer_id=request.GET.get('customer')
    local_no=request.GET.get('local')
    img = qrcode.make('{domain}/zk/new_wash_session/?customer_id={customer_id}&local={local}'\
                      .format(domain=settings.DOMAIN,customer_id=customer_id,local=local_no))
    byt=BytesIO()
    img.save(byt,'png')
    return HttpResponse(byt.getvalue(),content_type="image/png")

def start(request):
    session_id=request.GET.get('session')
    try:
        session = WashSessionModel.objects.get(pk=session_id)
        session.start=timezone.now()
        session.save()
        return HttpResponse(json.dumps({'status':'success'}),content_type="application/json")
    except WashSessionModel.DoesNotExist:
        return HttpResponse(json.dumps({'error':'session not exist'}),content_type="application/json")

def end(request):
    session_id=request.GET.get('session')
    try:
        session = WashSessionModel.objects.get(pk=session_id)
        session.end=timezone.now()
        session.save()
        return HttpResponse(json.dumps({'status':'success'}),content_type="application/json")
    except WashSessionModel.DoesNotExist:
        return HttpResponse(json.dumps({'error':'session not exist'}),content_type="application/json")



def get_code(request):
    "通过短信发验证码"
    mobile= request.GET.get('mobile')
    send_type = request.GET.get('type','1')
    if mobile:
        # Todo 通过短信发验证码
        # fake code =1111
        pass
    dc ={
        'ret':1,
    }
    return HttpResponse(json.dumps(dc),content_type="application/json")
   
def valide_sms(request):
    mobile=request.GET.get('mobile')
    vcode=request.GET.get('vcode')
    send_type=int(request.GET.get('type',1))
    dc={}
    if mobile and vcode:
        dc['ret']= 1  # 1好像是代表成功
    return HttpResponse(json.dumps(dc),content_type="application/json")

def user_login(request):
    
