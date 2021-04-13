from django.urls import path
from .views import *
app_name = 'cars'

urlpatterns = [
    path('', CarListView.as_view(), name='cars'),

]