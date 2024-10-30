# run.py

from app.seating import book_seat

def main():
    print("Welcome to the Theater Booking System")
    while True:
        # Prompt user for booking details
        section = input("Enter Section (Gold, Silver, Bronze): ").strip().capitalize()
        row = input("Enter Row (A, B, C, etc.): ").strip().upper()
        
        try:
            seat_number = int(input("Enter Seat Number: ").strip())
        except ValueError:
            print("Invalid input: Seat number must be an integer.")
            continue  # Skip to the next iteration to ask again

        # Debugging print statements
        print(f"DEBUG: Section = '{section}', Row = '{row}', Seat Number = {seat_number}")
        
        # Attempt to book the seat and display result
        result = book_seat(section, row, seat_number)
        print(result)

        # Ask if the user wants to book another seat
        cont = input("Do you want to book another seat? (y/n): ").strip().lower()
        if cont != 'y':
            print("Thank you for using the Theater Booking System!")
            break

if __name__ == "__main__":
    main()
