from django.views.generic import View
from django.shortcuts import render
from fest9000.models import *


class Home(View):
    sponsor = Sponsor
    message = Message
    profile = Profile
    tname = 'fest9000/home.html'

    def get(self, request):
        return render(request, self.tname, { 'sponsor': self.getSponsor(), 'profile': self.getProfile(), 'message': self.getMessage() })

    def post(self, request):
        m = Message(name = request.POST.get('name'), text = request.POST.get('message'))
        m.save()
        return render(request, self.tname, { 'sponsor': self.getSponsor(), 'profile': self.getProfile(), 'message': self.getMessage() })

    def getSponsor(self):
        return self.sponsor.objects.all().order_by('name')

    def getProfile(self):
        return self.profile.objects.all()

    def getMessage(self):
        return self.message.objects.all()

