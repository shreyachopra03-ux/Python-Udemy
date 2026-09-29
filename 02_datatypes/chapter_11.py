import arrow
from collections import namedtuple

brewing_time = arrow.utcnow()
brewing_time.to("Europe/Rome")

chaiProfile = namedtuple("chaiProfile", ["aroma", "taste", "size"])