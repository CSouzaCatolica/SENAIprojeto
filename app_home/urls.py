from django.urls import path
from app_home import views

    # path('logout', views.logout_view, name='logout'),
urlpatterns = [
    #views
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    # path('logout', views.logout_view, name='logout'),
    
    path('dev', views.dev, name='dev'),

    path('usuarios', views.view_usuarios, name='view_usuarios'),
    path('cargos', views.view_cargos, name='view_cargos'),
    path('itens', views.view_itens, name='view_itens'),
    # path('itensEditar', views.view_itens_edicao, name='view_itens_edicao'),
    path('emprestimos', views.view_emprestimos, name='view_emprestimos'),
    path('estoque', views.view_estoque, name='view_estoque'),
    #users
    path('get_user/<int:id>', views.get_user, name='get_user'),
    path('get_allUsers', views.get_allUsers, name='get_allUsers'),
    path('delete_user/<int:id>', views.delete_user, name='delete_user'),
    path('update_user/<int:id>', views.update_user, name='update_user'),
    path('create_user', views.create_user, name='create_user'),
    #cargo
    path('create_cargo', views.create_cargo, name='create_cargo'),
    path('get_allCargos', views.get_allCargos, name='get_allCargos'),
    path('delete_cargo/<int:id>', views.delete_cargo, name='delete_cargo'),
    path('update_cargo/<int:id>', views.update_cargo, name='update_cargo'),
    path('get_cargo/<int:id>', views.get_cargo, name='get_cargo'),
    #emprestimos
    path('create_emprestimo', views.create_emprestimo, name='create_emprestimo'),
    path('get_allEmprestimos', views.get_allEmprestimos, name='get_allEmprestimos'),
    path('delete_emprestimo/<int:id>', views.delete_emprestimo, name='delete_emprestimo'),
    path('update_emprestimo/<int:id>', views.update_emprestimo, name='update_emprestimo'),
    path('get_emprestimo/<int:id>', views.get_emprestimo, name='get_emprestimo'),
    path('get_allEmprestimosByUser/<int:id>', views.get_allEmprestimosByUser, name='get_allEmprestimosByUser'),
    path('get_allEmprestimosByItem/<int:id>', views.get_allEmprestimosByItem, name='get_allEmprestimosByItem'),
    #item
    path('create_item', views.create_item, name='create_item'),
    path('get_allItems', views.get_allItems, name='get_allItems'),
    path('delete_item/<int:id>', views.delete_item, name='delete_item'),
    path('update_item/<int:id>', views.update_item, name='update_item'),
    path('get_item/<int:id>', views.get_item, name='get_item'),
    path('get_allItemsByUser/<int:id>', views.get_allItemsByUser, name='get_allItemsByUser'),
    #estoque
    path('create_estoque', views.create_estoque, name='create_estoque'),
    path('get_allEstoque', views.get_allEstoque, name='get_allEstoque'),
    path('delete_estoque/<int:id>', views.delete_estoque, name='delete_estoque'),
    path('update_estoque/<int:id>', views.update_estoque, name='update_estoque'),
    path('get_estoque/<int:id>', views.get_estoque, name='get_estoque'),
    
]
