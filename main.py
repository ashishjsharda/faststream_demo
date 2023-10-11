from faststream import FastStream
from faststream.kafka import KafkaBroker

broker = KafkaBroker('localhost:9092')
stream = FastStream(broker)

@broker.subscribe('my-topic')
async def my_topic_handler(message):
    print(message)
