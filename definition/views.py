# from .forms import DefinitionForm

from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)
# ========= your views here.========

# createView
# def createView(request, *args, **kwargs):
#     return render(request, 'home.html', {} )
# # updateView
# def updateView(request,*args, **kwargs):
#     return render(request, 'update.html', {}) 
from .forms import DefinitionForm
from .models import Definition
# CreateView
class HackerCreateView(CreateView):
     template_name = 'infoData/theCreate.html'
     form_class = DefinitionForm
     queryset = Definition.objects.all()

     def form_valid(self, form):
         print(form.cleaned_data)
         return super().form_valid(form)   

#listView  
class HackerListView(ListView):
     template_name = 'infoData/theList.html'
     queryset = Definition.objects.all()
     def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Definition, id=id_)

#detailView  

class HackerDetailView(DetailView):
    template_name = 'infoData/theDetail.html'
    #  queryset = Definition.objects.all()
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Definition, id=id_)

# updateView
class HackerUpdateView(UpdateView):
     template_name = 'infoData/theCreate.html'
     form_class = DefinitionForm
     queryset = Definition.objects.all()
     def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Definition, id=id_)

     def form_valid(self, form):
         print(form.cleaned_data)
         return super().form_valid(form)

#deleteView  
class HackerDeleteView(DeleteView):
    template_name = 'infoData/theDelete.html'
    #  queryset = Definition.objects.all()
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Definition, id=id_)

    def get_success_url(self):
        return reverse('definitions:definition-list')