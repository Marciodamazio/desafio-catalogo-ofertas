from django.shortcuts import render
from .raspagem import obter_dados_produto  

from .models import Produto

def lista_produtos(request):
    produtos = Produto.objects.all()

    # Filtragem
    frete_gratis = request.GET.get('frete_gratis')
    full = request.GET.get('full')

    if frete_gratis:
        produtos = produtos.filter(frete_gratis=True)
    if full:
        produtos = produtos.filter(tipo_entrega='Full')

    # Maior e menor preço
    maior_preco = produtos.order_by('-preco')[:1]
    menor_preco = produtos.order_by('preco')[:1]

    return render(request, 'produtos/lista_produtos.html', {
        'produtos': produtos,
        'maior_preco': maior_preco,
        'menor_preco': menor_preco
    })
def lista_produtos(request):
    produtos = obter_dados_produto()  # Chama a função de raspagem
    return render(request, 'produtos/lista_produtos.html', {'produtos': produtos})
