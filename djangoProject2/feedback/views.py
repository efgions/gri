from django.shortcuts import render
from .forms import FeedbackForm


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            # Можно добавить здесь код для отправки уведомления администратору
            return render(request, 'thank_you.html')
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html', {'form': form})
