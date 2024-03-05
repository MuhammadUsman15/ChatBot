from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth.models import User
# import genai
import google.generativeai as genai
from .models import Chat
from django.utils import timezone
# Replace with your Google Cloud API key
google_api_key = 'Your API Key'
genai.configure(api_key=google_api_key)


def ask_gemini(message):
    # Modify model name according to your specific Gemini model
    model = genai.GenerativeModel('gemini-pro')  # Replace with your model name
    response = model.generate_content( message)
    return response.text.strip()


def chat(request):
    chats = Chat.objects.filter(user = request.user)

    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_gemini(message)

        chat = Chat(user = request.user,message =message, response= response, created_at= timezone.now())
        chat.save()
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html', {'chats':chats})

def login(request):
    if request.method ==  "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request,  username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('chat')
        else:
            error_message = 'Invalid username or password'
            return render(request,'login.html', {'error_message': error_message })
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request, user)
                return redirect('chat')
            except:
                error_message = 'Error creating account'
                return  render(request, 'register.html', {'error_message': error_message})
        else:
            error_message = 'Password does not match.'
            return render(request, 'register.html',{'error_message':error_message})
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')