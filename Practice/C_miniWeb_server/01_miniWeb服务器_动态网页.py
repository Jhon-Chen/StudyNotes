# 导入模块
import socket
from application import app

class WebServer():
    # 定义初始化方法
    def __init__(self):
        # 创建套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置套接字属性
        tcp_server_socket.setsocketopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定端口
        tcp_server_socket.bind("", 8080)
        # 开启监听 设置套接字从主动变为被动
        tcp_server_socket.listen(128)

        self.tcp_server_socket = tcp_server_socket

    # 定义启动服务器方法
    def start(self):
        while True:
            # 接受客户端连接并拆包
            new_client_socket, ip_port = self.tcp_server_socket.accept()
            # 调用request_handler()处理请求
            self.requset_handler(new_client_socket, ip_port)

    # 定义响应服务器的方法
    def requset_handler(self, new_client_socket, ip_port):
        # 接受客户端请求报文
        requset_data = new_client_socket.recv(1024)
        # 判断客户端是否已经下线
        if not requset_data:
            print('客户端[%s]已断开连接' % str(ip_port))
            new_client_socket.close()
            return
        # 调用app模块的application方法处理请求
        response_data = app.application
        # 发送请求报文
        new_client_socket.send(response_data)
        # 关闭连接
        new_client_socket.close()

def main():
    # 主函数入口
    ws = WebServer()
    ws.start

if __name__ == '__main__':
    main()
    

