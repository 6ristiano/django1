from django.shortcuts import render

def index(request):
    context = {
        'curso': 'Programacao web com Django Framework',
        'outro': 'Django é complicadinho mas tentamos aprender',
    }
    return render(request, 'index.html', context)

def contato(request):
    context = {
        'faleconosco': 'Ligue djáá',
        'outro': 'Django batendo na gente',
    }
    return render(request, 'contato.html', context)

