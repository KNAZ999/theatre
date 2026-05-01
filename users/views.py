from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from users.forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('homepage:homepage')
    template_name = 'homepage/homepage.html'  # ← Указан явно

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)