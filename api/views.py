from django.shortcuts import render
from services.chatgpt_service import ChatGPTService
from django.http import JsonResponse

# Initialize ChatGPT service
chat_service = ChatGPTService()

def send_message(request):
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