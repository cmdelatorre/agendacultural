from django.views.generic import TemplateView


class AgendaHomePage(TemplateView):

    template_name = "agenda/index.html"

index = AgendaHomePage.as_view()
