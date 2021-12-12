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

from base.forms import TextForm,UploadFileForm
from base.models import Pdf

from tika import parser

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


# ------------------------------------------------------------------
def file_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            sys.stderr.write("*** file_upload *** aaa ***\n")
            handle_uploaded_file(request.FILES['file'])
            Orc(request.FILES['file'])
            file_obj = request.FILES['file']
            sys.stderr.write(file_obj.name + "\n")
            return HttpResponseRedirect('/')
            # return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'pages/upload_files.html', {'form': form})
#
#
# ------------------------------------------------------------------
def handle_uploaded_file(file_obj):
    sys.stderr.write("*** handle_uploaded_file *** aaa ***\n")
    sys.stderr.write(file_obj.name + "\n")
    file_path = 'media/documents/' + file_obj.name 
    sys.stderr.write(file_path + "\n")
    with open(file_path, 'wb+') as destination:
        for chunk in file_obj.chunks():
            sys.stderr.write("*** handle_uploaded_file *** ccc ***\n")
            destination.write(chunk)
            sys.stderr.write("*** handle_uploaded_file *** eee ***\n")
#
# ------------------------------------------------------------------
def success(request):
    str_out = "Success!<p />"
    str_out += "成功<p />"
    return HttpResponse(str_out)
# ------------------------------------------------------------------

def Orc(file_obj):
    file_path = 'media/documents/' + file_obj.name
    file_name =  os.path.basename(file_obj.name).split('.', 1)[0]
    extension = os.path.basename(file_obj.name).split('.', 1)[1]
    file_data = parser.from_file(file_path)
    text = file_data["content"]

    with open('media/documents/' + file_name + ".txt","w") as f:
        f.write(text)
    
    os.remove('media/documents/' + file_name + "." + extension)
    
