from http.server import BaseHTTPRequestHandler, HTTPServer

class BackendHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/api/hello":
            message = b"Hello from Backend VM!"

            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.send_header("Content-Length", str(len(message)))
            self.end_headers()

            self.wfile.write(message)

        else:
            self.send_response(404)
            self.end_headers()

server = HTTPServer(("0.0.0.0", 8080), BackendHandler)

print("Backend running on port 8080...")

server.serve_forever()
