from django.contrib import admin
from .models import Posts, Author, SocialMediaHandles

# Register your models here.
admin.site.register(Posts)
admin.site.register(Author)
admin.site.register(SocialMediaHandles)