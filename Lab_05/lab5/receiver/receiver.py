from kafka import KafkaConsumer

bootstrap_servers = 'kafka:9092'
topic = 'common'

consumer = KafkaConsumer(topic, bootstrap_servers=bootstrap_servers, api_version=(2, 7, 0))

for message in consumer:
    print(f"Received message: {message.value.decode('utf-8')}")
    