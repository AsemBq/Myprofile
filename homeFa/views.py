from django.shortcuts import render,redirect
from . import models
from home.models import Ticket, SocialMedia


def home_fa(request):
    header = models.Header.objects.last()
    aboutMe = models.AboutMe.objects.last()
    socialMedia = SocialMedia.objects.all()
    technologys = models.Technology.objects.all()
    tools = models.Tools.objects.all()
    otherSkills = models.OtherSkills.objects.all()
    projects = models.Project.objects.all()

    if request.method == "POST":
        name = request.POST.get('fullName')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Ticket.objects.create(name=name, email=email, message=message)
        return redirect('homeFa:home')
    return render(request, 'homeFa/fa.html',
                  context={'header': header, 'aboutMe': aboutMe, 'technologys': technologys, 'socialMedia': socialMedia,
                           'tools': tools, 'otherSkills': otherSkills,'projects':projects})