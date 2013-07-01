from scrapy.exceptions import DropItem

from agenda.models import Event, Venue, Artist


class ToAgendaDB(object):
    def process_item(self, item, spider):
        # Search for the event in the DB: by title and start time 
        # If already exists: log and add url.
        #    Verify Venue: if different: add as web_watchlist (different venue)
        # If title exist and time 'soon', add as web_watchlist (possible repeat)
        import ipdb; ipdb.set_trace()
        if not item.get('venue'):
            raise DropItem("Venue not found for event %s" % str(item))
        venue, created = Venue.objects.get_or_create(name=item.get('venue'))
        match = False  # flag True if the event exist aand the venue matches.
        good_timing = False #  flag True if the event has same start time.
        event_id = None
        event_query = Event.objects.filter(name=item.get('name'))
        if event_query.exists():
            event = event_query[0]
            event_id = event.id
            match = self.verify_events_venue(event, venue)
            good_timing = self.verify_event_timing(event, item)
            if match and goodtiming:
                raise DropItem("Event exists in DB (id=%s)" % str(event.id))
        else:
            event = self._create_new_event(item, venue,
                                      review_venue=not match,
                                      review_timing=not good_timing)
        item['db_id'] = event.id

        return item

    def verify_events_venue(self,event, venue):
        return event.venue == venue

    def verify_event_timing(self, event, item):
        """Check if the event's start time matches the item's. Return boolean."""
        return True

    def _create_new_event(self, item, venue, review_venue=False, review_timing=False):
        #
        if not item.get('name'):
             raise DropItem("Item with no name found: %s" % item)

        status = Event.WEB_PUBLISHED
        if review_venue or review_timing:
            status = Event.WEB_WATCHLIST

        event = Event.objects.create(name=item.get('name'),
                      description=item.get('description', ''),
                      #email=,
                      photo=item.get('photo', ''),
                      short_description=item.get('short_description', ''),
                      start_time=item.get('start_time', None),
                      end_time=item.get('end_time', None),
                      #artists=,
                      #responsable=,  # Relate to some user... Robot kinda thing
                      venue=venue,
                      tickets=item.get('tickets', ''),
                      )

        artist_name = item.get('artist', '')
        if artist_name:
            artist, created = Artist.get_or_create_artist(name=artist_name)
            event.artist_set.add(artist)
        
        return event


class AddURL(object):
    def process_item(self, item, spider):
        # Link the event with the URL where it was found.
        # url = find_or_create(item.get('url'))
        # event.url_set.add(url)
        return item
