from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(
        min_length=3, max_length=10, description="characters")
    name: str = Field(min_length=1, max_length=50, description="characters")
    crew_size: int = Field(ge=1, le=20, description="people")
    power_level: float = Field(ge=0.0, le=100.0, description="%")
    oxygen_level: float = Field(ge=0.0, le=100.0, description="%")
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(
        default=None, max_length=200, description="characters")


def main() -> None:
    print("Space Station Data Validation")

    print("========================================")
    print("Valid station created:")

    station1 = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance="2024-10-27T12:00:00",
        is_operational=True
    )

    desc1 = SpaceStation.model_fields['crew_size'].description
    desc2 = SpaceStation.model_fields['power_level'].description
    desc3 = SpaceStation.model_fields['oxygen_level'].description

    print(f"ID: {station1.station_id}")
    print(f"Name: {station1.name}")
    print(f"Crew: {station1.crew_size} {desc1}")
    print(f"Power: {station1.power_level}{desc2}")
    print(f"Oxygen: {station1.oxygen_level}{desc3}")
    if station1.is_operational:
        print("Status: Operational")

    print("\n========================================")
    print("Expected validation error:")

    try:
        station2 = SpaceStation(
            station_id="ISS002",
            name="International Space Station",
            crew_size=21,
            power_level=98.3,
            oxygen_level=89.5,
            last_maintenance="2024-11-27T12:00:00",
            is_operational=False
        )

        print(f"ID: {station2.station_id}")

    except ValidationError as e:
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
