from django.db.models import Q
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import Crudobject, Comment
from .forms import CrudobjectForm, CrudCommentForm


class CrudobjectListView(LoginRequiredMixin, ListView):
    model = Crudobject
    context_object_name = 'crudobject_list'
    template_name = 'crudobjects/crudobject_list.html'
    login_url = 'account_login'


class CrudobjectDetailView(LoginRequiredMixin,
                           PermissionRequiredMixin,
                           DetailView):
    model = Crudobject
    context_object_name = 'crudobject'
    template_name = 'crudobjects/crudobject_detail.html'
    login_url = 'account_login'
    permission_required = 'crudobjects.special_status'


class SearchResultsView(ListView):
    model = Crudobject
    context_object_name = 'crudobject_list'
    template_name = 'crudobjects/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Crudobject.objects.filter(
            Q(title__icontains=query) | Q(title__icontains=query)
        )

class CreateCrudobjectView(CreateView):
    model = Crudobject
    form_class = CrudobjectForm
    template_name = 'crudobjects/crudobject_create.html'
    success_url = reverse_lazy('home')


class CrudCommentCreateView(CreateView):
    model = Comment
    form_class = CrudCommentForm
    template_name = 'crudobjects/crudcomment_create.html'
    success_url = reverse_lazy('home')