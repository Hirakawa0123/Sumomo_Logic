from django.views.generic import TemplateView
from base.models import Pdf

class IndexView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = Pdf.objects.all()[:5]
        return context