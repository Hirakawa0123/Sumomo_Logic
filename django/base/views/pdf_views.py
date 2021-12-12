from django.views.generic import TemplateView,CreateView,ListView,DetailView,View,DeleteView,UpdateView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib import messages
from django.shortcuts import render

import collections
import re

from base.forms import MyModelForm,TextForm,TestForm
from base.models import Pdf,Post

class MyCreateView(CreateView):
    form_class = MyModelForm
    success_url = reverse_lazy("list")
    template_name = "pages/form.html"

class UploadView(FormView):
    form_class = TextForm
    template_name = "pages/upload.html"
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class PdfListView(ListView):
    model = Pdf 
    paginate_by = 10
    template_name = "pages/list.html"

class PdfDetailView(DetailView):
    model = Pdf
    template_name = "pages/detail.html"

class PdfDeleteView(DeleteView):
    model = Pdf
    success_url = reverse_lazy('list')
    template_name = "pages/delete.html"

class PdfUpdateView(UpdateView):
    model = Pdf
    fields = ["file_name","content"]
    success_url = reverse_lazy('list')
    template_name = "pages/update.html"