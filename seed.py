import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nextstep.settings')
django.setup()

from django.contrib.auth.models import User
from accounts.models import Profile
from roadmaps.models import Roadmap, Topic, Resource
from articles.models import Article
from internships.models import Internship
from communities.models import Community

# Create superuser
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@nextstep.edu', 'admin123')
    print('Superuser created: admin / admin123')

# Create sample user
user, _ = User.objects.get_or_create(username='demo', defaults={'email': 'demo@nextstep.edu'})
user.set_password('demo123')
user.save()
Profile.objects.get_or_create(user=user, defaults={'career_goal': 'Data Scientist', 'budget_mode': 'mixed', 'learning_style': 'video'})
print('Demo user created: demo / demo123')

# Get admin user for created_by
admin_user = User.objects.filter(username='admin').first() or user

# Sample Roadmap: Data Scientist
ds, _ = Roadmap.objects.update_or_create(
    title='Data Scientist',
    defaults={'description': 'Master data science from fundamentals to advanced ML.', 'career_role': 'Data Scientist', 'created_by': admin_user, 'difficulty': 'intermediate', 'estimated_duration': '6 Months'}
)


topics_ds = [
    ('Python Basics', 'Learn Python programming fundamentals.', 1),
    ('Linear Algebra', 'Vectors, matrices, and linear transformations.', 2),
    ('NumPy & Pandas', 'Data manipulation with Python libraries.', 3),
    ('Data Visualization', 'Matplotlib, Seaborn, and Plotly.', 4),
    ('Machine Learning', 'Supervised and unsupervised learning algorithms.', 5),
]

for title, desc, order in topics_ds:
    t, _ = Topic.objects.get_or_create(roadmap=ds, title=title, defaults={'description': desc, 'order': order, 'estimated_time': '2 Weeks'})
    Resource.objects.get_or_create(topic=t, title=f'Free: {title} Guide', defaults={'url': 'https://www.youtube.com/results?search_query=' + title.replace(' ', '+'), 'resource_type': 'free'})
    Resource.objects.get_or_create(topic=t, title=f'Free: {title} Kaggle Notebook', defaults={'url': 'https://www.kaggle.com/', 'resource_type': 'free'})
    Resource.objects.get_or_create(topic=t, title=f'Paid: Coursera {title}', defaults={'url': 'https://www.coursera.org/', 'resource_type': 'paid'})
    Resource.objects.get_or_create(topic=t, title=f'Paid: Udemy {title}', defaults={'url': 'https://www.udemy.com/', 'resource_type': 'paid'})

# Sample Roadmap: Full Stack Developer
fs, _ = Roadmap.objects.update_or_create(
    title='Full Stack Developer',
    defaults={'description': 'Build modern web applications from front to back.', 'career_role': 'Full Stack Developer', 'created_by': admin_user, 'difficulty': 'beginner', 'estimated_duration': '4 Months'}
)


topics_fs = [
    ('HTML & CSS', 'Web page structure and styling.', 1),
    ('JavaScript', 'Dynamic client-side programming.', 2),
    ('React.js', 'Modern frontend framework.', 3),
    ('Node.js & Express', 'Backend API development.', 4),
    ('Django & Databases', 'Full-stack Python framework.', 5),
]

for title, desc, order in topics_fs:
    t, _ = Topic.objects.get_or_create(roadmap=fs, title=title, defaults={'description': desc, 'order': order, 'estimated_time': '2 Weeks'})
    Resource.objects.get_or_create(topic=t, title=f'Free: MDN {title}', defaults={'url': 'https://developer.mozilla.org/', 'resource_type': 'free'})
    Resource.objects.get_or_create(topic=t, title=f'Free: freeCodeCamp {title}', defaults={'url': 'https://www.freecodecamp.org/', 'resource_type': 'free'})
    Resource.objects.get_or_create(topic=t, title=f'Paid: Udemy {title}', defaults={'url': 'https://www.udemy.com/', 'resource_type': 'paid'})
    Resource.objects.get_or_create(topic=t, title=f'Paid: Frontend Masters {title}', defaults={'url': 'https://frontendmasters.com/', 'resource_type': 'paid'})

# Sample Articles
Article.objects.get_or_create(title='How to Avoid Analysis Paralysis', defaults={'content': 'Analysis paralysis is a common problem for self-taught developers. This article explains how to overcome it.', 'author': user})
Article.objects.get_or_create(title='Top Free Resources for Self-Taught Developers', defaults={'content': 'Here are the best free resources available online for learning programming and data science.', 'author': user})
Article.objects.get_or_create(title='Building a Study Routine That Works', defaults={'content': 'Consistency is key to mastering technical skills. Learn how to build an effective study routine.', 'author': user})

# Sample Internships
Internship.objects.get_or_create(title='Data Science Intern at TechCorp', defaults={'company': 'TechCorp', 'description': 'Work on real-world ML models and data pipelines.', 'location': 'Remote', 'is_remote': True, 'posted_by': user})
Internship.objects.get_or_create(title='Frontend Developer Intern', defaults={'company': 'WebStart', 'description': 'Build React components for SaaS platform.', 'location': 'Remote', 'is_remote': True, 'posted_by': user})
Internship.objects.get_or_create(title='Backend Developer Intern', defaults={'company': 'CloudScale', 'description': 'Develop REST APIs with Django and PostgreSQL.', 'location': 'San Francisco, CA', 'is_remote': False, 'posted_by': user})

# Sample Communities
Community.objects.get_or_create(name='Data Science Study Group', defaults={'description': 'Collaborative learning for aspiring data scientists.', 'created_by': user})
Community.objects.get_or_create(name='Full Stack Builders', defaults={'description': 'Building projects together from zero to deployment.', 'created_by': user})
Community.objects.get_or_create(name='Python Enthusiasts', defaults={'description': 'For Python lovers of all levels.', 'created_by': user})

print('Sample data seeded successfully!')
