from django.shortcuts import render
from django.http import JsonResponse
# import genai
import google.generativeai as genai

<<<<<<< HEAD
# Replace with your Google Cloud API key
google_api_key = 'Your API'
genai.configure(api_key=google_api_key)


def ask_gemini(message):
    # Modify model name according to your specific Gemini model
    model = genai.GenerativeModel('gemini-pro')  # Replace with your model name
    response = model.generate_content( message)
    return response.text.strip()
=======
openai_api_key = 'Your Open Api key'
openai.api_key = openai_api_key
>>>>>>> a0a238013177949d66336319505eb6af5f663c26


def chat(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_gemini(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')

