from socketserver import TCPServer, BaseRequestHandler
from shutil import copy as copyfile
from datetime import datetime as dt
from time import time

try:
    from conf import SERVER_PORT
except ImportError:
    print("Could not find conf.py!\nTrying to copy DEFAULT config to conf.py...")
    copyfile("./DEFAULT_conf.py", "./conf.py")
    from conf import SERVER_PORT
    print("Successful!")

 
class RequestHandler(BaseRequestHandler):
    def handle(self) -> None:
        data: str = self.request.recv(512).strip().decode("UTF-8")
        with open("server_key.log", "a", encoding="UTF-8") as logfile:
            logfile.write(f"{dt.fromtimestamp(int(time()))}:\n{data}\n")
        return super().handle() 


with TCPServer(("localhost", SERVER_PORT), RequestHandler) as server:
    server.serve_forever()
