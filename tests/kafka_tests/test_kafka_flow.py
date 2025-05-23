from kafka import KafkaProducer, KafkaConsumer
import json

def test_kafka_send_receive():
    topic = "booking_topic"
    msg = {"test": "message"}

    producer = KafkaProducer(
        bootstrap_servers="localhost:9092",
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    producer.send(topic, msg)
    producer.flush()

    consumer = KafkaConsumer(
        topic,
        bootstrap_servers="localhost:9092",
        auto_offset_reset='earliest',
        consumer_timeout_ms=1000,
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )

    messages = [msg.value for msg in consumer]
    assert {"test": "message"} in messages

