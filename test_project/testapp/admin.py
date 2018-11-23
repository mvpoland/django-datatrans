from django.contrib import admin
from test_project.testapp.models import Option


class OptionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Option, OptionAdmin)
