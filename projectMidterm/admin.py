from django.contrib import admin
from .models import Profile, Skill, Project, Education, SocialLink, ContactMessage

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'tagline', 'short_intro', 'profile_photo', 'email')
        }),
        ('About Section', {
            'fields': ('about_text',)
        }),
    )

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'order']
    list_filter = ['category']
    list_editable = ['proficiency', 'order']
    search_fields = ['name']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'completion_date', 'is_featured', 'order']
    list_filter = ['is_featured', 'completion_date']
    list_editable = ['is_featured', 'order']
    search_fields = ['title', 'description']
    readonly_fields = ['get_technologies_list_display']
    
    def get_technologies_list_display(self, obj):
        return ', '.join(obj.get_technologies_list())
    get_technologies_list_display.short_description = 'Technologies'

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'school', 'year_start', 'year_end', 'is_current', 'order']
    list_filter = ['is_current']
    list_editable = ['order']

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ['platform', 'url', 'order']
    list_editable = ['order']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    list_editable = ['is_read']
    search_fields = ['name', 'email', 'subject']
    readonly_fields = ['created_at']