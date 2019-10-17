from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import BadHeaderError, EmailMessage, send_mail
from myportfolio import settings
from .models import Projects, Services, HomePage
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        html_content = (
            '<h4>You have received a new message from the contact us form on your website</h4><br/>'
            '<strong>Name: </strong>' + request.POST['name'] + '<br/>'
            '<strong>Email: </strong>' + request.POST['email'] + '<br/>'
            '<strong>Message: </strong>' + request.POST['message'] + ''
        )
        from_email = settings.EMAIL_HOST_USER
        to = [settings.ADMINS[0][1]]
        try:
            msg = EmailMessage(subject, html_content, from_email, to)
            msg.content_subtype = "html"
            msg.send()
            return redirect('/')  
            
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
    else:
        context = {
            'form': ContactForm(), 
            'page': HomePage.objects.get(),  
            'projects': Projects.objects.all(),
            'services': Services.objects.all()
        }
    return render(request, 'index.html', context)