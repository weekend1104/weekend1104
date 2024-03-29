import socket

connect = socket.socket()

connect.bind(("127.0.0.1",9090))
connect.listen(2)



if __name__ == "__main__":
    # while 1:
    #     print("wait for links!")
    #     conn,addr = connect.accept()
    #     webcon = conn.recv(1024)
    #     print(webcon)
    #     conn.send(b"HTTP/1.1 200 OK\r\nservername:youxiu\r\n\r\nhello,websoket!")
    #     conn.close()

    dicttest = dict('GET /favicon.ico HTTP/1.1\r\nHost: localhost:9090\r\nConnection: keep-alive\r\nsec-ch-ua: "Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"\r\nsec-ch-ua-mobile: ?0\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36\r\nsec-ch-ua-platform: "Windows"\r\nAccept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8\r\nSec-Fetch-Site: same-origin\r\nSec-Fetch-Mode: no-cors\r\nSec-Fetch-Dest: image\r\nReferer: http://localhost:9090/\r\nAccept-Encoding: gzip, deflate, br, zstd\r\nAccept-Language: zh-CN,zh;q=0.9\r\n\r\n')
    print(dicttest)