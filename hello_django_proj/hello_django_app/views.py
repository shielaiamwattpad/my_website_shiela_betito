from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"
    def get_context_data(self):
        data = {"message_title" : "Favorite Quote",
                "message": "You don’t raise heroes, you raise sons. And if you treat them like sons, they’ll turn out to be heroes, even if it’s just in your own eyes"}
        return data
    
class ResumePageView (TemplateView):
    template_name = "resume.html"
    def get_context_data(self):
        data = {"message_title" : "Website",
                "message1": "Villamayor High School",
                "message": "Elementary: san antonio elementary School"}
        return data

class ContactInfoPageView (TemplateView):
    template_name = "contactInfo.html"
    def get_context_data(self):
        data = {"message_title" : " Shiela Mae Betito ",
                "message1": "Address:san antonio Minalabac Cam sur",
                "message2": "Email: shielabetito12@gmail.com",               
                "message3": "Mobile No. 09353971291"}
        return data