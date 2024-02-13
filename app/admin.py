from django.contrib import admin
from .models import Category
from .models import Movie
from .models import *

admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(Video)
