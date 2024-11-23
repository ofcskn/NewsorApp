from django.shortcuts import render
from django.http import HttpResponse
from services.chatgpt_service import ChatGPTService
from django.http import JsonResponse
from .forms import ChatForm
# Initialize ChatGPT service
chat_service = ChatGPTService()

def home(request):
    """
    Handle the request to render the home page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML for the home page.
    """
    try:
        form = ChatForm()
        return render(request, 'frontend/home.html', {"form": form})
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}", status=500)

def chat(request):
    """
    Handle AJAX chat requests and return AI model responses.
    """
    if request.method == 'POST':
        user_message = request.POST.get('message')
        try:
            ai_response = chat_service.get_chat_response([
                {"role": "user", "content": user_message}
            ])
            return JsonResponse({'message': user_message, 'response': ai_response})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request'}, status=400)