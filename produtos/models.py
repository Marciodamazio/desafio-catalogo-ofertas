from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    imagem = models.URLField()
    preco = models.CharField(max_length=50)
    preco_sem_desconto = models.CharField(max_length=50, null=True, blank=True)
    percentual_desconto = models.CharField(max_length=50, null=True, blank=True)
    link = models.URLField()
    tipo_entrega = models.CharField(max_length=50)
    frete_gratis = models.BooleanField(default=False)

    def __str__(self):
        return self.nome