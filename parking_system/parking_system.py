from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ParkingLot:
    # Total number of parking spaces (easy to adjust)
    capacity: int = 100
    # Keep unique license plates of parked vehicles
    parked_vehicles: set[str] = field(default_factory=set)

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

    def park(self, license_plate: str) -> bool:
        # Normalize plate input for consistent storage
        normalized = license_plate.strip().upper()
        if not normalized:
            return False
        if self.is_full():
            return False
        if normalized in self.parked_vehicles:
            return False
        self.parked_vehicles.add(normalized)
        return True

    def remove(self, license_plate: str) -> bool:
        # Remove a vehicle by plate if present
        normalized = license_plate.strip().upper()
        if normalized in self.parked_vehicles:
            self.parked_vehicles.remove(normalized)
            return True
        return False

    def list_plates(self) -> list[str]:
        # Return plates in alphabetical order
        return sorted(self.parked_vehicles)


class ParkingSystemApp:
    # Simple console UI wrapper around ParkingLot
    def __init__(self, capacity: int = 100) -> None:
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
        print("\n=== Car Parking System ===")
        print("1. Park a vehicle")
        print("2. Remove a vehicle")
        print("3. Vehicles in the parking")
        print("4. Free parking spaces")
        print("5. List license plates")
        print("0. Exit")

    def _handle_park(self) -> None:
        # Park a new vehicle
        plate = input("Enter license plate: ")
        if self.lot.park(plate):
            print("Vehicle parked.")
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


if __name__ == "__main__":
    # Start the app with default capacity (adjust if needed)
    app = ParkingSystemApp(capacity=100)
    app.run()
