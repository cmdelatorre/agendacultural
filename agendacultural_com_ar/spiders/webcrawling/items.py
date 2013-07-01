"""Items scraped from the Vos site."""

from scrapy.item import Item, Field


class Event(Item):
	"""An event in the Vos site."""
	url = Field()
	name = Field()
	description = Field()
	photo = Field()
	short_description = Field()
	start_time = Field()
	end_time = Field()
	artists = Field()
	venue = Field()
	tickets = Field()
	db_id = Field()