from core.models import Funcionario, Produto, Venda
from django import forms


# FORMULÁRIO DE INCLUSÃO DE FUNCIONÁRIOS
# -------------------------------------------

class InsereFuncionarioForm(forms.ModelForm):

    chefe = forms.BooleanField(
        label='Chefe?',
        required=False,
    )

    biografia = forms.CharField(
        label='Biografia',
        required=False,
        widget=forms.Textarea
    )

    class Meta:
        # Modelo base
        model = Funcionario

        # Campos que estarão no form
        fields = [
            'nome',
            'sobrenome',
            'cpf',
            'tempo_de_servico',
            'remuneracao'
        ]


# FORMULÁRIO DE INCLUSÃO DE Produtos
# -------------------------------------------

class InsereProdutoForm(forms.ModelForm):
    descricao = forms.CharField(
        label='Descrição',
        required=True,
        widget=forms.Textarea
    )

    class Meta:
        # Modelo base
        model = Produto

        # Campos que estarão no form
        fields = [
            'nome',
            'descricao',
            'preco'
        ]


# FORMULÁRIO DE INCLUSÃO DE Vendas
# -------------------------------------------

class InsereVendaForm(forms.ModelForm):
    class Meta:
        # Modelo base
        model = Venda

        # Campos que estarão no form
        fields = [
            'funcionario',
            'produto'
        ]
