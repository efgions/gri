from django.urls import path
from .views import feedback_view

urlpatterns = [
    path('', feedback_view, name='feedback'),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('feedback.urls')),
]