from django.test import TestCase
from model_bakery import baker
import uuid

from core.models import get_file_path


# testCase da função get_file_path
class GetFilePathTestCase(TestCase):
    def setUp(self) -> None:
        self.filename = f'{uuid.uuid4()}.png'

    def test_get_file_path(self) -> None:
        arquivo = get_file_path(None, 'teste.png')
        self.assertTrue(len(arquivo), len(self.filename))


# testCase da classe Servico
class ServicoTestCase(TestCase):
    def setUp(self) -> None:
        self.servico = baker.make('Servico')

    def test_str(self) -> None:
        self.assertEquals(str(self.servico), self.servico.servico)


# testCase da classe Cargo
class CargoTestCase(TestCase):
    def setUp(self) -> None:
        self.cargo = baker.make('Cargo')

    def test_str(self) -> None:
        self.assertEquals(str(self.cargo), self.cargo.cargo)


# testCase da classe Funcionario
class FuncionarioTestCase(TestCase):
    def setUp(self) -> None:
        self.funcionario = baker.make('Funcionario')

    def test_str(self) -> None:
        self.assertEquals(str(self.funcionario), self.funcionario.nome)


# testCase da classe Funcionalidade - criada no desafio
class FuncionalidadeTestCase(TestCase):
    def setUp(self) -> None:
        self.funcionalidade = baker.make('Funcionalidade')

    def test_str(self) -> None:
        self.assertEquals(str(self.funcionalidade), self.funcionalidade.nome)
