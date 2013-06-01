from django.views.generic import TemplateView, ListView
from agenda.models import Event

class AgendaHomePage(TemplateView):
    template_name = "agenda/index.html"
index = AgendaHomePage.as_view()


class EventList(ListView):
    model = Event
    context_object_name = 'events_list'
events = EventList.as_view()


# TODO!
class EventDetails(TemplateView):
    template_name = "agenda/index.html"
event_details = EventDetails.as_view()


# TODO!
class VenueDetails(TemplateView):
    template_name = "agenda/index.html"
venue_details = VenueDetails.as_view()