#!/usr/bin/env python3
import http.server
import socketserver
import os
import json

PORT = int(os.getenv("PORT", 3000))

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            response = {"status": "ok", "port": str(PORT), "message": "Docker test!"}
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_error(404)

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    print(f"Server on port {PORT}")
    httpd.serve_forever()
