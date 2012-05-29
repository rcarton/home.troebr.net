from common.templatetags import message_list as mltag
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed, HttpResponseForbidden, \
    HttpResponse
from django.shortcuts import render_to_response
from django.template import Template, loader
from django.template.context import Context, RequestContext
from home.common.models import MessageList, Message, Place
from home.common.templatetags.imgur_image_list import imgur_image_list_ajax



@login_required
def add_message(request):
    """Adds a new message and renders the message list."""
    
    if request.method != 'POST':
        raise HttpResponseNotAllowed(('POST',))
    
    message_list = MessageList.objects.get(name=str(request.POST.get('message_list')))
    
    if request.user not in message_list.place.users.all():
        raise HttpResponseForbidden()
    
    message = Message()
    
    message.value = mltag.auto_markdown(request.POST.get('value'))
    message.poster = request.user
    message.messagelist = message_list
    message.save()
    
    t = loader.get_template(mltag.MESSAGE_LIST_TEMPLATE)
    
    return HttpResponse(content=t.render(Context(mltag.message_list(message_list))), content_type='text/html')

@login_required
def image_list(request):
    """Adds a new message and renders the message list."""
    if request.GET.get('place'):
        place = Place.objects.get(name=request.GET.get('place'))
    else:
        place = Place.objects.all()[0]
    
    #Only registered users
    if request.user not in place.users.all():
        return HttpResponseForbidden()
    
    context = imgur_image_list_ajax(place.imgurimagelist)
    
    return render_to_response('modules/imgur_image_list/imgur_image_list_ajax.html', RequestContext(request, context))

