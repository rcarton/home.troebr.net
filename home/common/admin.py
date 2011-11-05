from django.contrib import admin
from home.common.models import Countdown, Place, MessageList, Message

admin.site.register(Place)
admin.site.register(Countdown)
admin.site.register(MessageList)
admin.site.register(Message)

