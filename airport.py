class Airport:

    def __init__(self, co, n, c, s):
        self._code = co
        self._name = n
        self._city = c
        self._state = s
        self._origin_flights = []
        self._dest_flights = []

    def add_origin_flight(self, flight):
        self._origin_flights.append(flight)

    def add_dest_flight(self, flight):
        self._dest_flights.append(flight)

    def __repr__(self):
        return '(' + self._code + ", " + self._name + ", " + self._city + ", " + self._state + ", " + str(len(self._origin_flights)) + ", " + str(len(self._dest_flights)) + ')'

    def get_code(self):
        return self._code

    def get_name(self):
        return self._name

    def get_city(self):
        return self._city

    def get_state(self):
        return self._state

    def get_origin_flights(self):
        return self._origin_flights

    def get_dest_flights(self):
        return self._dest_flights
