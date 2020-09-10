from django.db import models
from stdimage import StdImageField
import uuid


def get_file_path(_instance: object, filename: str) -> str:
    """
    Generates a new filename for the uploaded image

    Parameters
    ----------
    _instance : object
        an image
    filename :  str
        an image's filename

    Attributes
    ----------
    ext : str
        file's extension
    """
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'  # uses uuid to generate a new filename
    return filename


class Base(models.Model):
    """
    An abstract class containing common fileds used as a base for the others models

    Attributes
    ----------
    criado : DateField
        the date of creation
    modificado : DateField
        the date of the last modification
    ativo : BooleanField
        state of the item
    """
    criado = models.DateField('Criado', auto_now_add=True)
    modificado = models.DateField('Modificado', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class Servico(Base):
    ICON_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )

    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Ícone', max_length=12, choices=ICON_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self) -> str:
        return f'{self.servico}'


class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self) -> str:
        return f'{self.cargo}'


class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem',
                           upload_to=get_file_path,
                           variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self) -> str:
        return f'{self.nome}'


class Funcionalidade(Base):
    ICON_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-rocket', 'Foguete'),
        ('lni-laptop-phone', 'Responsivo'),
        ('lni-leaf', 'Folha'),
        ('lni-layers', 'Camadas')
    )

    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Ícone', max_length=16, choices=ICON_CHOICES)

    class Meta:
        verbose_name = 'Funcionalidade'
        verbose_name_plural = 'Funcionalidades'

    def __str__(self) -> str:
        return f'{self.nome}'
