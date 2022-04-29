import airline
import airport


class Flight:

    def __init__(self, y, m, d, al, fn, oa, da, sd, dt, dd, sa, at, ad):
        self._date = str(y) + '-' + ('0' if len(str(m)) == 1 else '') + \
            str(m) + '-' + ('0' if len(str(d)) == 1 else '') + str(d)
        self._year = y
        self._month = m
        self._day = d
        self._airline = al
        self._flight_num = fn
        self._origin_airport = oa
        self._dest_airport = da
        self._scheduled_departure = sd
        self._departure_time = dt
        self._departure_delay = dd
        self._scheduled_arrival = sa
        self._arrival_time = at
        self._arrival_delay = ad

    def get_date(self):
        return self._date

    def get_year(self):
        return self._year

    def get_month(self):
        return self._month

    def get_day(self):
        return self._day

    def get_airline(self):
        return self._airline

    def get_flight_num(self):
        return self._flight_num

    def get_origin_airport(self):
        return self._origin_airport

    def get_dest_airport(self):
        return self._dest_airport

    def get_scheduled_departure(self):
        return int(self._scheduled_departure)

    def get_departure_time(self):
        return int(self._departure_time)

    def get_departure_delay(self):
        return int(self._departure_delay)

    def get_scheduled_arrival(self):
        return int(self._scheduled_arrival)

    def get_arrival_time(self):
        return int(self._arrival_time)

    def get_arrival_delay(self):
        return int(self._arrival_delay)

    def __repr__(self):
        return '(' + self.get_date() + ", " + self.get_airline().get_code() + ", " + self.get_flight_num() + ", " + self.get_origin_airport().get_code() + ", " + self.get_dest_airport().get_code() + ", " + str(self.get_scheduled_departure()) + ", " + str(self.get_departure_time()) + ", " + str(self.get_departure_delay()) + ", " + str(self.get_scheduled_arrival()) + ", " + str(self.get_arrival_time()) + ", " + str(self.get_arrival_delay()) + ')'
