from django.shortcuts import render
from django.views.generic import TemplateView



# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ContactsPageView(TemplateView):
    template_name = 'contacts.html'

class NewsPageView(TemplateView):
    template_name = 'news.html'
