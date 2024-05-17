from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member


# Create your views here.
def members(request):
    members = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'members': members
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    member = Member.objects.get(id=id)
    template = loader.get_template('member_details.html')
    context = {
        'member': member
    }
    return HttpResponse(template.render(context, request))