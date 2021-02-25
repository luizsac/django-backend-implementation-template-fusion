from django.db import models
from django.utils.translation import gettext_lazy as _
from stdimage import StdImageField
import uuid

# a documentação desse arquivo está em inglês por nenhuma razão

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
    criado = models.DateField(_('Criado'), auto_now_add=True)
    modificado = models.DateField(_('Modificado'), auto_now=True)
    ativo = models.BooleanField(_('Ativo'), default=True)

    class Meta:
        abstract = True


class Servico(Base):
    """
    Represents the Services offered by the company

    Attributes
    ----------
    ICON-CHOICES : tuple
        contains the bootstrap icon classes to represent the services visually
    servico : CharField
        name of the service
    descricao : TextField
        description of the service
    icone : Charfield
        the chosen icon from the tuple of icons
    """
    ICON_CHOICES = (
        ('lni-cog', _('Engrenagem')),
        ('lni-stats-up', _('Gráfico')),
        ('lni-users', _('Usuários')),
        ('lni-layers', _('Design')),
        ('lni-mobile', _('Mobile')),
        ('lni-rocket', _('Foguete')),
    )

    servico = models.CharField(_('Serviço'), max_length=100)
    descricao = models.TextField(_('Descrição'), max_length=200)
    icone = models.CharField(_('Ícone'), max_length=12, choices=ICON_CHOICES)

    class Meta:
        verbose_name = _('Serviço')
        verbose_name_plural = _('Serviços')

    def __str__(self) -> str:
        return f'{self.servico}'


class Cargo(Base):
    """
    Represents the positions of the employees of the company

    Attributes
    ----------
    cargo : CharField
        name of the position
    """
    cargo = models.CharField(_('Cargo'), max_length=100)

    class Meta:
        verbose_name = _('Cargo')
        verbose_name_plural = _('Cargos')

    def __str__(self) -> str:
        return f'{self.cargo}'


class Funcionario(Base):
    """
        Represents an employees of the company

        Attributes
        ----------
        nome : CharField
            employee's name
        cargo : ForeignKey
            employee's position
        bio : TextField
            employee's biography
        imagem : StdImageField
            employee's photograph
        facebook : CharField
            employee's facebook page
        twitter : CharField
            employee's twitter page
        instagram : CharField
            employee's instagram page
        """
    nome = models.CharField(_('Nome'), max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name=_('Cargo'), on_delete=models.CASCADE)
    bio = models.TextField(_('Bio'), max_length=200)
    imagem = StdImageField(_('Imagem'),
                           upload_to=get_file_path,
                           variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = _('Funcionário')
        verbose_name_plural = _('Funcionários')

    def __str__(self) -> str:
        return f'{self.nome}'


class Funcionalidade(Base):
    """
        Represents a feature of the system

        Attributes
        ----------
        ICON_CHOICES : tuple
            contains the bootstrap icon classes to represent the features visually
        nome : CharField
            name of the feature
        descricao : CharField
            description of the feature
        icone : CharField
            the chosen icon from the tuple of icons
        """
    ICON_CHOICES = (
        ('lni-cog', _('Engrenagem')),
        ('lni-rocket', _('Foguete')),
        ('lni-laptop-phone', _('Responsivo')),
        ('lni-leaf', _('Folha')),
        ('lni-layers', _('Camadas'))
    )

    nome = models.CharField(_('Nome'), max_length=100)
    descricao = models.TextField(_('Descrição'), max_length=200)
    icone = models.CharField(_('Ícone'), max_length=16, choices=ICON_CHOICES)

    class Meta:
        verbose_name = _('Funcionalidade')
        verbose_name_plural = _('Funcionalidades')

    def __str__(self) -> str:
        return f'{self.nome}'
