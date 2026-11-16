from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs, unquote
import os

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)

        if parsed.path == "/read":
            params = parse_qs(parsed.query)
            raw = params.get("path", [None])[0]

            if not raw:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Missing ?path=")
                return

            try:
                if raw.startswith("file://"):
                    u = urlparse(raw)
                    path = unquote(u.path)
                    if os.name == "nt" and path.startswith("/"):
                        path = path[1:]
                else:
                    path = raw

                with open(path, "rb") as f:
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(f.read())

            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(str(e).encode())

        else:
            # Everything else: behave like a normal static file server
            super().do_GET()

server = HTTPServer(("0.0.0.0", 8000), Handler)
print("Serving current directory + /read on http://localhost:8000")
server.serve_forever()
