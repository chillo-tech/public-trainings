#!/usr/bin/env python
import os
import pika
import sys
import time


def main():

    # RabbitMQ server connection parameters
    rabbitmq_host = 'localhost'
    rabbitmq_port = 29561
    rabbitmq_exchange = 'sharded.exchannge'
    rabbitmq_routing_key = '1'
    nb_messages = 1000000
    # Create a connection to RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port))
    channel = connection.channel()

    # Declare the exchange
    # channel.exchange_declare(exchange=rabbitmq_exchange, exchange_type='direct')

    # Publish 1,000,000 messages
    for i in range(1, nb_messages):
        message_body = f'Message {i}'
        
        # Publish the message to the exchange
        channel.basic_publish(exchange=rabbitmq_exchange, routing_key=rabbitmq_routing_key, body=message_body)
        # time.sleep(5)
        #if i % 1000 == 0:
        #    print(f'Published {i} messages')

    # Close the connection
    connection.close()

    print('All messages published!')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)