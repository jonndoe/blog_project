#/urls.py
from django.urls import path
from .views import CrudobjectListView, CrudobjectDetailView, SearchResultsView


urlpatterns = [
    path('', CrudobjectListView.as_view(), name='crudobject_list'),
    path('<uuid:pk>', CrudobjectDetailView.as_view(), name='crudobject_detail'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]