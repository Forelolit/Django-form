from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import FormSubmission

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваше сообщение успешно отправлено!')
            return redirect('index')
    else:
        form = ContactForm()
    
    submissions = FormSubmission.objects.all()[:5]
    return render(request, 'myapp/index.html', {
        'form': form,
        'submissions': submissions
    })
