import http.server
import socketserver
import http.client
import json

# -- IP and the port of the server
IP = "localhost"  # Localhost means "I": your local machine
PORT = 8002


# HTTPRequestHandler class
class testHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()


        #def file_sent(nombre_arch):
         #   with open(nombre_arch,'r') as f:
             #   mensaje= f.read()



        path = self.path

        if path == "/":
            print("SEARCH: client entered search web")
            with open("search.html",'r') as f:
                mensaje= f.read()
                self.wfile.write(bytes(mensaje), "utf8")

        elif 'Search' in path:  # let´s try to find a drug and a limit entered by user
            print("SEARCHED: client has attemped to make a request")
            data = self.path.strip('/search.html').split('&')
            drug = data[0].split('=')[1]
            limit = data[1].split('=')[1]
            print("client has succesfully made a request")
            nombre_arch = "fda_info.html"
            headers = {'User-Agent': 'http-client'}
            conn = http.client.HTTPSConnection("api.fda.gov")
            url = "/drug/label.json?search=generic_name:"+ drug + '&' + 'limit=' + limit
            conn.request("GET", url, None, headers)
            r1 = conn.getresponse()
            print(r1.status, r1.reason)
            repos_raw = r1.read().decode("utf-8")
            conn.close()
            repos = json.loads(repos_raw)
            self.wfile.write(bytes(str(repos), "utf8"))
        return






# Handler = http.server.SimpleHTTPRequestHandler
Handler = testHTTPRequestHandler

httpd = socketserver.TCPServer((IP, PORT), Handler)
print("serving at port", PORT)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass

httpd.server_close()
print("")
print("Server stopped!")