def create_http_response(status_desc, response_body):
    # 拼接响应报文
    # 响应行
    response_line = "HTTP/1.1 200 OK\r\n"
    # 响应头
    response_header = "Server:PythonWS/1.1\r\n"
    # 响应空行
    response_blank = "\r\n"
    # 响应主体
    # 拼接响应报文
    response_data = (response_line + response_header + response_blank).encode() + response_body

    return response_data

