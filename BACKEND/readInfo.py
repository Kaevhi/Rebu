import http.server
import socketserver
import json
import urllib.parse

PORT = 8000

class MyHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            with open("signUp2.html", "r") as file:
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(file.read().encode())

    def do_POST(self):
        if self.path == "/submit":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            parsed_data = urllib.parse.parse_qs(post_data.decode())

            user = {
                'first_name': parsed_data.get('first_name', [None])[0],
                'last_name': parsed_data.get('last_name', [None])[0],
                'username': parsed_data.get('username', [None])[0],
                'email': parsed_data.get('email', [None])[0],
                'password': parsed_data.get('password', [None])[0]  # Hash this in real applications!
            }

            with open('data.json', 'r') as file:
                data = json.load(file)
                if not "users" in data:
                    data["users"] = []
                data['users'].append(user)

            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)

            self.send_response(302)  # Redirect
            self.send_header("Location", "/")  # Redirect to the signup page for simplicity
            self.end_headers()

handler = MyHandler
httpd = socketserver.TCPServer(("", PORT), handler)
print(f"Serving at port {PORT}")
httpd.serve_forever() 
