from http.server import BaseHTTPRequestHandler, HTTPServer

class BackendHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        message = b"Hello from Backend 2 - VM1!"

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(message)))
        self.end_headers()

        self.wfile.write(message)

server = HTTPServer(("0.0.0.0", 8081), BackendHandler)

print("Backend 2 running on port 8081...")

server.serve_forever()
