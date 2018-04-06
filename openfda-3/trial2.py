import socket
import http.client
import json

PORT = 8092
MAX_OPEN_REQUESTS = 5

def process_client(clientsocket):
    headers = {'User-Agent': 'http-client'}

    conn = http.client.HTTPSConnection("api.fda.gov")
    conn.request("GET", "/drug/label.json?limit=10", None, headers)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    repos_raw = r1.read().decode("utf-8")
    conn.close()
    repos = json.loads(repos_raw)

    drug = []
    a = 0
    sd = "<ol>" + "\n"


    while a < 10:
        if 'active_ingredient' in repos['results'][a]:
            a += 1
            drug.append(repos['results'][a]['id'])
        else:
            a += 1
            drug.append("There is no drug in  this index")

    with open("trial3.html", "w") as f:
        f.write(sd)
        for el in drug:
            el_1 = "<\t>" + "<li>" + el
            f.write(el_1)


    with open("trial3.html", "r") as f:
        file = f.read()

    print(clientsocket)
    print(clientsocket.recv(1024))

    f = open('trial3.html', 'w')

    message = """<html>
    <head></head>
    <body><p>Hello World!</p></body>
    </html>"""

    f.write(message)
    f.close()

    web_contents = file
    web_headers = "HTTP/1.1 200"
    web_headers += "\n" + "Content-Type: text/html"
    web_headers += "\n" + "Content-Length: %i" % len(str.encode(web_contents))
    clientsocket.send(str.encode(web_headers + "\n\n" + web_contents))
    clientsocket.close()


# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
hostname = socket.gethostname()
# Let's use better the local interface name
hostname = "10.10.107.36"
try:
    serversocket.bind((hostname, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        # accept connections from outside
        print ("Waiting for connections at %s %i" % (hostname, PORT))
        (clientsocket, address) = serversocket.accept()
        # now do something with the clientsocket
        # in this case, we'll pretend this is a non threaded server
        process_client(clientsocket)

except socket.error as ex:
    print("Problemas using port %i. Do you have permission?" % PORT)
    print(ex)