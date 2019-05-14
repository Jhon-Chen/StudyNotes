from application import utils
import time
from application import funs
from application import urls


def parse_requsest(request_data):
    """处理客户端请求"""
    # 解码客户端发来的请求报文 得到请求行
    request_text = request_data.decode()
    # 得到请求行 使用"\r\n"切片得到
    request_list = request_text.split("\r\n")
    # 得到请求路径
    request_line_parts = request_list[0].split(" ")
    # 定义空字典
    request_line_dict = dict()
    # 把资源保存到字典中
    # key ----> value
    # file_path ----> /index.html
    request_line_dict['file_path'] = request_line_parts[1]
    # 保存请求协议版本
    request_line_dict['version'] = request_line_parts[2]
    # 保存请求方式
    request_line_dict['method'] = request_line_parts[0]

    # 设置默认首页
    if request_line_dict['file_path'] == '/':
        request_line_dict['file_path'] = '/index.html'
    return request_line_dict 

def application(static, request_data, ip_port):
    # 解析请求报文 得到请求信息字典
    request_line_dict = parse_requsest(request_data)
    path_info = 'static' + request_line_dict['file_path']
    response_data = ""
    # 判断文件是否是python文件
    if request_line_dict['file_path'].endswith(".py"):
        # 如果是python动态文件 做单独处理
        # 判断当前访问路径是否在路由列表中
        if request_line_dict['file_path'] in urls.route_dict:
            # 调用对应函数
            func = urls.route_dict[request_line_dict['file_path']]
            # 调用函数执行 并且得到返回值
            response_body =func()
            # 创建HTTP协议
            response_data = utils.create_http_response("200 OK", response_body.encode())
        else:
            response_data = utils.create_http_response("404 Not Found", "Not Found")

    else:
        try:
            # 如果报错 则执行此代码
            with open(path_info, "rb") as file:
                response_body = file.read()
                # 调用方法 得到响应报文
                response_data = utils.create_http_response("200 OK", response_body)
        except Exception as e:
            # 重新设置请求行
            response_line = "HTTP/1.1 404 Not Found\r\n"
            # 重新设置响应信息为错误信息
            response_body = "Error!! %s" % str(e)
            response_body = response_body.encode()
            response_data = utils.create_http_response("404 Not Found", response_body)
    return response_data


    
