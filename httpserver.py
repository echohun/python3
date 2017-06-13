import SimpleHTTPServer
import SocketServer

PORT = input("input port:")
 
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
 
httpd = SocketServer.TCPServer(("", PORT), Handler)
 
print "serving at port", PORT
httpd.serve_forever()
