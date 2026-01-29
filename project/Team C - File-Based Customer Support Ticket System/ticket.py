class Ticket:
    def __init__(self, ticket_id, description, priority, status="Open"):
        self.ticket_id = ticket_id
        self.description = description
        self.priority = priority
        self.status = status

    def to_list(self):
        return [self.ticket_id, self.description, self.priority, self.status]
