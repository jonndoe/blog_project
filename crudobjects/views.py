from django.db.models import Q
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import Crudobject, Comment
from .forms import CrudobjectForm, CrudCommentForm

from django.core.paginator import ( Paginator,
                                    EmptyPage,
                                    PageNotAnInteger,
                                    )

from django.shortcuts import render, get_object_or_404


'''
# this is for some referrence only

class CrudobjectListView(LoginRequiredMixin, ListView):
    model = Crudobject
    context_object_name = 'crudobject_list'
    template_name = 'crudobjects/crudobject_list.html'
    login_url = 'account_login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['crudobject_list'] = Crudobject.published.all()

        crudobject_list = Crudobject.published.all()
        paginator = Paginator(crudobject_list, 3) # 3 posts in each page
        request = self.request
        page = request.GET.get('page')
        try:
            crudobjects = paginator.page(page)
        except PageNotAnInteger:
            # if page is not an integer deliver the first page
            crudobjects = paginator.page(1)
        except EmptyPage:
            # If page is out of range deliver last page of results
            crudobjects = paginator.page(paginator.num_pages)

        context['page'] = page
        context['crudobjects'] = crudobjects

        return context
  
  
  
  
# this function works good
def CrudobjectListView(request):
    object_list = Crudobject.published.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'crudobjects/crudobject_list.html',
                  {'page': page,
                   'crudobject_list': posts})
'''
class CrudobjectListView(ListView):
    model = Crudobject
    queryset = Crudobject.published.all()
    context_object_name = 'crudobject_list'
    paginate_by = 3
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

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CrudCommentCreateView(CreateView):
    model = Comment
    form_class = CrudCommentForm
    template_name = 'crudobjects/crudcomment_create.html'
    success_url = reverse_lazy('home')