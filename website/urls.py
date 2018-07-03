from website.views import IndexTemplateView, FuncionarioListView, FuncionarioUpdateView, FuncionarioCreateView, \
    FuncionarioDeleteView

from django.urls import path

app_name = 'website'

urlpatterns = [
    # GET /
    path('', IndexTemplateView.as_view(), name="index"),

    # GET /funcionario/cadastrar
    path('funcionario/cadastrar', FuncionarioCreateView.as_view(), name="cadastra_funcionario"),

    # GET /funcionarios
    path('funcionarios/', FuncionarioListView.as_view(), name="lista_funcionarios"),

    # GET/POST /funcionario/{pk}
    path('funcionario/<pk>', FuncionarioUpdateView.as_view(), name="atualiza_funcionario"),

    # GET/POST /funcionarios/excluir/{pk}
    path('funcionario/excluir/<pk>', FuncionarioDeleteView.as_view(), name="deleta_funcionario"),
]
