1. 安装gRPC：
```
pip3 install grpcio
```

2. 安装proto编译工具：

```
pip3 install protobuf
pip3 install grpcio-tools
```

3. 编写proto文件：
```
vim grpc/helloworld.proto
```

```
syntax = "proto3";

service Greeter {
    rpc SayHello(HelloRequest) returns (HelloReply) {}
    rpc SayHelloAgain(HelloRequest) returns (HelloReply) {}
}

message HelloRequest {
    string name = 1;
}

message HelloReply {
    string message = 1;
}
```

4. 编译proto文件：
```
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. grpc/helloworld.proto
```

5. 服务器程序：
```python
from concurrent import futures
import time
import grpc
import helloworld_pb2
import helloworld_pb2_grpc

# 实现 proto 文件中定义的 GreeterServicer
class Greeter(helloworld_pb2_grpc.GreeterServicer):
    # 实现 proto 文件中定义的 rpc 调用
    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message = 'hello {msg}'.format(msg = request.name))

    def SayHelloAgain(self, request, context):
        return helloworld_pb2.HelloReply(message='hello {msg} again'.format(msg = request.name))

def serve():
    # 启动 rpc 服务
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('localhost:50051')
    server.start()
    _ONE_DAY_IN_SECONDS = 60 * 60 * 24
    # 使用 ctrl+c 可以退出服务
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
```
6. 客户端程序：
```python
import grpc
import helloworld_pb2
import helloworld_pb2_grpc

def run():
    # 连接 rpc 服务器
    with grpc.insecure_channel('localhost:50051') as channel:
        # 调用 rpc 服务
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='jack'))
        print("Greeter client received: " + response.message)
        response = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name='jack'))
        print("Greeter client received: " + response.message)

if __name__ == '__main__':
    run()
```