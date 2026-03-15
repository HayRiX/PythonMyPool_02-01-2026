from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, model_validator, ValidationError


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(
        min_length=5, max_length=15, description="characters")
    timestamp: datetime
    location: str = Field(
        min_length=3, max_length=100, description="characters")
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0, description="/10")
    duration_minutes: int = Field(gt=0, le=1440, description="(max 24 hours)")
    witness_count: int = Field(gt=0, lt=101, description="people")
    message_received: Optional[str] = Field(default=None,
                                            max_length=500,
                                            description="characters")
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def custom_validation_rules(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if (self.contact_type == ContactType.PHYSICAL
           and not self.is_verified):
            raise ValueError("Physical contact reports must be verified")
        if (self.contact_type == ContactType.TELEPATHIC and
           self.witness_count < 3):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages")
        return self


def main() -> None:
    print("Alien Contact Log Validation")

    print("======================================")
    print("Valid contact report:")

    contact1 = AlienContact(
        contact_id="AC_2024_001",
        location="Area 51, Nevada",
        contact_type=ContactType.RADIO,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        is_verified=True,
        message_received="'Greetings from Zeta Reticuli'",
        timestamp="2024-10-27T12:00:00"
    )

    desc1 = AlienContact.model_fields['signal_strength'].description

    print(f"ID: {contact1.contact_id}")
    print(f"Type: {contact1.contact_type.value}")
    print(f"Location: {contact1.location}")
    print(f"Signal: {contact1.signal_strength}{desc1}")
    print(f"Duration: {contact1.duration_minutes} minutes")
    print(f"Witnesses: {contact1.witness_count}")
    print(f"Message: {contact1.message_received}")

    print("\n======================================")
    print("Expected validation error:")

    try:
        contact2 = AlienContact(
            contact_id="AC_2024_002",
            location="Area 51, Nevada",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=6,
            duration_minutes=45,
            witness_count=2,
            is_verified=True,
            message_received="'Greetings from Zeta Reticuli'",
            timestamp="2024-11-27T12:00:00"
        )

        print(f"ID: {contact2.contact_id}")

    except ValidationError as e:
        raw_msg = e.errors()[0]['msg']
        msg = raw_msg.replace("Value error, ", "")
        print(msg)


if __name__ == "__main__":
    main()
