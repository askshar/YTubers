from django.shortcuts import render

from .models import Slider, Team

from youtubers.models import Youtuber


def home(request):
    sliders = Slider.objects.all()
    our_team = Team.objects.all()
    featured_youtubers = Youtuber.objects.order_by('-created_date').filter(is_featured=True)
    all_youtubers = Youtuber.objects.order_by('-created_date')

    context = {
        'sliders': sliders,
        'our_team': our_team,
        'featured_youtubers': featured_youtubers,
        'all_youtubers': all_youtubers
    }
    return render(request, 'webpages/home.html', context)


def about(request):
    our_team = Team.objects.all()
    context = {
        'our_team': our_team
    }
    return render(request, 'webpages/about.html', context)


def services(request):
    return render(request, 'webpages/services.html')


def contact(request):
    return render(request, 'webpages/contact.html')