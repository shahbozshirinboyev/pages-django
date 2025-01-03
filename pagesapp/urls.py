from django.urls import path
from .views import HomePageView, AboutPageView, ContactsPageView, NewsPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path('news/', NewsPageView.as_view(), name='news'),
]