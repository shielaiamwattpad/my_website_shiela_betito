from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"
    def get_context_data(self):
        data = {"message_title" : "This is graet!",
                "message": "niceeeee!"}
        return data
    
class ResumePageView (TemplateView):
    template_name = "about.html"
    def get_context_data(self):
        data = {"message_title" : "This is great!",
                "message": "Welcome to my website!"}
        return data