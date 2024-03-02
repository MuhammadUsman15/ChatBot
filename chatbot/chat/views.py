from django.shortcuts import render
from django.http import JsonResponse
# import genai
import google.generativeai as genai

# Replace with your Google Cloud API key
google_api_key = 'Your API'
genai.configure(api_key=google_api_key)


def ask_gemini(message):
    # Modify model name according to your specific Gemini model
    model = genai.GenerativeModel('gemini-pro')  # Replace with your model name
    response = model.generate_content( message)
    return response.text.strip()


def chat(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_gemini(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')

