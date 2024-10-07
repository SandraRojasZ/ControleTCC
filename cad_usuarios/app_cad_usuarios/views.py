from django.shortcuts import render
from .models import Usuarios # importar a classe que foi criado no models.py

def home(request):
    return render(request, 'usuarios/home.html')

# Deverá já ter uma uls/rota de usuarios antes de criar uma view
# urls.py -> path('usuarios/', views.usuarios, name='listagem_usuarios')
# Deverá constar no models para puxar os dados dos campos da BD
# puxar a class Usuarios que foi criado no models.py
# Django irá substituir essa linha pelo valor da lista de objetos Usuarios.
def usuarios(request):
    # Salvar os dados da tela home.html para o bando de dados db.sqlite
    novo_usuario = Usuarios()
    novo_usuario.nome= request.POST.get('nome') #name = "nome" no home.html
    novo_usuario.tipo = request.POST.get('tipo') #name = "tipo" no home.html
    novo_usuario.curso = request.POST.get('curso') #name = "curso" no home.html
    novo_usuario.save()
    # Exibir todos os usuários já cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuarios.objects.all()
    }
    # Retornar os dados para a página de listagem de usuários
    return render(request, 'usuarios/usuarios.html', usuarios)