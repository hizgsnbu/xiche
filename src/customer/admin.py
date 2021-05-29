from django.contrib import admin
from models import HookModel,CarWashLocalModel,UserCarModel,WashSessionModel

# Register your models here.
admin.site.register(HookModel)
admin.site.register(CarWashLocalModel)
admin.site.register(UserCarModel)
admin.site.register(WashSessionModel)