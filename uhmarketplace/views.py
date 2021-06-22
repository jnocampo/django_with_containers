from django.views import generic
from django.urls import reverse_lazy
from .models import Uhmarketplace

class IndexView(generic.ListView):
    template_name = 'uhmarketplace/index.html'
    context_object_name = 'uhmarketplace_list'

    def get_queryset(self):
        """Return the all uhmarketplace."""
        return Uhmarketplace.objects.all()

class CreateView(generic.edit.CreateView):
    template_name = 'uhmarketplace/create.html'
    model = Uhmarketplace
    fields = ['message']
    success_url = reverse_lazy('uhmarketplace:index') # more robust than hardcoding to /uhmarketplace/; directs user to index view after creating a Uhmarketplace

class UpdateView(generic.edit.UpdateView):
    template_name = 'uhmarketplace/update.html'
    model = Uhmarketplace
    fields = ['message']
    success_url = reverse_lazy('uhmarketplace:index')

class DeleteView(generic.edit.DeleteView):
    template_name = 'uhmarketplace/delete.html' # override default of uhmarketplace/uhmarketplace_confirm_delete.html
    model = Uhmarketplace
    success_url = reverse_lazy('uhmarketplace:index')

class TextbookView(generic.ListView):
    template_name = 'uhmarketplace/textbook.html'
    model = Uhmarketplace

class DormView(generic.ListView):
    template_name = 'uhmarketplace/dorm.html'
    model = Uhmarketplace

class ClassesView(generic.ListView):
    template_name = 'uhmarketplace/classes.html'
    model = Uhmarketplace

class FoodieView(generic.ListView):
    template_name = 'uhmarketplace/foodie.html'
    model = Uhmarketplace

class SuppliesView(generic.ListView):
    template_name = 'uhmarketplace/supplies.html'
    model = Uhmarketplace
