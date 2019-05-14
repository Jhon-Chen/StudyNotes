# 导入模块
import socket
from application import app

# 创建服务器类
class WebServer(object):
    def __init__(self):
        # 创建套接字
        web_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置套接字属性端口重用
        web_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定端口
        web_server_socket.bind(("", 8080 ))
        # 开启监听
        web_server_socket.listen(101)
        # 保存套接字
        self.web_server_socket = web_server_socket
    def start(self):
        while True:
            new_client_socket, ip_port = self.web_server_socket.accept()
            print("新客户端[%s]来了" % str(ip_port))
            # 调用响应服务器方法函数
            self.request_handler(new_client_socket, ip_port)

    def request_handler(self, new_client_socket, ip_port):
        # 接受请求报文
        request_data = new_client_socket.recv(2048)
        # 判断客户端是否已下线
        if not request_data:
            print("客户端[%s]已下线", str(ip_port))
            new_client_socket.close()
            return 
        # 调用app模块解析报文函数
        response_data = app.application("static", request_data, ip_port)
        # 发送响应报文
        new_client_socket.send(response_data)
        # 关闭套接字
        new_client_socket.close()


# 定义主函数
def main():
    wb = WebServer()
    wb.start()

# 运行主函数
if __name__ == "__main__":
    main()
