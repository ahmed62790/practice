from django.shortcuts import render,redirect
from .forms import contactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    form = contactForm()

    if request.method == 'POST':
        form = contactForm(request.POST)

        

        if form.is_valid():
            name = form.cleaned_data['name']
            email =form.cleaned_data['email'] 
            contant = form.cleaned_data['contant']
            
            html = render_to_string('emails/contactform.html',
                                    {'name': name,
                                    'email' : email,
                                    'conatnt' : contant
                                    }
                                    )
            

            send_mail('this contact for subject', 'this is the message','ahmedkhanmd2021@gmail.com', ['ahmed22khan.ak@gmail.com'], html_message = html)



            return redirect('index')
    else:
        form = contactForm()
    return render(request, 'index.html', {'form' : form})