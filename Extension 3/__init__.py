import

socketserver.TCPServer.allow_reuse_address = True

PORT = 8000





Handler = testHTTPRequestHandler
#httpd.serve_forever(). Create a class that includes all the logic related with OpenFDA
class OpenFDAClient():
    #Code related to sending queries to OpenFDA
    #We also move the one for searching drugs
    pass
#hago lo mismo con los otros.
#the ones for creating html list con el segundo