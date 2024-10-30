# tests/test_seating.py

import unittest
from app.seating import book_seat, theater_seating

class TestSeating(unittest.TestCase):
    def setUp(self):
        # Reset theater seating for each test to avoid interference between tests
        for section in theater_seating:
            for row in theater_seating[section]:
                for seat in theater_seating[section][row]:
                    if isinstance(seat, dict):
                        seat["available"] = True

    def test_valid_booking(self):
        result = book_seat("Gold", "A", 1)
        self.assertEqual(result, "Seat 1 in Section Gold Row A has been successfully booked.")
        # Verify seat is no longer available
        self.assertFalse(theater_seating["Gold"]["A"][0]["available"])

    def test_rebooking(self):
        book_seat("Gold", "A", 1)
        result = book_seat("Gold", "A", 1)
        self.assertEqual(result, "Seat 1 in Section Gold Row A is already booked.")

    def test_staircase_selection(self):
        result = book_seat("Silver", "G", 14)  # Assuming "G14" is a staircase
        self.assertEqual(result, "Invalid selection: This is a staircase.")

    def test_invalid_selection(self):
        result = book_seat("Gold", "A", 100)  # Out of range seat number
        self.assertEqual(result, "Invalid selection: Please check section, row, or seat number.")

if __name__ == "__main__":
    unittest.main()
