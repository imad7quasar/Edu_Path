from django.shortcuts import render, redirect
from .models import Question, Answer


from django.shortcuts import render

def quiz_view(request):
    # Define questions directly in the view
    questions = [
        {"text": "How old are you?"},
        {"text": "What is your wilaya?"},
        {"text": "What was your grade in the baccalaureate?"},
        {"text": "What field did you study in secondary school?"},
        {"text": "Which subjects or topics are you most passionate about?"},
        {"text": "Are you more inclined towards theoretical or practical learning?"},
        {"text": "How important is the location of the university to you?"},
        {"text": "Do you prefer a large campus with many amenities or a smaller, more intimate campus environment?"},
        {"text": "Are you interested in participating in extracurricular activities such as sports, arts, or community service?"},
        {"text": "Are you interested in opportunities for internships or cooperative education programs during your studies?"},
        {"text": "Are you open to studying abroad your wilaya  or do you prefer to stay within your wilaya?"},
        {"text": "Are there any specific research areas or specializations you're interested in pursuing?"},
        # Add more questions as needed
    ]
    return render(request, 'quiz.html', {'questions': questions})

from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def submit_quiz_view(request):
    if request.method == 'POST':
        # Process the submitted data
        answers = {}
        for key, value in request.POST.items():
            if key.startswith('answer_'):
                question_text = key.replace('answer_', '')
                # Get the actual question text from the questions dictionary
                question = request.POST.get(f'question_{question_text}')
                answers[question] = value
        
        # Pass the answers to the template
        return render(request, 'quiz_answers.html', {'answers': answers})
    else:
        # Handle GET requests or other cases
        # For now, let's return a 405 Method Not Allowed response
        return HttpResponse(status=405)



def thank_you_view(request):
    return render(request, 'thank_you.html')
