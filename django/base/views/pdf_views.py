from django.views.generic import TemplateView,CreateView,ListView,DetailView,View
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
    template_name = "form.html"

class CountView(FormView):
    form_class = TextForm
    template_name = "count.html"
    success_url = '/'

    def form_valid(self, form):
        limit = 10

        data = form.cleaned_data
        content = data["content"]
        limit = data["limit"]
        save_or_not = data["save_or_not"]

        splite_content = content.split()
        new_content = collections.Counter(splite_content).most_common(limit)
        ctxt = self.get_context_data(new_content=new_content,form=form)
        
        if save_or_not == 1:
            form.save()  # 保存処理など
            messages.add_message(self.request, messages.SUCCESS, '登録しました！')  # メッセージ出力
        elif save_or_not == 0:
            messages.add_message(self.request, messages.SUCCESS, '登録しませんでした')  # メッセージ出力
        else:
            messages.add_message(self.request, messages.SUCCESS, 'デフォルト設定でデータは保存しませんでした。')

        return super().form_valid(form)


class TestView(FormView):
    template_name = 'index.html'
    form_class = TestForm
    success_url = '/'

    def form_valid(self, form):
        form.save()  # 保存処理など
        #messages.add_message(self.request, messages.SUCCESS, '登録しました！')  # メッセージ出力
        return super().form_valid(form)


class PdfListView(ListView):
    model = Pdf 
    template_name = "list.html"

class PdfDetailView(DetailView):
    model = Pdf
    template_name = "detail.html"