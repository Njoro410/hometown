from django.contrib import admin
from .models import Business,Hospitals,Police,Posts,Tags
# Register your models here.

class PostsAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

admin.site.register(Business)
admin.site.register(Hospitals)
admin.site.register(Police)
admin.site.register(Posts, PostsAdmin)
admin.site.register(Tags)