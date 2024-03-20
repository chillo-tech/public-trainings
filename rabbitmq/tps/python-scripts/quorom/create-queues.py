#!/usr/bin/env python3
import pika

# RabbitMQ server connection parameters
rabbitmq_host = 'localhost'
rabbitmq_port = 29562
rabbitmq_channel = None  # To be initialized later

# List of quorum queue names
quorum_queue_names = ['quorum_queue_1', 'quorum_queue_2', 'quorum_queue_3']
#quorum_queue_names = ['classic_queue_1', 'classic_queue_2', 'classic_queue_3']

# RabbitMQ server connection parameters
exchange_name = 'cluster.exchange'
routing_key = '1'

# Create a connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port))
rabbitmq_channel = connection.channel()

# Declare the exchange
rabbitmq_channel.exchange_delete(exchange=exchange_name)
rabbitmq_channel.exchange_declare(exchange=exchange_name, exchange_type='x-consistent-hash', durable=True)

# Declare quorum queues
for queue_name in quorum_queue_names:
    rabbitmq_channel.queue_declare(queue=queue_name, durable=True, arguments={'x-queue-type': 'quorum'})
    #rabbitmq_channel.queue_declare(queue=queue_name, durable=True)
    rabbitmq_channel.exchange_delete(exchange=queue_name)
    print(f'Quorum queue {queue_name} declared successfully.')

    # Bind the quorum queue to the exchange
    rabbitmq_channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)
    print(f'Quorum queue {queue_name} bound to exchange {exchange_name} with routing key {routing_key}.')

# Close the connection
connection.close()
