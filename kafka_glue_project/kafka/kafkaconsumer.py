from kafka import KafkaConsumer
from time import sleep
from json import loads
from s3 import S3FileSystem

# Set the Kafka broker address
bootstrap_servers = [
    "<your_broker_ip>:9092"
]  # Replace <your_broker_ip> with the actual IP address

# Create a Kafka consumer with JSON deserializer
consumer = KafkaConsumer(
    "demo_test",
    bootstrap_servers=bootstrap_servers,
    value_deserializer=lambda x: loads(x.decode("utf-8")),
)

# Uncomment the following lines if you want to print each consumed message
# for message in consumer:
#     print(message.value)

# Create an S3FileSystem object
s3 = S3FileSystem()

# Continue with your code using the 'consumer' and 's3' objects
