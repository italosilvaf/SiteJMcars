from django.template import Library
from utils import utils

register = Library()


@register.filter
def formata_preco(valor):
    return utils.formata_preco(valor)


@register.filter
def formata_preco_admin(valor):
    return utils.formata_preco_admin(valor)


@register.filter
def formata_quilometragem(valor):
    return utils.formata_quilometragem(valor)
