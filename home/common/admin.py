from django.contrib import admin
from home.common.models import Countdown, Place, MessageList, Message, \
    ImgurImageList, ImgurIdent

admin.site.register(Place)
admin.site.register(Countdown)
admin.site.register(MessageList)
admin.site.register(Message)
admin.site.register(ImgurImageList)
admin.site.register(ImgurIdent)

