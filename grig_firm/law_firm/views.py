from django.views import View
from django.template.response import TemplateResponse

class LawFirmView(View):
    def get(self, request):
        return TemplateResponse(request, 'law_firm/index.html', {
            'title': 'Юридическая фирма',
            'services': ['Услуга 1', 'Услуга 2', 'Услуга 3'],
            'contact': {'phone': '+7 (123) 456-78-90', 'email': 'info@example.com'}
        })