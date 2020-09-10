from django.views.generic import TemplateView
from .models import Funcionalidade, Funcionario, Servico


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.all()
        context['funcionarios'] = Funcionario.objects.all()
        context['funcionalidades'] = Funcionalidade.objects.all()

        return context
