from django.db import models

# Create your models here.
class Funcionarios(models.Model):
  nome             = models.CharField(max_length=100, verbose_name='Nome do Funcionário')
  email            = models.CharField(max_length=100,verbose_name='Email')
  contato          = models.CharField(max_length=15, verbose_name='Número de Telefone')
  cpf              = models.CharField(max_length=11, verbose_name='CPF do Funcionário')
  rg               = models.CharField(max_length=11, verbose_name='RG do Funcionário')
  cidade           = models.CharField(max_length=50, verbose_name='Cidade')
  rua              = models.CharField(max_length=50, verbose_name='Rua')
  bairro           = models.CharField(max_length=50, verbose_name='Bairro')
  numero_casa      = models.IntegerField(verbose_name='Número da casa')
  dtnasc_func      = models.CharField(max_length=10, verbose_name='Data de Nascimento do Funcionário')
  sexo             = models.CharField(max_length=9, verbose_name="Sexo do funcionário")
  estadocivil      = models.CharField(max_length=15, verbose_name="Estado civil")
  setor            = models.CharField(max_length=16, verbose_name="Setor")
  observacao       = models.TextField( verbose_name="Observação"'')  
  
  class Meta:
    db_table = 'funcionarios'
    
  def __str__(self) -> str:
    return f"{self.nome} {self.contato} {self.cpf} {self.rg} {self.rua} {self.bairro} {self.numero_casa} {self.dtnasc_func} {self.cidade}"
  