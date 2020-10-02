from protos import demo_pb2_grpc
from protos import demo_pb2
from grpc_server.services import Basic
import msgpack


class InteractionService(demo_pb2_grpc.DemoServicer):

    def __init__(self):
        self.c = Basic()

    def GetServerResponseDemo(self, request_iterator, context):
        for message in request_iterator:
            msg = msgpack.unpackb(message.message, raw=False)
            message_transformed = Basic().get_data(self.c, msg)
            packed_open_session = msgpack.packb(message_transformed, use_bin_type=True)
            yield demo_pb2.Message(message=packed_open_session)
