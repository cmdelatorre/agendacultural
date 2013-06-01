from django import template
from django.template.loader import render_to_string
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe


register = template.Library()


def _conditional_escape(autoescape):
    """"""
    if autoescape:
        return conditional_escape
    else:
        return lambda x: x


def _get_nice_link(entity, upper=None, autoescape=None):
    """Get an HTML anchor element linking to this entity's detailed view."""

    esc = _conditional_escape(autoescape)
    name = unicode(entity)
    if upper:
        name = name.upper()
    return mark_safe('<a href="%s">%s</a>'%(entity.get_absolute_url(),
                                            esc(name)))
register.filter('get_nice_link', _get_nice_link, needs_autoescape=True)


@register.filter
def event_widget(event):
    """Render an HTML snippet with an event's info."""
    if not event:
        return ''
    return mark_safe(render_to_string('agenda/event_summary_widget.html', 
                                      dictionary={'event': event}))
