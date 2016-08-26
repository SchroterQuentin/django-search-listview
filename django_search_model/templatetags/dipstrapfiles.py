from django import template
from django.conf import settings
from django.templatetags.static import StaticNode, PrefixNode, urljoin


register = template.Library()


class DipstrapNode(StaticNode):

    @classmethod
    def handle_simple(cls, path):
        static_dipstrap = getattr(settings, 'DIPSTRAP_STATIC_URL', '')
        if static_dipstrap:
            return urljoin(PrefixNode.handle_simple('DIPSTRAP_STATIC_URL'),
                           path)
        else:
            return super(DipstrapNode, cls).handle_simple(path)


@register.tag(name='dipstrap')
def do_dipstrap(parser, token):
    return DipstrapNode.handle_token(parser, token)


def dipstrap(path):
    return DipstrapNode.handle_simple(path)
