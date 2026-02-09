from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ParkingLot:
    # Total number of parking spaces (easy to adjust)
    capacity: int
    # Map parking spot number -> license plate
    parked_vehicles: dict[int, str] = field(default_factory=dict)
    # Set of approved license plates
    approved_plates: set[str] = field(default_factory=set)

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
        if normalized not in self.approved_plates:
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
