from django.shortcuts import render
from django.http import HttpResponse
import pika

def publish_message(request):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='your_queue_name', durable=True)  # Adjust the 'durable' parameter as needed
    # channel.queue_declare(queue='your_queue_name')
    channel.basic_publish(exchange='', routing_key='your_queue_name', body='Hello, RabbitMQ!')

    connection.close()

    return HttpResponse("Message published to RabbitMQ!")

