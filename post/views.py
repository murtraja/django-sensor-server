from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from ws4redis.publisher import RedisPublisher
from ws4redis.redis_store import RedisMessage

import json

# Create your views here.
@csrf_exempt
def postData(request):
    print 'inside postData'
    if request.method == 'POST':
        print 'inside post'
        name = request.POST['name']
        print name
        data = request.POST['data']
        print data
        mydict = {'name':name, 'data':data}
        print mydict
        redis_publisher = RedisPublisher(facility = 'sensor', broadcast = True)
        message = RedisMessage(json.dumps(mydict))
        redis_publisher.publish_message(message)
        return HttpResponse("OK")
    else:
        print 'get request'
        #return render(request,'post/postdata.html')
        return downloadAPK(request)

def monitorData(request):
    return render(request, 'post/monitor.html')

def downloadAPK(request):
    return HttpResponse("<a href = /static/Sensorization.apk>Download now!</a>")