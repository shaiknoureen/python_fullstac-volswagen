import csv
import os

FILE_NAME = "tickets.csv"
HEADERS = ["Ticket ID", "Description", "Priority", "Status"]


def save_ticket(ticket):
    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(HEADERS)
        writer.writerow(ticket.to_list())


def read_tickets():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader, None)
        return list(reader)


def update_status(ticket_id, new_status):
    tickets = read_tickets()
    updated = False

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(HEADERS)

        for t in tickets:
            if t[0] == ticket_id:
                t[3] = new_status
                updated = True
            writer.writerow(t)

    return updated


def search_ticket(ticket_id):
    tickets = read_tickets()

    for t in tickets:
        if t[0] == ticket_id:
            return t

    return None
