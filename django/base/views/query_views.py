from django.views.generic import TemplateView,CreateView,ListView,DetailView,View,DeleteView,UpdateView,FormView
from django.urls import reverse_lazy

from base.models import Search
from base.forms import SearchQueryForm

class SearchQueryUploadView(FormView):
    form_class = SearchQueryForm
    template_name = "pages/search_query/search_form.html"
    success_url = reverse_lazy('search_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class SearchQueryListView(ListView):
    model = Search 
    paginate_by = 10
    template_name = "pages/search_query/search_list.html"

class SearchQueryDetailView(DetailView):
    model = Search
    template_name = "pages/search_query/search_detail.html"

class SearchQueryDeleteView(DeleteView):
    model = Search
    success_url = reverse_lazy('search_list')
    template_name = "pages/search_query/search_delete.html"

class SearchQueryUpdateView(UpdateView):
    template_name = "pages/search_query/search_update.html"
    model = Search
    success_url = reverse_lazy('search_list')
    form_class = SearchQueryForm