from django.urls import path

from .views import HomePageView, ResumePageView, ContactInfoPageView

urlpatterns = [
    path( 'home', HomePageView.as_view(), name="home_view"),
    path( 'resume', ResumePageView.as_view(), name="resume_view"),
    path( 'contactinfo', ContactInfoPageView.as_view(), name="contactinfo_view")
]