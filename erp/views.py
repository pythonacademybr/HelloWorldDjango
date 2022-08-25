from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from core.models import Funcionario, Produto, Venda
from erp.forms import InsereFuncionarioForm, InsereProdutoForm, InsereVendaForm


# PÁGINA PRINCIPAL
# ----------------------------------------------

class HomeView(TemplateView):
    template_name = "erp/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()

        context['vendas'] = Venda.objetos.all()
        
        # Soma de vendas por funcionário
        context['vendas_funcionario'] = \
            Venda.objetos.values('funcionario__nome').annotate(
                numero_vendas=Sum('produto'),
                total_vendas=Sum('produto__preco'),
                media_venda=Sum('produto__preco')/Sum('produto')
            )

        # Total em vendas
        context['total_vendas'] = Venda.objetos.aggregate(vendas=Sum('produto__preco'))

        # Quantidade total de vendas
        context['qtde_vendas'] = Venda.objetos.count()

        return context


# PÁGINA PRINCIPAL FUNCIONÁRIOS
# ----------------------------------------------

class HomeFuncionarioView(TemplateView):
    template_name = "erp/funcionarios/index.html"


# LISTA DE FUNCIONÁRIOS
# ----------------------------------------------

class ListaFuncionariosView(ListView):
    template_name = "erp/funcionarios/lista.html"
    model = Funcionario
    context_object_name = "funcionarios"


# CADASTRAMENTO DE FUNCIONÁRIOS
# ----------------------------------------------

class CriaFuncionarioView(CreateView):
    template_name = "erp/funcionarios/cria.html"
    model = Funcionario
    form_class = InsereFuncionarioForm
    success_url = reverse_lazy("erp:lista_funcionarios")


# ATUALIZAÇÃO DE FUNCIONÁRIOS
# ----------------------------------------------

class AtualizaFuncionarioView(UpdateView):
    template_name = "erp/funcionarios/atualiza.html"
    model = Funcionario
    fields = '__all__'
    context_object_name = 'funcionario'
    success_url = reverse_lazy("erp:lista_funcionarios")


# EXCLUSÃO DE FUNCIONÁRIOS
# ----------------------------------------------

class DeletaFuncionarioView(DeleteView):
    template_name = "erp/funcionarios/exclui.html"
    model = Funcionario
    context_object_name = 'funcionario'
    success_url = reverse_lazy("erp:lista_funcionarios")


# PÁGINA PRINCIPAL PRODUTOS
# ----------------------------------------------

class HomeProdutoView(TemplateView):
    template_name = "erp/produtos/index.html"


# LISTA DE PRODUTOS
# ----------------------------------------------

class ListaProdutosView(ListView):
    template_name = "erp/produtos/lista.html"
    model = Produto
    context_object_name = "produtos"


# CADASTRAMENTO DE PRODUTOS
# ----------------------------------------------

class CriaProdutoView(CreateView):
    template_name = "erp/produtos/cria.html"
    model = Produto
    form_class = InsereProdutoForm
    success_url = reverse_lazy("erp:lista_produtos")


# ATUALIZAÇÃO DE PRODUTOS
# ----------------------------------------------

class AtualizaProdutoView(UpdateView):
    template_name = "erp/produtos/atualiza.html"
    model = Produto
    fields = '__all__'
    context_object_name = 'produto'
    success_url = reverse_lazy("erp:lista_produtos")


# EXCLUSÃO DE PRODUTOS
# ----------------------------------------------

class DeletaProdutoView(DeleteView):
    template_name = "erp/produtos/exclui.html"
    model = Produto
    context_object_name = 'produto'
    success_url = reverse_lazy("erp:lista_produtos")


# PÁGINA PRINCIPAL VENDAS
# ----------------------------------------------

class HomeVendaView(TemplateView):
    template_name = "erp/vendas/index.html"


# LISTA DE VENDAS
# ----------------------------------------------

class ListaVendasView(ListView):
    template_name = "erp/vendas/lista.html"
    model = Venda
    context_object_name = "vendas"


# CADASTRAMENTO DE VENDAS
# ----------------------------------------------

class CriaVendaView(CreateView):
    template_name = "erp/vendas/cria.html"
    model = Venda
    form_class = InsereVendaForm
    success_url = reverse_lazy("erp:cadastra_venda")


# ATUALIZAÇÃO DE VENDAS
# ----------------------------------------------

class AtualizaVendaView(UpdateView):
    template_name = "erp/vendas/atualiza.html"
    model = Venda
    fields = '__all__'
    context_object_name = 'venda'
    success_url = reverse_lazy("erp:lista_vendas")


# EXCLUSÃO DE VENDAS
# ----------------------------------------------

class DeletaVendaView(DeleteView):
    template_name = "erp/vendas/exclui.html"
    model = Venda
    context_object_name = 'venda'
    success_url = reverse_lazy("erp:lista_vendas")
