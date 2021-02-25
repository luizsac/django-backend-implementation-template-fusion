from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext as _
from django.utils import translation
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
        context['lang'] = translation.get_language()  # pega idioma do navegador
        translation.activate(context['lang'])  # altera o idioma da aplicação para o idioma do navegador, se disponível
        return context

    # é chamado se o formulário for válido
    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, _('E-mail enviado com sucesso!'))
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    # é chamado se o formulário for inválido
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, _('Erro ao enviar e-mail'))
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
