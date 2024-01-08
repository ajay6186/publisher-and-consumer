from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import pika

def consume_message(request):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='your_queue_name', durable=True)  # Adjust the 'durable' parameter as needed
    
    def callback(ch, method, properties, body):
        print(f"Received message: {body}")

    channel.basic_consume(queue='your_queue_name', on_message_callback=callback, auto_ack=True)

    print("Waiting for messages. To exit, press CTRL+C")
    channel.start_consuming()

    return HttpResponse("Consumer started!")
