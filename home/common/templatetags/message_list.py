from django import template
from django.template.defaultfilters import timesince
import datetime
import re
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


def auto_markdown(s):
    """Converts urls to markdown."""
    
    url_pattern = re.compile(r'(http://[^\s]+)')
        
    def replace(s):
        res = s
        if re.match(url_pattern, s):
            # images
            image_types = ('gif', 'jpg', 'jpeg', 'png')
            if any(map(lambda x: s.lower().endswith(x), image_types)):
                res = ''.join(('[![img](', s, ')](', s,')'))
            # regular links
            else:
                res = ''.join(('[', s,'](', s, ')'))
        return res

    return ''.join([replace(token) for token in re.split(url_pattern, s)])
    
    