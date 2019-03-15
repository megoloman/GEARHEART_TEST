from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

from replacer import replace_content

BASE_PATH = 'https://habrahabr.ru'


class HabrProxyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        habr = requests.get(BASE_PATH + self.path)

        self.send_response(habr.status_code)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        new_content = replace_content(habr.content.decode())
        self.wfile.write(new_content.encode())
        return


server = HTTPServer(('127.0.0.1', 8080,), HabrProxyHandler)
server.serve_forever()