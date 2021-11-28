from django.views.generic import TemplateView,CreateView
from django.urls import reverse_lazy
from base.forms import MyModelForm
from base.models import Pdf

class IndexView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['name'] = Pdf.objects.all()[:5]
        context['name'] = "mike"
        return context

class MyCreateView(CreateView):
    form_class = MyModelForm
    success_url = reverse_lazy("index")
    template_name = "form.html"