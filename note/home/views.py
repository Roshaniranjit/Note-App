from django.shortcuts import render
from .models import Note


# Create your views here.
def home(request):
    notes = Note.objects.all()
    context = {
        'notes': notes
    }
    print(notes)
    return render(request,'index.html',context)





