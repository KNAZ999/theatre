from django.views.generic import DetailView
from plays.models import Show


class ShowDetailView(DetailView):
    model = Show
    template_name = 'plays/show_detail.html'
    context_object_name = 'object'  # ← важно: в шаблоне вы используете {{ object }}