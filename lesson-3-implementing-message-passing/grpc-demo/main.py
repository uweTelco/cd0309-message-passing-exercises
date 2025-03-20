import time
from concurrent import futures

import grpc
import order_pb2
import order_pb2_grpc


class OrderServiceServicer(order_pb2_grpc.OrderServiceServicer):
    def Create(self, request, context):
         print("Received OrderMessage:")
         print(request)  # Prints the OrderMessage
         return request
    
    def Get(self, request, context):
        #  To be implemented
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
order_pb2_grpc.add_OrderServiceServicer_to_server(OrderServiceServicer(), server)

print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
