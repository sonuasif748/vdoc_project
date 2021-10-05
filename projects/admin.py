from django.contrib import admin
from .models import *

# Register your models here.

class FilesAdd(admin.TabularInline):
    model = Project_Images
    extra = 0

class FilesAdd2(admin.TabularInline):
    model = Project_Files
    extra = 0


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': ['Author','co_author','title','abstract','project_keywords','mentor','start_date','completion_date','status','work_progress']}),
    ]
    inlines = [FilesAdd,FilesAdd2]
    list_display = ('title','status')
    list_filter = ['title']
    search_fields = ['title']
admin.site.register({Projects}, ProjectAdmin)

# admin.site.register(Project_Files)
# admin.site.register(Project_Images)
