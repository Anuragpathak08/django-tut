# Tutorial 1: My First Django Website

Welcome to your first Django project. If you're looking at the file structure and wondering why we need so many files just to say "Hello World," relax. Django is just being organized. 

In this tutorial, we will build a simple 4-page website (Home, About, Contact, Hobbies) to understand the core concepts of Django. We will start simple to build your confidence, then add a little complexity at the end.

## 1. Project vs. App: What's the difference?
Before writing code, you need to understand the hierarchy. 
- **Project (`mysite`)**: The entire website. It holds global settings and configurations. Think of it as the whole house.
- **App (`pages`)**: A specific feature or module. Think of it as a room in the house (like the kitchen). 

**Commands to create them:**
```bash
django-admin startproject mysite       # 1. Create the project (from the outside)
cd mysite                              # 2. Step inside the project folder
python manage.py startapp pages        # 3. Create the app (using the project's tool!)
```
*(Notice we used `manage.py` for the app? That's because `manage.py` is your project's personal assistant. `django-admin` is the generic tool you use before the project exists.)*

## 2. The Initial Project Structure
Right after running those commands, your folder looks like this. Notice what is **missing**: there is no `urls.py` in the `pages` app yet, and no `templates` folder. We will create those soon.

```text
mysite/                  # Main Project folder
├── mysite/              # Project settings
│   ├── settings.py      
│   ├── urls.py          # Main URL router
│   └── wsgi.py / asgi.py
├── pages/               # Your Django App
│   ├── views.py         # Your Python functions go here
│   ├── apps.py          
│   └── models.py        
└── manage.py            # The magic command-line tool
```

## 3. The "I Always Forget This" Setup (`settings.py`)
Django doesn't read minds. It doesn't know your app or your HTML files exist until you explicitly tell it. Open `mysite/settings.py` and make these two changes:

**A. Register your app:**
Find `INSTALLED_APPS` and add `'pages'` to the list:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages', # <-- Add your app name here!
]
```

**B. Tell Django where your templates live:**
Find the `TEMPLATES` setting. We are using a project-level templates folder, so update the `DIRS` list:
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # <-- Add this line
        'APP_DIRS': True,
        # ... rest of the settings
    },
]
```

## 4. Creating the Missing Pieces
Now, let's create the files Django is waiting for:
1. Create a folder named `templates` in the **root** directory (same level as `manage.py`).
2. Create a file named `urls.py` inside the `pages` app folder.

Your **final** project structure should now look like this:
```text
mysite/                  
├── mysite/              
│   ├── settings.py      # (We just edited this!)
│   └── urls.py          # Main URL router
├── pages/               
│   ├── views.py         # We will write functions here
│   └── urls.py          # <-- You just created this!
├── templates/           # <-- You just created this! (along with the html files inside the folder)
│   ├── home.html
│   ├── about.html
│   ├── contact.html
│   └── hobbies.html
└── manage.py            
```

## 5. Views: The Brains
All your page logic goes into `pages/views.py`. A view is a Python function that takes a `request` and returns a `response`. Let's write them, starting simple.

```python
from django.shortcuts import render

# 1. Simple: Just passing a name
def home(request):
    context = {"name": "Anurag Pathak"}
    return render(request, "home.html", context)

# 2. Simple: No dynamic data needed at all
def about(request):
    return render(request, "about.html")

# 3. Simple: Also no dynamic data needed
def contact(request):
    return render(request, "contact.html")

# 4. A bit more complex: Passing a list to use in a loop
def hobbies(request):
    context = {"hobbies": ["Python", "Django", "Gaming", "Music"]}
    return render(request, "hobbies.html", context)
```

## 6. Routing: Connecting URLs to Views
When you type a URL, Django checks the main `urls.py`, which then forwards the request to the app's `urls.py`.

**Main `mysite/urls.py`:**
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")), # Forwards requests to the 'pages' app
]
```

**App `pages/urls.py`:**
```python
from django.urls import path
from .views import home, about, contact, hobbies

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("hobbies/", hobbies, name="hobbies"),
]
```

## 7. Templates: The Face
Templates are HTML files with superpowers. Let's build them from simplest to most complex.

**`templates/home.html`** (Uses a variable)
```html
<h1>Welcome, {{ name }}!</h1>
<p>This is the home page of my first Django website.</p>
```

**`templates/about.html`** (Plain HTML, builds confidence)
```html
<h1>About Me</h1>
<p>I am learning Django and building cool things.</p>
```

**`templates/contact.html`** (Plain HTML, builds confidence)
```html
<h1>Contact</h1>
<p>You can reach me at: fake@email.com</p>
```

**`templates/hobbies.html`** (Introducing logic: The For Loop)
```html
<h1>My Hobbies</h1>
<ul>
    {% for hobby in hobbies %}
        <li>{{ hobby }}</li>
    {% endfor %}
</ul>
```

## 8. How to Run This Project
1. Open your terminal in the root folder (where `manage.py` is).
2. Activate your virtual environment.
3. Run the server:
   ```bash
   python manage.py runserver
   ```
4. Open your browser and go to `http://127.0.0.1:8000/`.

---
### Check Your Understanding
Before moving to the next tutorial, ask yourself: If I want to add a new page called `/blog/`, which **three** files do I need to touch or create to make it work? 

*(Hint: Think about the path the request takes: URL -> View -> Template).*
