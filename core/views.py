from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContatoForm
from .models import Funcionalidade, Funcionario, Servico


class IndexView(FormView):  # trabalhando com forms - herda as mesmas características de TemplateView
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')  # se o formulário for submetido com sucesso, redirecionar para index

    def get_context_data(self, **kwargs) -> dict:
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.all()
        context['funcionarios'] = Funcionario.objects.all()
        context['funcionalidades'] = Funcionalidade.objects.all()

        return context

    # é chamado se o formulário for válido
    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    # é chamado se o formulário for inválido
    def form_invalid(self, form, *args, **kwargs):
        print('FORMULÁRIO É INVÁLIDO')
        messages.error(self.request, 'Erro ao enviar e-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
