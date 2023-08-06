from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render

from mail_templated_simple import send_mail

from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            context = {
                'name': name,
                'authentication': False,
                'email': email,
                'message': message,
                'SITE_URL': settings.SITE_URL
            }
            if request.user.is_authenticated:
                context['authentication'] = request.user.username

            send_mail('contact/emails/submission.tpl', context, None, settings.CONTACT_EMAILS)

            messages.success(request, 'Your message has been sent.')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
