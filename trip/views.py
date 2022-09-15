from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return render(request, 'trip/index.html')

def camping(request):
    return render(request, 'trip/camping.html')

def corupa(request):
    return render(request, 'trip/corupa.html')

def cozinha(request):
    return render(request, 'trip/cozinha.html')

def mochila(request):
    return render(request, 'trip/mochila.html')

def pico(request):
    return render(request, 'trip/pico.html')


def cadastropost(request):
    if request.method == 'GET':
        form = CadastroPostagem()
        return render(request, "trip/pagina_postagem.html", {'form': form})
    else:
        form = CadastroPostagem(request.POST)
        if form.is_valid():
            cadastro = form.save()
            form = CadastroPostagem()
            return index(request)
        else:
            return render(request, "trip/pagina_postagem.html",{'form':form})


def post(request):
    return render(request, 'trip/pagina_postagem.html',
                  {'postagem': postagem})