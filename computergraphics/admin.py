from django.contrib import admin
from .models import Post, Note, Mcq, Link
# Register your models here.

admin.site.register(Post)
admin.site.register(Note)
admin.site.register(Mcq)
admin.site.register(Link)