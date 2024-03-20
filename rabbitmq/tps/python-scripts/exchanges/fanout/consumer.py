#!/usr/bin/env python3
import pika
import time
# Callback function to handle incoming messages
def callback(ch, method, properties, body):
    print("Received message:", body.decode())

# RabbitMQ server connection parameters
rabbitmq_host = 'localhost'
rabbitmq_port = 28572
rabbitmq_channel = None  # To be initialized later

# List of queue names
quorum_queue_names = ['messages.notification', 'messages.analysis', 'messages.send']

# Create a connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port))
rabbitmq_channel = connection.channel()

# Declare quorum queues
for queue_name in quorum_queue_names:
    rabbitmq_channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print("Waiting for messages. To exit press CTRL+C")

# Start consuming messages
rabbitmq_channel.start_consuming()