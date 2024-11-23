from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """
    Handle the request to render the home page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML for the home page.
    """
    try:
        return render(request, 'frontend/home.html')
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}", status=500)
