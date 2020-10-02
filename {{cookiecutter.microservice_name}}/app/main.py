import os
from concurrent import futures
import grpc
from interactions.interactions import InteractionService
import logging
from protos import demo_pb2_grpc
from protos import demo_pb2


def run_server():
    server = grpc.server(futures.ThreadPoolExecutor(int(os.environ.get('MAX_WORKERS'))))
    demo_pb2_grpc.add_DemoServicer_to_server(InteractionService(), server)
    server.add_insecure_port('%s:%d' % (os.environ.get('DEMO_SERVER_HOST'), int(os.environ.get('DEMO_SERVER_PORT'))))
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    run_server()
