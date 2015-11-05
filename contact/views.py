from django.shortcuts import render
from django.views.generic import FormView, DetailView 

from .models import Message
from .forms import MessageForm, ContactForm

class MessageDetailView(DetailView):
    model = Message

class MessageAddView(FormView):
    form_class = MessageForm
    template_name = 'contact/message_form.html'
    sucess_url='/'
    
    #co jezeli dane beda poprawne 
    def form_valid(self, form):
        form.save()
        return super(MessageAddView, self).form_valid(form)
    