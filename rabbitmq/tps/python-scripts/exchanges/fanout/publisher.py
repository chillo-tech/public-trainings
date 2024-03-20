#!/usr/bin/env python3
import pika
import time


# RabbitMQ server connection parameters
rabbitmq_host = 'localhost'
rabbitmq_port = 28572
rabbitmq_channel = None  # To be initialized later
nb_messages=10


# RabbitMQ server connection parameters
exchange_name = 'sa.message.new'

# Create a connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port))
rabbitmq_channel = connection.channel()

# Declare the exchange
#channel.exchange_declare(exchange=rabbitmq_exchange, exchange_type='direct', durable=True)


# Publish 1,000,000 messages
for i in range(1, nb_messages):
    message_body = f'Message {i}'
    
    # Publish the message to the exchange
    rabbitmq_channel.basic_publish(exchange=exchange_name, routing_key='', body=message_body)

# Close the connection
connection.close()

print('All messages published!')
