from django.contrib import admin
from .models import Comment, Business, Post,Neighbourhood, Profile


# Register your models here.
admin.site.register(Comment)
admin.site.register(Business)
admin.site.register(Post)
admin.site.register(Neighbourhood)
admin.site.register(Profile)