from django.contrib import admin
from .models import Post, Note, Mcq, Link, DsPostComment
# Register your models here.

admin.site.register((Post, Note, Mcq, Link, DsPostComment))