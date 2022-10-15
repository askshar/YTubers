from django.contrib import messages
from django.shortcuts import redirect

from hiretubers.models import Hiretuber



def hiretuber(request):
    
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        tuber_id = request.POST['tuber_id']
        tubername = request.POST['tubername']
        city = request.POST['city']
        phone = request.POST['phone']
        state = request.POST['state']
        message = request.POST['message']
        user_id = request.POST['user_id']

        hiretuber = Hiretuber(firstname=firstname, lastname=lastname, email=email,
                                tuber_id=tuber_id, tubername=tubername, city=city,
                                phone=phone, state=state, message=message, user_id=user_id
        )

        hiretuber.save()
        messages.success(request, "Thanks for reaching out!")
        return redirect('youtubers')