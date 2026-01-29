from ticket import Ticket
from utils import save_ticket, read_tickets, update_status, search_ticket


def assign_priority(description):
    desc = description.lower()

    if "urgent" in desc or "immediately" in desc:
        return "High"
    elif "slow" in desc or "delay" in desc:
        return "Medium"
    else:
        return "Low"


def create_ticket():
    ticket_id = input("Enter Ticket ID: ")
    description = input("Enter problem description: ")

    priority = assign_priority(description)
    ticket = Ticket(ticket_id, description, priority)

    save_ticket(ticket)
    print("\nTicket created successfully!")
    print("Assigned Priority:", priority)


def view_tickets():
    tickets = read_tickets()

    if not tickets:
        print("\nNo tickets available.")
        return

    print("\n--- All Tickets ---")
    for t in tickets:
        print(f"ID: {t[0]} | Desc: {t[1]} | Priority: {t[2]} | Status: {t[3]}")


def change_status():
    ticket_id = input("Enter Ticket ID: ")

    print("\n1. Open\n2. In Progress\n3. Closed")
    choice = input("Select new status: ")

    status_map = {
        "1": "Open",
        "2": "In Progress",
        "3": "Closed"
    }

    if choice not in status_map:
        print("Invalid status choice.")
        return

    if update_status(ticket_id, status_map[choice]):
        print("Ticket status updated successfully.")
    else:
        print("Ticket not found.")


def track_ticket():
    ticket_id = input("Enter Ticket ID to track: ")
    ticket = search_ticket(ticket_id)

    if ticket:
        print("\n--- Ticket Tracking Result ---")
        print("Ticket ID     :", ticket[0])
        print("Description   :", ticket[1])
        print("Priority      :", ticket[2])
        print("Current Status:", ticket[3])
    else:
        print("Ticket not found.")


def main():
    while True:
        print("\nCustomer Support Ticket System")
        print("1. Create Ticket")
        print("2. View Tickets")
        print("3. Update Ticket Status")
        print("4. Track Ticket")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_ticket()
        elif choice == "2":
            view_tickets()
        elif choice == "3":
            change_status()
        elif choice == "4":
            track_ticket()
        elif choice == "5":
            print("Thank you for using the system.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
