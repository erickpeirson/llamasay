#!/usr/bin/env python3

import os
from http.server import BaseHTTPRequestHandler, HTTPServer

LLAMA = """
                          ▓▓  ▓▓                                        
                        ▓▓░░▓▓░░▓▓                                      
                      ▓▓▓▓░░░░░░▓▓                                      
                    ▓▓░░░░░░██░░▓▓                                      
                    ▓▓░░░░░░░░░░▓▓                                      
                      ▓▓▓▓░░░░░░▓▓                                      
                          ▓▓░░░░▓▓                                      
                          ▓▓░░░░▓▓                ▓▓                    
                          ▓▓░░░░▓▓              ▓▓░░▓▓                  
                          ▓▓░░░░▓▓              ▓▓░░▓▓                  
                          ▓▓░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░▓▓                  
                          ▓▓░░░░░░░░░░░░░░░░░░░░░░▓▓                    
                          ▓▓░░░░░░░░░░░░░░░░░░░░░░▓▓                    
                          ▓▓░░░░░░░░░░░░░░░░░░░░░░▓▓                    
                          ▓▓░░░░░░░░░░░░░░░░░░░░░░▓▓                    
                          ▒▒░░▒▒░░▒▒▒▒░░░░░░░░░░▒▒▓▓                    
                            ▓▓░░░░░░░░░░░░░░░░░░▓▓                      
                            ▓▓▓▓▓▓░░▓▓▓▓▓▓▓▓▓▓░░▓▓                      
                            ▓▓░░▓▓░░▓▓  ▓▓░░▓▓░░▓▓                      
                            ▓▓░░▓▓░░▓▓  ▓▓░░▓▓░░▓▓                      
                            ▓▓░░▓▓░░▓▓  ▓▓░░▓▓░░▓▓                      
                            ▓▓░░▓▓░░▓▓  ▓▓░░▓▓░░▓▓                      
                            ▓▓░░▓▓░░▓▓  ▓▓░░▓▓░░▓▓                      
                              ▒▒  ▓▓      ▓▓  ▓▓     
"""


class WebRequestHandler(BaseHTTPRequestHandler):
  
    def do_GET(self):
        source = ":".join(map(str, self.client_address))
        target = ":".join(map(str, os.environ.get("POD_IP", self.server.server_address)))
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(f"\tSource: {source}\n\tTarget: {target}\n\n{LLAMA}".encode("utf-8"))

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 9000), WebRequestHandler)
    print("Llamaserv ready!")
    server.serve_forever()