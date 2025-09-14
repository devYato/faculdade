
class Evento(object):
    def __init__(self, name: str, date: str, location: str, description: str = ""):
        self.name = name
        self.date = date
        self.location = location
        self.description = description

class Participantes(object):
    def __init__(self, event_id: int, name: str, email: str, registration_date: str):
        self.event_id = event_id
        self.name = name
        self.email = email
        self.registration_date = registration_date