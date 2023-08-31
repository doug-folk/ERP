from django.urls import path
from django.conf.urls.static import static
from . import settings
from erp.views import DashboardView, ErpLoginView, ErpLogoutView, HomeView, ProdutoCreateView, ProdutoDeleteView, \
    ProdutoDetailView, ProdutoListView, ProdutoUpdateView,\
    VendaCreateView, VendaDeleteView, VendaDetailView, VendaListView, VendaUpdateView, atualizar_funcionario, \
    busca_funcionario_id, cria_funcionario, lista_funcionarios

app_name = 'erp'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    #login
    path('login/', ErpLoginView.as_view(), name='login'),
    path('logout/', ErpLogoutView.as_view(), name='logout'),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),

    # Funcionários
    path('funcionarios/', lista_funcionarios, name='lista_funcionarios'),
    path('funcionarios/novo', cria_funcionario, name='cria_funcionario'),
    path('funcionarios/detalhe/<pk>', busca_funcionario_id, name='busca_funcionario_id'),
    path('funcionarios/atualiza/<pk>', atualizar_funcionario, name='atualizar_funcionario'),

    # Produtos
    path('produtos/novo', ProdutoCreateView.as_view(), name='criar_produto'),
    path('produtos/', ProdutoListView.as_view(), name='lista_produto'),
    path('produtos/atualiza/<pk>', ProdutoUpdateView.as_view(), name='atualiza_produto'),
    path('produtos/detalhe/<pk>', ProdutoDetailView.as_view(), name='detalhe_produto'),
    path('produtos/deleta/<pk>', ProdutoDeleteView.as_view(), name='deleta_produto'),

    #Vendas
    path('vendas', VendaListView.as_view(), name='venda'),
    path('vendas/lista', VendaListView.as_view(), name='lista_vendas'),
    path('vendas/novo', VendaCreateView.as_view(), name='cria_venda'),
    path('vendas/detalhe/<pk>', VendaDetailView.as_view(), name='detalhe_venda'),
    path('vendas/deleta/<pk>', VendaDeleteView.as_view(), name='deleta_venda'),
    path('vendas/atualiza/<pk>', VendaUpdateView.as_view(), name='atualiza_venda'),


    
     

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)