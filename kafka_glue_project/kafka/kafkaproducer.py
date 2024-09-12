import pandas as pd
from kafka import KafkaProducer
from time import sleep
from json import dumps

# Set the Kafka broker address
bootstrap_servers = [
    "<your_broker_ip>:9092"
]  # Replace <your_broker_ip> with the actual IP address

# Create a Kafka producer with JSON serializer
producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    value_serializer=lambda x: dumps(x).encode("utf-8"),
)

# Send an initial message to 'demo_test' topic
producer.send("demo_test", value={"surname": "paramar"})

# Read data from CSV file
df = pd.read_csv("./indexProcessed.csv")
print(df)

# Display the first few rows of the DataFrame
df.head()

# Continuously send random samples from the DataFrame to Kafka
while True:
    dict_stock = df.sample(1).to_dict(orient="records")[0]
    producer.send("demo_test", value=dict_stock)
    sleep(1)

# Flush the producer to clear data from Kafka server
producer.flush()
