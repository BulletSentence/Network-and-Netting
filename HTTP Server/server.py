from http.server import HTTPServer, BaseHTTPRequestHandler;

class ServerSetup(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><body><h1>Bom Dia</h1></body></html>", "utf-8"))

HOST = "192.168.0.123"
PORTA = 8080
server = HTTPServer((HOST, PORTA), ServerSetup)
print("Servidor rodando na URL: http://" + HOST + ":" + str(PORTA))
server.serve_forever()
server.server_close()