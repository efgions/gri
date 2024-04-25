from django.contrib import admin
from django.urls import path

from law_firm.views import LawFirmView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LawFirmView.as_view(), name='law_firm'),
]