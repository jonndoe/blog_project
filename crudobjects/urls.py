#/urls.py
from django.urls import path
from .views import ( CrudobjectListView,
                     CrudobjectDetailView,
                     SearchResultsView,
                     CreateCrudobjectView,
                     CrudCommentCreateView,)
from . import views



urlpatterns = [
    path('', CrudobjectListView.as_view(), name='crudobject_list'),
    path('<uuid:pk>', CrudobjectDetailView.as_view(), name='crudobject_detail'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('crudobject_create/', CreateCrudobjectView.as_view(), name='add_crudobject'),
    path('crud_comment_create/', CrudCommentCreateView.as_view(), name='add_crudcomment'),
]