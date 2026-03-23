from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Skill, Project, Education, SocialLink
from .forms import ContactForm

def home(request):
    """Home page view"""
    profile = Profile.objects.first()
    featured_projects = Project.objects.filter(is_featured=True)[:3]
    
    context = {
        'profile': profile,
        'featured_projects': featured_projects,
        'active_page': 'home',
    }
    return render(request, 'projectMidterm/home.html', context)

def about(request):
    """About page view"""
    profile = Profile.objects.first()
    
    context = {
        'profile': profile,
        'active_page': 'about',
    }
    return render(request, 'projectMidterm/about.html', context)

def skills(request):
    """Skills page view"""
    technical_skills = Skill.objects.filter(category='technical')
    professional_skills = Skill.objects.filter(category='professional')
    
    context = {
        'technical_skills': technical_skills,
        'professional_skills': professional_skills,
        'active_page': 'skills',
    }
    return render(request, 'projectMidterm/skills.html', context)

def projects(request):
    """Projects page view"""
    all_projects = Project.objects.all()
    
    context = {
        'projects': all_projects,
        'active_page': 'projects',
    }
    return render(request, 'projectMidterm/projects.html', context)

def education(request):
    """Education page view"""
    education_list = Education.objects.all()
    
    context = {
        'education_list': education_list,
        'active_page': 'education',
    }
    return render(request, 'projectMidterm/education.html', context)

def contact(request):
    """Contact page view"""
    profile = Profile.objects.first()
    social_links = SocialLink.objects.all()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully! I will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    context = {
        'profile': profile,
        'social_links': social_links,
        'form': form,
        'active_page': 'contact',
    }
    return render(request, 'projectMidterm/contact.html', context)