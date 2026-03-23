from django.db import models
from django.utils import timezone

class Profile(models.Model):
    """Model for profile information"""
    name = models.CharField(max_length=100, default='Tyron Lee T. Paira')
    tagline = models.CharField(max_length=200, default='BSIT Student | Aspiring Developer')
    short_intro = models.TextField(default='A passionate Bachelor of Science in Information Technology student aiming to develop skills in web development and technology solutions.')
    about_text = models.TextField(default='I am Tyron Lee T. Paira, currently a third-year Bachelor of Science in Information Technology student at Negros Oriental State University. I have a strong interest in technology and continuously strive to improve my knowledge and skills in programming and system development. My goal is to become a successful IT professional and contribute to innovative projects in the future.')
    profile_photo = models.ImageField(upload_to='profile/', blank=True, null=True)
    email = models.EmailField(default='pairatyronlee21@gmail.com')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Profile'

class Skill(models.Model):
    """Model for skills"""
    SKILL_CATEGORIES = [
        ('technical', 'Technical Skills'),
        ('professional', 'Professional Skills'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=SKILL_CATEGORIES, default='technical')
    proficiency = models.IntegerField(help_text='Proficiency level (1-100)', default=50)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['order', 'name']

class Project(models.Model):
    """Model for projects"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    tools_technologies = models.CharField(max_length=500, help_text='Comma-separated list of tools/technologies used')
    github_link = models.URLField(blank=True, null=True)
    live_demo_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    completion_date = models.DateField(default=timezone.now)
    order = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    def get_technologies_list(self):
        return [tech.strip() for tech in self.tools_technologies.split(',')]
    
    class Meta:
        ordering = ['order', '-completion_date']

class Education(models.Model):
    """Model for education"""
    school = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    year_start = models.IntegerField()
    year_end = models.IntegerField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.degree} at {self.school}"
    
    class Meta:
        ordering = ['order', '-year_start']
        verbose_name_plural = 'Education'

class SocialLink(models.Model):
    """Model for social media links"""
    platform = models.CharField(max_length=50)
    url = models.URLField()
    icon_class = models.CharField(max_length=50, help_text='Font Awesome icon class', default='fab fa-github')
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.platform
    
    class Meta:
        ordering = ['order']

class ContactMessage(models.Model):
    """Model for contact form submissions"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
    
    class Meta:
        ordering = ['-created_at']