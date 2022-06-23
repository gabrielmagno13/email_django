from django.shortcuts import render
from django.contrib.messages import success, error
from .forms import ContatoForm


def index(request):
    return render(request, 'index.html')


def contato(request):
    form = ContatoForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            form.enviar_email()
            success(request, 'Email enviado com sucesso')
            form = ContatoForm()

        else:
                error(request, 'Email nao enviado')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


def formulario(request):
    return render(request, 'formulario.html')