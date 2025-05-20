class Client:
    def __init__(self, name):
        self.name = name
        self._bookings = []


    def add_booking(self, bookings):
        self._bookings.append(bookings)

    def get_bookings(self):
        return self._bookings

    def get_name(self):
        return self.name

