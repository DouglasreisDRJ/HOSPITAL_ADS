# Em pacientes/models.py
from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    rg = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    endereco = models.ForeignKey('enderecos.Endereco', on_delete=models.CASCADE)  # Usar a string 'enderecos.Endereco'
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'pacientes'

    def __str__(self):
        return self.nome



# Create your models here.
