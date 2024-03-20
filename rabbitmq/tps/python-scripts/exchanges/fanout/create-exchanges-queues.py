#!/usr/bin/env python3
import pika

# RabbitMQ server connection parameters
rabbitmq_host = 'localhost'
rabbitmq_port = 28572
rabbitmq_channel = None  # To be initialized later

# List of queue names
quorum_queue_names = ['sa.notification', 'sa.analyses']

# RabbitMQ server connection parameters
exchange_name = 'sa.exchange'
exchange_type='fanout'

# Create a connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port))
rabbitmq_channel = connection.channel()

# Declare the exchange
rabbitmq_channel.exchange_delete(exchange=exchange_name)
rabbitmq_channel.exchange_declare(exchange=exchange_name, exchange_type='fanout')

# Declare quorum queues
for queue_name in quorum_queue_names:
    rabbitmq_channel.queue_declare(queue=queue_name, durable=True)
    print(f'Queue {queue_name} declared successfully.')

    # Bind the quorum queue to the exchange
    rabbitmq_channel.queue_bind(exchange=exchange_name, queue=queue_name)
    print(f'Queue {queue_name} bound to exchange {exchange_name}')

# Close the connection
connection.close()
