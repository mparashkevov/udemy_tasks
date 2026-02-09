from __future__ import annotations

from dataclasses import dataclass, field

# Global capacity setting (change here to update default capacity)
PARKING_CAPACITY = 100

# ANSI color codes for menu styling
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"


@dataclass
class ParkingLot:
    # Total number of parking spaces (easy to adjust)
    capacity: int = PARKING_CAPACITY
    # Map parking spot number -> license plate
    parked_vehicles: dict[int, str] = field(default_factory=dict)

    @property
    def occupied_count(self) -> int:
        # Number of vehicles currently parked
        return len(self.parked_vehicles)

    @property
    def free_spaces(self) -> int:
        # Remaining available spaces
        return self.capacity - self.occupied_count

    def is_full(self) -> bool:
        # Check if the parking lot is full
        return self.occupied_count >= self.capacity

    def park(self, license_plate: str) -> int | None:
        # Normalize plate input for consistent storage
        normalized = license_plate.strip().upper()
        if not normalized:
            return None
        if self.is_full():
            return None
        if normalized in self.parked_vehicles.values():
            return None
        spot = self._next_available_spot()
        if spot is None:
            return None
        self.parked_vehicles[spot] = normalized
        return spot

    def remove(self, license_plate: str) -> bool:
        # Remove a vehicle by plate if present
        normalized = license_plate.strip().upper()
        for spot, plate in list(self.parked_vehicles.items()):
            if plate == normalized:
                del self.parked_vehicles[spot]
                return True
        return False

    def list_plates(self) -> list[str]:
        # Return plates in alphabetical order
        return sorted(self.parked_vehicles.values())

    def list_spots(self) -> list[tuple[int, str]]:
        # Return (spot, plate) sorted by spot number
        return sorted(self.parked_vehicles.items())

    def _next_available_spot(self) -> int | None:
        # Find the smallest available spot number
        for spot in range(1, self.capacity + 1):
            if spot not in self.parked_vehicles:
                return spot
        return None


class ParkingSystemApp:
    # Simple console UI wrapper around ParkingLot
    def __init__(self, capacity: int = PARKING_CAPACITY) -> None:
        self.lot = ParkingLot(capacity=capacity)

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


if __name__ == "__main__":
    # Start the app with default capacity (adjust if needed)
    app = ParkingSystemApp(capacity=PARKING_CAPACITY)
    app.run()
