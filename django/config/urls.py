"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.PdfListView.as_view(),name="list"),
    path("upload/",views.UploadView.as_view(),name="upload"),
    path('items/<int:pk>/',views.PdfDetailView.as_view(),name="detail"),
    path('items/<int:pk>/delete/',views.PdfDeleteView.as_view(),name="delete"),
    path('items/<int:pk>/update/',views.PdfUpdateView.as_view(),name="update"),
    path('file_upload/', views.FileFieldFormView.as_view(), name='file_upload'),

    # query
    path('search/', views.SearchQueryListView.as_view(), name='search_list'),
    path('search/form/', views.SearchQueryUploadView.as_view(), name='search_form'),
    path('search/<int:pk>/',views.SearchQueryDetailView.as_view(),name="search_detail"),
    path('search/<int:pk>/delete/',views.SearchQueryDeleteView.as_view(),name="search_delete"),
    path('search/<int:pk>/update/',views.SearchQueryUpdateView.as_view(),name="search_update"),
]
