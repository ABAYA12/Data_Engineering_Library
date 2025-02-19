from django.contrib import admin
from .models import PipelineDetails

class PipelineDetailsAdmin(admin.ModelAdmin):
    list_display = ('title', 'purpose', 'database_type', 'cloud_provider', 'year')  # Columns in the admin list view
    list_filter = ('purpose', 'database_type', 'cloud_provider')  # Filters in the sidebar
    search_fields = ('title', 'purpose', 'database_type')  # Search functionality

admin.site.register(PipelineDetails, PipelineDetailsAdmin)
