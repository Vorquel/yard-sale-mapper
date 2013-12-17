from django.core.management.base import BaseCommand, CommandError

#the following is equivalent to from yard-sale-mapper.models import Yardsale, Distance
#or it would be, if identifiers could have dashes. 
_temp = __import__('yard-sale-mapper.models', globals(), locals(), ['Yardsale', 'Distance'], -1)
Yardsale = _temp.Yardsale
Distance = _temp.Distance

class Command(BaseCommand):
    help = 'retrieves new yardsales from the internet'
    def handle(self, *args, **options):
        #doto: write a screen-scraper for ksl here
        self.stdout.write('test')

