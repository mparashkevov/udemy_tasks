from __future__ import annotations

from approved_vehicles import APPROVED_PLATES
from parking_lot import ParkingLot

# Global capacity setting (change here to update default capacity)
PARKING_CAPACITY = 100

# ANSI color codes for menu styling
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"


class ParkingSystemApp:
    # Simple console UI wrapper around ParkingLot
    def __init__(self, capacity: int = PARKING_CAPACITY) -> None:
        self.lot = ParkingLot(capacity=capacity, approved_plates=set(APPROVED_PLATES))

    def run(self) -> None:
        # Main application loop
        while True:
            self._print_menu()
            choice = input("Select an option: ").strip()
            if choice == "1":
                self._handle_park()
            elif choice == "2":
                self._handle_remove()
            elif choice == "3":
                self._show_vehicles_count()
            elif choice == "4":
                self._show_free_spaces()
            elif choice == "5":
                self._show_license_plates()
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

    def _print_menu(self) -> None:
        # Show the menu options
        print(f"\n{BOLD}{CYAN}=== Car Parking System ==={RESET}")
        print(f"{YELLOW}1. Park a vehicle{RESET}")
        print(f"{YELLOW}2. Remove a vehicle{RESET}")
        print(f"{YELLOW}3. Vehicles in the parking{RESET}")
        print(f"{YELLOW}4. Free parking spaces{RESET}")
        print(f"{YELLOW}5. List license plates{RESET}")
        print(f"{RED}0. Exit{RESET}")

    def _handle_park(self) -> None:
        # Park a new vehicle
        plate = input("Enter license plate: ")
        if not self.lot.is_approved(plate):
            print("Car not allowed to park in this parking")
            return
        spot = self.lot.park(plate)
        if spot is not None:
            print("Vehicle parked.")
            self._print_parking_stats()
        else:
            if self.lot.is_full():
                print("Parking is full.")
            else:
                print("Unable to park. Check the license plate or duplication.")

    def _handle_remove(self) -> None:
        # Remove an existing vehicle
        plate = input("Enter license plate to remove: ")
        if self.lot.remove(plate):
            print("Vehicle removed.")
        else:
            print("License plate not found.")

    def _show_vehicles_count(self) -> None:
        # Display number of parked vehicles
        print(f"Vehicles in the parking: {self.lot.occupied_count}")

    def _show_free_spaces(self) -> None:
        # Display remaining free spaces
        print(f"Free parking spaces: {self.lot.free_spaces}")

    def _show_license_plates(self) -> None:
        # Display all stored license plates
        plates = self.lot.list_plates()
        if not plates:
            print("No vehicles parked.")
            return
        print("License plates:")
        for plate in plates:
            print(f"- {plate}")

    def _print_parking_stats(self) -> None:
        # Print summary stats after parking
        print()
        print("=" * 30)
        print("Current parking status:")
        print(f"Free parking spots: {self.lot.free_spaces}/{self.lot.capacity}")
        print("Currently parked vehicles:")
        for spot, plate in self.lot.list_spots():
            print(f"  Spot {spot}: {plate}")
        print(f"Total parked: {self.lot.occupied_count}")
        print("=" * 30)
        print()


def main() -> None:
    app = ParkingSystemApp(capacity=PARKING_CAPACITY)
    app.run()


if __name__ == "__main__":
    main()
