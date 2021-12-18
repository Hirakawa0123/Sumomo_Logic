from django.views.generic import TemplateView,CreateView,ListView,DetailView,View,DeleteView,UpdateView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

import collections
import re
import sys
import os

from tika import parser

from base.forms import TextForm,FileFieldForm
from base.models import Pdf

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
    template_name = "pages/update.html"
    model = Pdf
    success_url = reverse_lazy('list')
    form_class = TextForm


class FileFieldFormView(FormView):
    form_class = FileFieldForm
    template_name = 'pages/upload_files.html'  # Replace with your template.
    success_url = reverse_lazy('list')  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')

        if form.is_valid():
            for file in files:
                self.handle_uploaded_file(file)
                extension = os.path.basename(file.name).split('.', 1)[1]
                if extension == "pdf":
                    self.orc_pdf(file)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def handle_uploaded_file(self,file):
        file_path = 'media/documents/' + file.name
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
    
    def orc_pdf(self,file):
        file_path = 'media/documents/' + file.name
        file_name =  os.path.basename(file.name).split('.', 1)[0]
        file_data = parser.from_file(file_path)
        text = file_data["content"]

        with open('media/documents/' + file_name + ".txt","w") as f:
            f.write(text)
    
