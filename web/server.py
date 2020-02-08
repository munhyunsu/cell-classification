import http.server
import socketserver

FLAGS = None


class MyRequestHandler(http.server.CGIHTTPRequestHandler):
    pass


class MyHTTPServer(socketserver.TCPServer):
    allow_reuse_address= True


def main():
    with MyHTTPServer((FLAGS.ip, FLAGS.port),
                      MyRequestHandler) as httpd:
        print(f'Serving at {httpd.server_address}')
        httpd.serve_forever()


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ip', type=str, default='')
    parser.add_argument('-p', '--port', type=int, default=8080)

    FLAGS, _ = parser.parse_known_args()

    main()

