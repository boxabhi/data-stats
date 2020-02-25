from django.contrib import admin
from data_stats.models import Category, Content,Technology,Political,Business,extendeduser
# Register your models here.


admin.site.register(Category)
admin.site.register(Content)
admin.site.register(Technology)
admin.site.register(Political)
admin.site.register(Business)
admin.site.register(extendeduser)