from pydantic import BaseModel

class Booking(BaseModel):
    user_id: int
    event_id: int
    seat_number: str

