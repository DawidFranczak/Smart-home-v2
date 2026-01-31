import aio_pika
from contextlib import asynccontextmanager
import os
import asyncio
from fastapi import FastAPI

@asynccontextmanager
async def startup_event(app: FastAPI):
    asyncio.create_task(consume())
    yield

async def consume():
    user = os.environ.get("RABBITMQ_FASTAPI_USER")
    password = os.environ.get("RABBITMQ_FASTAPI_PASSWORD")
    address = os.environ.get("RABBITMQ_ADDRESS")
    queue_name = os.environ.get("QUEUE_NAME")
    amqp_url = f"amqp://{user}:{password}@{address}/"
    while True:
        try:
            connection = await aio_pika.connect_robust(amqp_url)
            break
        except Exception as e:
            print(f"RabbitMQ not ready, retrying in 5s... ({e})")
            await asyncio.sleep(5)
    print("Connected to RabbitMQ")
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue(queue_name, durable=True)
        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    print(f"Received from {queue_name}: {message.body.decode()}")
