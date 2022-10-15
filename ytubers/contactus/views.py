from django.shortcuts import redirect, render
from django.contrib import messages

from contactus.models import ContactUs

# Create your views here.


def contact_us(request):
    
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        user_id = request.POST['user_id']
        company_name = request.POST['company_name']
        phone = request.POST['phone']
        subject = request.POST['subject']
        description = request.POST['description']

        contact_form = ContactUs(firstname=firstname, lastname=lastname,
                                email=email, user_id=user_id, company_name=company_name,
                            phone=phone, subject=subject, description=description
        )

        contact_form.save()
        messages.success(request, "Thanks for reaching out to us.")
        return redirect('contact')