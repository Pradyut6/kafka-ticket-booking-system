import requests

def test_booking_endpoint():
    payload = {
        "user_id": 1,
        "event_id": 101,
        "seat_number": "A15"
    }
    r = requests.post("http://localhost:8000/book", json=payload)
    assert r.status_code == 200
    assert r.json()["status"] == "Booking event sent to Kafka"

