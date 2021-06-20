from django.views import generic
from django.urls import reverse_lazy
from .models import Greeting

class IndexView(generic.ListView):
    template_name = 'greetings/index.html'
    context_object_name = 'greeting_list'

    def get_queryset(self):
        """Return the all greetings."""
        return Greeting.objects.all()

class CreateView(generic.edit.CreateView):
    template_name = 'greetings/create.html'
    model = Greeting
    fields = ['message']
    success_url = reverse_lazy('greetings:index') # more robust than hardcoding to /greetings/; directs user to index view after creating a greeting

class UpdateView(generic.edit.UpdateView):
    template_name = 'greetings/update.html'
    model = Greeting
    fields = ['message']
    success_url = reverse_lazy('greetings:index')

class DeleteView(generic.edit.DeleteView):
    template_name = 'greetings/delete.html' # override default of greetings/greeting_confirm_delete.html
    model = Greeting
    success_url = reverse_lazy('greetings:index')

class TextbookView(generic.ListView):
    template_name = 'greetings/textbook.html'
    model = Greeting

class DormView(generic.ListView):
    template_name = 'greetings/dorm.html'
    model = Greeting

class ClassesView(generic.ListView):
    template_name = 'greetings/classes.html'
    model = Greeting

class FoodieView(generic.ListView):
    template_name = 'greetings/Foodie.html'
    model = Greeting

class SuppliesView(generic.ListView):
    template_name = 'greetings/Supplies.html'
    model = Greeting