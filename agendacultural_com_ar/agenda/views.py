from django.utils import timezone
from django.views.generic import MonthArchiveView, TemplateView, ListView, DetailView

from agenda.models import Event

class AgendaHomePage(MonthArchiveView):
    allow_empty = True    
    allow_future = True
    date_field = 'start_time'
    date_list_period = 'day'
    http_method_names = [u'get']
    page_kwarg = 'page'
    paginate_by = 10
    queryset = Event.objects.all()
    context_object_name = 'object_list'  
    template_name = "agenda/index.html"

    def get_month(self):
        """
        Return the month for which this view should display data.
        """
        month = self.month
        if month is None:
            try:
                month = self.kwargs['month']
            except KeyError:
                try:
                    month = self.request.GET['month']
                except KeyError:
                    month = timezone.now().strftime('%b')
        return month

    def get_year(self):
        """
        Return the year for which this view should display data.
        """
        year = self.year
        if year is None:
            try:
                year = self.kwargs['year']
            except KeyError:
                try:
                    year = self.request.GET['year']
                except KeyError:
                    year = unicode(timezone.now().year)
        return year

index = AgendaHomePage.as_view()


class EventList(ListView):
    model = Event
    context_object_name = 'events_list'
events = EventList.as_view()


# TODO!
class EventDetails(DetailView):
    model = Event
    pk_url_kwarg = 'event_pk'
event_details = EventDetails.as_view()


# TODO!
class VenueDetails(TemplateView):
    template_name = "agenda/index.html"
venue_details = VenueDetails.as_view()