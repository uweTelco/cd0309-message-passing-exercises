import grpc
import order_pb2 as order_pb2
import order_pb2_grpc as order_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:5005') as channel:
        stub = order_pb2_grpc.OrderServiceStub(channel)
        order = order_pb2.OrderMessage(
            id='123',
            created_by='test_user',
            status=order_pb2.OrderMessage.Status.QUEUED,
            created_at='2024-08-22',
            equipment=[order_pb2.OrderMessage.Equipment.KEYBOARD, order_pb2.OrderMessage.Equipment.MOUSE]
        )
        response = stub.Create(order)
        print("Client received:", response)

if __name__ == '__main__':
    run()
