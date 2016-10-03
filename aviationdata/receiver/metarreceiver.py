from . import Receiver

class MetarReceiver(Receiver):
    _url = 'http://tgftp.nws.noaa.gov/pub/data/observations/metar/stations/%s.TXT'

    def receive(self):
        x = super(MetarReceiver, self).receive()
        if x:
            return x
        return []