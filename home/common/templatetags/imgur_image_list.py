from django import template
from django.template.defaultfilters import timesince
import datetime
import re
register = template.Library()
import requests
import json

SIGNIN_URL = "http://imgur.com/signin"
API_ENDPOINT = "http://api.imgur.com" 
API_VERSION = "2"
API_ACCOUNT = "account"
API_FORMAT = "json"

IMGUR_IMAGE_LIST_TEMPLATE = 'modules/imgur_image_list/imgur_image_list.html'

@register.inclusion_tag(IMGUR_IMAGE_LIST_TEMPLATE)
def imgur_image_list(imgur_image_list):
    
    all = []
    images = dict()
    for ident in imgur_image_list.lists.all():
        key = ident.user
        if not images.get(key, None): images[key] = []
        l = get_images_for_ident(ident)
        images[key].extend(l)
        all.extend(l)
    
    # Sort by date
    all.sort(cmp=lambda x,y: cmp(x['image']['datetime'], y['image']['datetime']), reverse=True)
    
    return {'images': images, 'images_by_date': all }


def get_images_for_ident(ident):
    
    # Sign in with ident (mostly get the cookies)
    # TODO? use OAuth instead of cookies
    auth = dict(username=ident.username, password=ident.password, remember='remember', submit='')
    r = requests.post(SIGNIN_URL, data=auth)
    cookies = r.cookies
    
    r = requests.get(get_url_for_action('images'), cookies=cookies) 
    if r.status_code != 200:
        return []
    else:
        return json.loads(r.content).get('images', [])

def get_url_for_action(action):
    d = dict(endpoint=API_ENDPOINT, version=API_VERSION, account=API_ACCOUNT, action=action, format=API_FORMAT)
    return "%(endpoint)s/%(version)s/%(account)s/%(action)s.%(format)s" % d
    

