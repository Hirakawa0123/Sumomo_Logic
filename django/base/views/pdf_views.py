from django.views.generic import TemplateView,CreateView,ListView,DetailView,View
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

import collections

from base.forms import MyModelForm,TextForm
from base.models import Pdf

class MyCreateView(CreateView):
    form_class = MyModelForm
    success_url = reverse_lazy("list")
    template_name = "form.html"

class Index(FormView):
    form_class = TextForm
    template_name = "index.html"

    def form_valid(self, form):
        data = form.cleaned_data
        text = data["text"]

        splite_text = text.split()
        new_text = collections.Counter(splite_text)#.most_common(5)
        ctxt = self.get_context_data(new_text=new_text,form=form)
        return self.render_to_response(ctxt)


class PdfListView(ListView):
    model = Pdf 
    template_name = "list.html"

class PdfDetailView(DetailView):
    model = Pdf
    template_name = "detail.html"