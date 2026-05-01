from django.views.generic import ListView
from plays.models import Show

class HomepageView(ListView):
    model = Show
    template_name = 'homepage/homepage.html'
    context_object_name = 'show_list'
    queryset = Show.objects.select_related('play').order_by('starts_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context