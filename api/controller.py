from .models import *
from django.http import HttpResponse
from django.conf import settings
import hashlib
import datetime
import json

def login(request):
  try:
    user = User.objects.get(login=request.POST['login'], password=request.POST['password'])
    secret = str(datetime.datetime.now().microsecond) + user.login
    user.token = hashlib.sha1(secret.encode('utf-8')).hexdigest()
    user.save()
    return HttpResponse(json.dumps(user.token))
  except:
    return HttpResponse(0)
