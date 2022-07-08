import requests

from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

from .forms import LoginForm, UserRegistrationForm


#@login_required
def chat(request, chat_id):
    user = request.user
    messages = requests.get(f'http://127.0.0.1:8000/api/chat/{chat_id}/')
    messages = messages.json()
    print(chat_id)
    return render(request, 'chat/chat.html', {
        'chat_id': chat_id,
        'messages': messages
    })

#@login_required
# def chat_list(request):
#     chats = requests.get(f'http://127.0.0.1:8000/api/chats/')
#     print(request.user, request.auth)
#     print(chats.text)
#     chats = chats.json()
#     print(chats)
#     return render(request, 'chat/chats.html', {'chats': chats})

# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             print(cd)
#             username = cd['username']
#             password = cd['password']
#             user = authenticate(request,
#                                 username=username,
#                                 password=password)
#             if user is not None:
#                 if user.is_active:
#                     print(username)
#                     user_info = requests.post(
#                         'http://127.0.0.1:8000/api/login/',
#                          json={'username': username,
#                               'password': password}).json()
#                     if 'token' in user_info:
                        
#                         token = user_info['token']
#                         #print(request.META)
#                         request.META['Authorization'] = f'Token {token}'
#                         #print(request.headers)
#                         print(user_info)
#                         login(request, user)
#                         return HttpResponse('Authenticated successfully')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()
#     return render(request, 'registration/login.html', {'form': form})

# def register(request):
#     if request.method == 'POST':
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             username = user_form.cleaned_data['username']
#             new_user = requests.post(
#                 'http://127.0.0.1:8000/api/create/',
#                 json={'username': username,
#                       'password': user_form.cleaned_data['password']}).json()
#             if username != new_user['username']:
#                 return HttpResponse('This username is taken.')
            
            # THIS RAISES AN ERROR DUE TO USAGE OF THE SAME DB
            # new_user = user_form.save(commit=False)
            # new_user.set_password(
            #     user_form.cleaned_data['password'])
            # new_user.save()
#             return render(request,
#                         'registration/register_done.html', {})
#         else:
#             return HttpResponse('Something went wrong')
#     else:
#         user_form = UserRegistrationForm()
#     return render(request,
#                   'registration/register.html',
#                   {'user_form': user_form})
                
# def get_token(request, password):
#     token = requests.post('http://127.0.0.1:8000/api/login/',
#                   json={'username': request.user.username,
#                         'password': password}).json()['token']
#     return token
    