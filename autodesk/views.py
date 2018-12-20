from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import json
import requests


def viewer(request):
	context = {}
	template = loader.get_template('autodesk/index.html')
	return HttpResponse(template.render(context, request))


# to get the access tokens with received scope for autodesk viewers
def generate_token(request):
    try:
        base_url = 'https://developer.api.autodesk.com'
        url_authenticate = base_url + '/authentication/v1/authenticate'
        data = {
            'client_id': 'W8DWpGrj5W3LHRFJsh2iMEUV1Sjb32zj',
            'client_secret': 'mZKwI5w2YNo4QLHY',
            'grant_type': 'client_credentials',
            'scope': 'viewables:read'
        }
        r = requests.post(url_authenticate, data=data)
    except Exception as e:
        return json.dumps({'status':0, 'error':e.__str__()})
    return HttpResponse(json.dumps({'status':1, 'r':r.content.decode('utf-8')}))




    

# dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWwyMDE4LTEyLTE5LTA5LTUyLTQyLWQ0MWQ4Y2Q5OGYwMGIyMDRlOTgwMDk5OGVjZjg0MjdlL3JhY19hZHZhbmNlZF9zYW1wbGVfcHJvamVjdC5ydnQ

# dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWwyMDE4LTEyLTE5LTA5LTUyLTU1LWQ0MWQ4Y2Q5OGYwMGIyMDRlOTgwMDk5OGVjZjg0MjdlL3JhY19iYXNpY19zYW1wbGVfcHJvamVjdC5ydnQ

# dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bW9kZWwyMDE4LTEyLTE5LTA5LTUyLTA3LWQ0MWQ4Y2Q5OGYwMGIyMDRlOTgwMDk5OGVjZjg0MjdlL0dhdGVIb3VzZS5ud2Q
