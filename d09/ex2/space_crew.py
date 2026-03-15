from enum import Enum
from datetime import datetime
from typing import List
from pydantic import BaseModel, Field, model_validator, ValidationError


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(gt=17, le=80, description="")
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50, description="")
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(gt=0, le=3650, description="")
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def mission_validation_rules(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        for member in self.crew:
            if not member.is_active:
                raise ValueError("All crew members must be active")
        has_leader = any(
            member.rank in [Rank.COMMANDER, Rank.CAPTAIN]
            for member in self.crew)
        if not has_leader:
            raise ValueError(
                             "Mission must have at least one Commander or "
                             "Captain")
        if (self.duration_days > 365):
            for member in self.crew:
                if member.years_experience < 5:
                    raise ValueError("Long missions (> 365 days) require at "
                                     "least 5 years of experience for all crew"
                                     " members")
        return self


def main() -> None:
    print("Space Mission Crew Validation")

    print("=========================================")
    print("Valid mission created:")
    member1 = CrewMember(
        member_id="SC_MC3",
        name="Sarah Connor",
        rank=Rank.COMMANDER,
        age=33,
        specialization="Mission Command",
        years_experience=12
    )
    member2 = CrewMember(
        member_id="JS_N5",
        name="John Smith",
        rank=Rank.LIEUTENANT,
        age=28,
        specialization="Navigation",
        years_experience=6
    )
    member3 = CrewMember(
        member_id="AJ_E2",
        name="Alice Johnson",
        rank=Rank.OFFICER,
        age=39,
        specialization="Engineering",
        years_experience=14
    )
    member4 = CrewMember(
        member_id="AJ_E2",
        name="Leon Denir",
        rank=Rank.LIEUTENANT,
        age=26,
        specialization="Navigation",
        years_experience=3
    )
    mission1 = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date="2024-10-27T12:00:00",
        duration_days=900,
        budget_millions=2500.0,
        crew=[member1, member2, member3]
    )

    print(f"Mission: {mission1.mission_name}")
    print(f"ID: {mission1.mission_id}")
    print(f"Destination: {mission1.destination}")
    print(f"Duration: {mission1.duration_days} days")
    print(f"Budget: ${mission1.budget_millions}M")
    print(f"Crew size: {len(mission1.crew)}")
    print("Crew members:")
    print(f"- {member1.name} ({member1.rank.value}) - "
          f"{member1.specialization}")
    print(f"- {member2.name} ({member2.rank.value}) - "
          f"{member2.specialization}")
    print(f"- {member3.name} ({member3.rank.value}) - "
          f"{member3.specialization}")

    print("\n=========================================")
    print("Expected validation error:")

    try:
        mission2 = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2024-11-27T12:00:00",
            duration_days=900,
            budget_millions=2500.0,
            crew=[member2, member3, member4]
        )
        print(f"ID: {mission2.mission_id}")

    except ValidationError as e:
        raw_msg = e.errors()[0]['msg']
        msg = raw_msg.replace("Value error, ", "")
        print(msg)


if __name__ == "__main__":
    main()
