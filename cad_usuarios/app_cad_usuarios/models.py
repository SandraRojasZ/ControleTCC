from django.db import models

# urls de usuarios
# views de usuarios
# models Usuarios para cadastrar no Banco de Dados via Django
class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, default='')
    tipo = models.CharField(max_length=255)
    curso = models.CharField(max_length=255)