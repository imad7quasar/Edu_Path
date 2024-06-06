from django.shortcuts import render, get_object_or_404,redirect
from .models import University
from django.contrib import messages
from .forms import CustomRegistrationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomAuthenticationForm

def login_page(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['username'] = username
                return render(request, 'universities.html')
                
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})


from django.http import JsonResponse
def get_university_by_name(request, university_name):
    if request.method == 'GET':
        # Query the database to get the university by name
        university = get_object_or_404(University, university_name=university_name)
        # Prepare context data with university details
        data = {
            'university_name': university.university_name,
            'university_image': university.university_image ,
            'university_overview': university.university_overview,
            'university_fields': university.university_fields,
            'university_location': university.university_location,
            'university_ranking': university.university_ranking,
            'email': university.email,
            'phone': university.phone,
            'website': university.website
        }
        # Render the template with the context data
        return render(request, 'university_page.html', {'university_data': data})
    else:
        # Return an error response for unsupported HTTP methods
        return JsonResponse({'error': 'Method not allowed'}, status=405)


def search_universities(request):
    query = request.GET.get('query')
    if query:
        universities = University.objects.filter(university_name__icontains=query)
        universities_json = [{
            'name': university.university_name,
            'location': university.university_location,
            'image': university.university_image
        } for university in universities]
        return JsonResponse(universities_json, safe=False)
    else:
        return JsonResponse([], safe=False)  # Return empty response if query is empty



# views.py

from django.shortcuts import render

def universities_view(request):
    # You can add any context data you want to pass to the template here
    context = {
        # Add context data if needed
    }
    return render(request, 'universities.html', context)

def landing(request):
    # You can add any context data you want to pass to the template here
    context = {
        # Add context data if needed
    }
    return render(request, 'landing.html', context)
def contact_page(request):
    # You can add any context data you want to pass to the template here
    context = {
        # Add context data if needed
    }
    return render(request, 'contact.html', context)
def abts_page(request):
    context = {
        # Add context data if needed
    }
    return render(request, 'about_us.html', context)
def reg_page(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # Create user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = CustomRegistrationForm()
    return render(request, 'sigin.html', {'form': form})


def questionAboutUs(request):
    # You can add any context data you want to pass to the template here
    context = {
        # Add context data if needed
    }
    return render(request, 'questionAboutUs.html', context)





def startQuiz(request):
    if request.user.is_authenticated:
        # The user is authenticated, retrieve the username from the session
        username = request.session.get('username')
        context = {
            'username': username,  # Add the username to the context
        }
        return render(request, 'start-quiz.html', context)
    else:
        # The user is not authenticated, redirect to the login page
        return redirect('/login/')