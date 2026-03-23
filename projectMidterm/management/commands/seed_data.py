from django.core.management.base import BaseCommand
from projectMidterm.models import Profile, Skill, Project, Education, SocialLink
from django.utils import timezone

class Command(BaseCommand):
    help = 'Seed initial data for portfolio'

    def handle(self, *args, **options):
        # Create Profile
        profile, created = Profile.objects.get_or_create(
            name='Tyron Lee T. Paira',
            defaults={
                'tagline': 'BSIT Student | Aspiring Developer | Tech Enthusiast',
                'short_intro': 'A passionate Bachelor of Science in Information Technology student aiming to develop skills in web development and technology solutions.',
                'about_text': 'I am Tyron Lee T. Paira, currently a third-year Bachelor of Science in Information Technology student at Negros Oriental State University. I have a strong interest in technology and continuously strive to improve my knowledge and skills in programming and system development. My goal is to become a successful IT professional and contribute to innovative projects in the future.',
                'email': 'pairatyronlee21@gmail.com',
            }
        )
        self.stdout.write(self.style.SUCCESS(f'Profile {"created" if created else "updated"}'))

        # Create Skills
        skills_data = [
            ('Python Programming', 'technical', 75, 1),
            ('Django Framework', 'technical', 65, 2),
            ('HTML/CSS', 'technical', 70, 3),
            ('JavaScript', 'technical', 60, 4),
            ('Database Management', 'technical', 65, 5),
            ('Problem Solving', 'professional', 80, 1),
            ('Team Collaboration', 'professional', 85, 2),
            ('Communication', 'professional', 75, 3),
            ('Time Management', 'professional', 80, 4),
            ('Adaptability', 'professional', 90, 5),
        ]
        
        for name, category, proficiency, order in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=name,
                defaults={
                    'category': category,
                    'proficiency': proficiency,
                    'order': order,
                }
            )
            self.stdout.write(f'Skill: {name} {"created" if created else "exists"}')

        # Create Projects
        projects_data = [
            {
                'title': 'Portfolio Website',
                'description': 'A personal portfolio website built with Django to showcase my skills and projects. Features include dynamic content management through admin panel, contact form with message storage, and responsive design.',
                'tools_technologies': 'Django, Python, HTML5, CSS3, Bootstrap, JavaScript',
                'github_link': 'https://github.com/tyronlee/portfolio',
                'completion_date': timezone.now(),
                'order': 1,
                'is_featured': True,
            },
            {
                'title': 'Task Management System',
                'description': 'A web-based task management application that allows users to create, update, and track tasks. Includes user authentication, task categories, and priority levels.',
                'tools_technologies': 'Django, SQLite, Bootstrap, JavaScript',
                'github_link': 'https://github.com/tyronlee/task-manager',
                'completion_date': timezone.now(),
                'order': 2,
                'is_featured': True,
            },
            {
                'title': 'Student Information System',
                'description': 'A comprehensive system for managing student records, grades, and attendance. Developed as a course project demonstrating database management and CRUD operations.',
                'tools_technologies': 'Python, Django, PostgreSQL, HTML, CSS',
                'github_link': 'https://github.com/tyronlee/student-system',
                'completion_date': timezone.now(),
                'order': 3,
                'is_featured': False,
            },
        ]
        
        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            self.stdout.write(f'Project: {project_data["title"]} {"created" if created else "exists"}')

        # Create Education
        education, created = Education.objects.get_or_create(
            school='Negros Oriental State University',
            defaults={
                'degree': 'Bachelor of Science in Information Technology',
                'year_start': 2022,
                'year_end': None,
                'is_current': True,
                'description': 'Third-year student focusing on software development, web technologies, and database management.',
                'order': 1,
            }
        )
        self.stdout.write(f'Education: {"created" if created else "exists"}')

        # Create Social Links
        social_links_data = [
            ('Facebook', 'https://www.facebook.com/tyronlee.paira', 'fab fa-facebook', 1),
            ('GitHub', 'https://github.com/tyronlee', 'fab fa-github', 2),
            ('LinkedIn', 'https://linkedin.com/in/tyronlee', 'fab fa-linkedin', 3),
        ]
        
        for platform, url, icon_class, order in social_links_data:
            link, created = SocialLink.objects.get_or_create(
                platform=platform,
                defaults={
                    'url': url,
                    'icon_class': icon_class,
                    'order': order,
                }
            )
            self.stdout.write(f'Social Link: {platform} {"created" if created else "exists"}')

        self.stdout.write(self.style.SUCCESS('Data seeding completed successfully!'))