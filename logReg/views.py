from .forms import RegistrationForm, LoginForm
from django.contrib.auth import login as auth_login, authenticate, logout, get_user_model
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode 
from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.views.decorators.debug import sensitive_post_parameters
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse, HttpResponseRedirect 
from django.utils.encoding import force_bytes, force_str 
from django.utils.translation import gettext_lazy as _
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.template.loader import render_to_string
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.urls import reverse_lazy
from django.utils import timezone
from .models import CustomUser


User = get_user_model()
def registration(request):
    if request.method == 'POST': 
        form = RegistrationForm(request.POST) 
        if form.is_valid(): 
            email = form.cleaned_data.get('email')
            # Проверяем, существует ли пользователь с такой почтой
            try:
                existing_user = User.objects.get(email=email)
                # Проверяем, активен ли пользователь
                if not existing_user.is_active:
                    # Удаляем неактивного пользователя
                    existing_user.delete()
                else:
                    # Показываем сообщение об ошибке
                    return render(request, 'registration/error_message.html', {
                        'error': 'Аккаунт с такой почтой уже существует и активен.'
                    })
            except User.DoesNotExist:
                # Нет пользователя с такой почтой, продолжаем регистрацию
                pass
            user = form.save(commit=False) 
            user.is_active = False 
            user.save() 
            current_site = get_current_site(request) 
            mail_subject = 'Ссылка для активации аккаунта на сайте ' + str(current_site) 
            message = render_to_string('registration/acc_active_email.html', { 
                'user': user, 
                'domain': current_site.domain, 
                'uid':urlsafe_base64_encode(force_bytes(user.pk)), 
            }) 
            to_email = form.cleaned_data.get('email') 
            print(to_email)
            email = EmailMessage( 
                        mail_subject, message, to=[to_email] 
            ) 
            email.send() 
            return render(request,'registration/registr_email_messege.html', {'email' : to_email}) 
    else: 
        form = RegistrationForm() 
    return render(request, 'registration/registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                auth_login(request, user)
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})



def user_logout(request):
    logout(request)
    return redirect('index')