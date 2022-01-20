# Problem 1
# Python3 
# no libs needed
# you will have to put the file names in the same directory

import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from json import JSONDecodeError

hostName = "localhost"


class MyServer(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def write_text_to_output(self, text):
        self.wfile.write(text.encode())

    def attempt_get_file_contents(self, file_name):
        try:
            with open(file_name, "r") as f:
                self.write_text_to_output(f.read())
        except IsADirectoryError as e:
            self.write_text_to_output(f"{self.path} is a directory")
        except FileNotFoundError:
            self.write_text_to_output("HTTP 404! File not found")

    def do_GET(self):
        print(f"In GET method, path {self.path}")
        self._set_headers()
        # get file name from path e.g. localhost/index.html is index.html
        file_name = self.path
        # remove leading / in file name e.g. /test.html to test.html
        file_name = file_name.replace("/", "", 1)
        self.attempt_get_file_contents(file_name)

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        """
        Recieve JSON file name via post, log the data and return its contents as response
        """
        self._set_headers()
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        print(f"In post method, data {self.data_string}")

        try:
            data = json.loads(self.data_string)
            # Generate unique file name for logging
            out_file_name = f"sever_logs_{int(time.time())}.json"
            with open(out_file_name, "w") as outfile:
                json.dump(data, outfile)
            file_name_from_post = data['file_name']
            self.attempt_get_file_contents(file_name_from_post)
        except JSONDecodeError:
            self.wfile.write(b'The POST JSON is not well formatted')
        except KeyError:
            self.wfile.write(b'The POST JSON is invalid. No file_name key')


if __name__ == "__main__":
    serverPort = input("Enter server port : ")
    serverPort = int(serverPort)
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
