from django import template
from django.template.defaultfilters import timesince
import datetime
register = template.Library()


MESSAGE_LIST_TEMPLATE = 'modules/message_list/message_list.html'

@register.inclusion_tag(MESSAGE_LIST_TEMPLATE)
def message_list(message_list):
    
    messages = message_list.message_set.order_by('date')
    
    return {'message_list': message_list,
            'messages': messages }

@register.filter
def age(value):
    now = datetime.datetime.now()
    try:
        difference = now - value
    except:
        return value

    if difference <= datetime.timedelta(minutes=1):
        return 'just now'
    return '%(time)s ago' % {'time': timesince(value).split(', ')[0]}