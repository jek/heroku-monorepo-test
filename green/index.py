#!/usr/bin/env python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from StringIO import StringIO
import os


class EchoHandler(BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.0'

    def do_GET(self):
        """Serve a GET request."""

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        r = """
        <html>
        <head><style>* { font-family: fixed; }</style></head>
        <body>
        """

        if os.path.exists('banner.html'):
            r += open('banner.html').read()

        r += "<table>"
        for pair in sorted(os.environ.items()):
            r += "<tr><td>%s</td><td>%s</td></tr>" % pair
        r += '</table>'
        if os.path.exists('recorder.txt'):
            r += '<hr/><p>Build Record:</p><pre>'
            r += open('recorder.txt').read()
            r += '\n</pre>'
        r += '</body></html>'

        self.wfile.write(r)



if __name__ == '__main__':
    server_address = ('', int(os.environ['PORT']))
    httpd = HTTPServer(server_address, EchoHandler)
    sa = httpd.socket.getsockname()
    print("Serving HTTP on %s port %s..." % sa[0:2])
    httpd.serve_forever()


