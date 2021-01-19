from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from django.template import loader
# Create your views here.

class Index(View):
    #This is the starting view
    
    def get(self, request):

        template = loader.get_template("consumer/index.html")
        content = {}
        return HttpResponse(template.render(content,request))
