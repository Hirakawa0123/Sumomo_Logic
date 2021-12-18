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
    success_url = reverse_lazy('list')

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
    template_name = 'pages/upload_files.html'
    success_url = reverse_lazy('list')
    save_path = 'media/documents/'
    validate_extension = ["txt", "pdf", "csv", "json", "html", "py"]

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')

        if form.is_valid():
            for file in files:
                extension = os.path.basename(file.name).split('.', 1)[1]
                if extension in self.validate_extension:
                    self.handle_uploaded_file(file)
                    if extension == "pdf":
                        self.orc_pdf(file)
                    self.save_db(file, extension)
                else:
                    pass
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def handle_uploaded_file(self,file):
        file_path = self.save_path + file.name
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
    
    def orc_pdf(self,file):
        file_path = self.save_path + file.name
        file_name =  os.path.basename(file.name).split('.', 1)[0]
        file_data = parser.from_file(file_path)
        text = file_data["content"]

        with open(self.save_path + file_name + ".txt","w") as f:
            f.write(text)
    
    def save_db(self,file,extension):

        if extension == "pdf":
            file_name =  os.path.basename(file.name).split('.', 1)[0]
            with open(self.save_path + file_name + ".txt","r") as f:
                text = f.read()
                myobject = Pdf(file_name=file.name,content=text)
                myobject.save()
        
        elif extension in self.validate_extension:
            with open(self.save_path + file.name, "r") as f:
                text = f.read()
                myobject = Pdf(file_name=file.name,content=text)
                myobject.save()
        
        else:
            pass
