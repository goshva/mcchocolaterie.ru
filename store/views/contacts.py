from django.shortcuts import render
from django.views import  View

class Contacts(View):

    def get(self, request):
        return render(request, 'contacts.html', {})