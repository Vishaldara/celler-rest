from django.shortcuts import render
from celler.models import Contact


# Create your views here.

def get_contacts(request):
    return render(request, 'dara/home.html',
                  {'contact_list': Contact.objects.all()})
