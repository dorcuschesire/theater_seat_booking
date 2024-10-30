# app/seating.py

# Define the seating layout with correct seat counts per row, based on the image.
theater_seating = {
    "Gold": {
        "A": [{"available": True} for _ in range(21)],
        "B": [{"available": True} for _ in range(22)],
        "C": [{"available": True} for _ in range(23)],
        "D": [{"available": True} for _ in range(24)],
        "E": [{"available": True} for _ in range(25)],
        "F": [{"available": True} for _ in range(26)],
    },
    "Silver": {
        "G": [{"available": True} if i != 13 else "S" for i in range(28)],  # Staircase at seat 14
        "H": [{"available": True} if i != 13 else "S" for i in range(30)],  # Staircase at seat 14
        "I": [{"available": True} for _ in range(31)],
        "J": [{"available": True} for _ in range(16)],
    },
    "Bronze": {
        "K": [{"available": True} for _ in range(30)],
        "L": [{"available": True} for _ in range(14)],
        "M": [{"available": True} for _ in range(10)],
        "N": [{"available": True} for _ in range(8)],
        "O": [{"available": True} for _ in range(24)],
        "P": [{"available": True} for _ in range(20)],
        "Q": [{"available": True} for _ in range(8)],
        "R": [{"available": True} for _ in range(2)],
    }
}

# Marking control room seats and staircases in the Bronze section
for i in range(10, 14):
    theater_seating["Bronze"]["O"][i] = "S"  # Control room seats
    theater_seating["Bronze"]["P"][i] = "S"  # Control room seats
for i in range(6, 8):
    theater_seating["Bronze"]["Q"][i] = "S"  # Staircases

def book_seat(section, row, seat_number):
    """Attempt to book a seat in the given section, row, and seat number."""
    try:
        # Check if section exists
        if section not in theater_seating:
            return "Invalid selection: Section does not exist."

        # Check if row exists in the section
        if row not in theater_seating[section]:
            return "Invalid selection: Row does not exist in this section."

        # Check if seat number is within the range for that row
        row_seats = theater_seating[section][row]
        if seat_number < 1 or seat_number > len(row_seats):
            return "Invalid selection: Seat number is out of range for this row."

        # Adjust for zero-indexed list
        seat = row_seats[seat_number - 1]

        # Check if the seat is a staircase or control room seat
        if seat == "S":
            return "Invalid selection: This is a staircase or control room seat."

        # Check if the seat is available
        if seat.get("available", False):
            seat["available"] = False
            return f"Seat {seat_number} in Section {section} Row {row} has been successfully booked."
        else:
            return f"Seat {seat_number} in Section {section} Row {row} is already booked."

    except (KeyError, IndexError):
        # Catch any unexpected errors
        return "An error occurred: Please check section, row, or seat number."
