from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe


register = template.Library()


def _conditional_escape(autoescape):
    """"""
    if autoescape:
        return conditional_escape
    else:
        return lambda x: x


def _get_nice_link(entity, autoescape=None):
    """Get an HTML anchor element linking to this entity's detailed view."""

    esc = _conditional_escape(autoescape)
    return mark_safe('<a href="%s">%s</a>'%(entity.get_absolute_url(),
                                            esc(unicode(entity))))
register.filter('get_nice_link', _get_nice_link, needs_autoescape=True)


@register.filter(needs_autoescape=True)
def event_widget(event, autoescape=None):
    """Render an HTML snippet with an event's info."""
    snippet = ''
    if event:
        esc = _conditional_escape(autoescape)
        snippet = "<p>%s<br><b>%s</b> en <i>%s</i></p>"%(
                esc(unicode(event.start_time)),
                _get_nice_link(event, autoescape),
                _get_nice_link(event.venue, autoescape),)

    return mark_safe(snippet)
