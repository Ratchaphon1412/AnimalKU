from django.urls import path,re_path,include
from Pet import views
urlpatterns = [
    re_path('pet/',views.petAPI),
    re_path('login/',views.accountAPI),
]