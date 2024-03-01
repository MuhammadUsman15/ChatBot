from django.shortcuts import render
from django.http import JsonResponse
import openai

openai_api_key = 'Your Open Api key'
openai.api_key = openai_api_key

def ask_openai(message):
    response = openai.completions.create(
         model = "davinci-002",
        messages=[
            {"role": "system", "content": "You are an helpful assistant."},
            {"role": "user", "content": message},
        ]
    )
    print(response)
    answer = response.choices[0].message.content.strip()
    return answer 
# Create your views here.

def chat(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message': message, 'response': response})
    return render (request, 'chatbot.html')
