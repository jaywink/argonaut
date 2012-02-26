from datetime import tzinfo, datetime, timedelta

class GMT2(tzinfo):   # copied from http://docs.python.org/library/datetime.html
	def __init__(self):
		dt = datetime.now()
		d = datetime(dt.year, 4, 1)
		self.dston = d - timedelta(days=d.weekday() + 1)
		d = datetime(dt.year, 11, 1)
		self.dstoff = d - timedelta(days=d.weekday() + 1)
	def utcoffset(self, dt):
		return timedelta(hours=1) + self.dst(dt)
	def dst(self, dt):
		if self.dston <=  dt.replace(tzinfo=None) < self.dstoff:
			return timedelta(hours=2)
		else:
			return timedelta(0)
	def tzname(self,dt):
		return "GMT +2"

def now():
	tz = GMT2()
	now = datetime.now(tz)
	return now
