from django.shortcuts import render, get_object_or_404
from .models import University
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
