# KLog

A simple Key Logger that can run in the background.
(Really very simple)
Can also send parsed key strokes to a remote server which is also included in the repo. (klog_listener.py)

## Dependencies

Python package dependencies:

- keyboard
- pyinstaller

(In [Requirements File](./requirements.txt))

## Build

The following command will create a minimal executable file within a `dist` folder. The format of the distributable depends on the os you're using. It will always be a single file!

```bash
python3 build.py
```

## Usage

Either use Python or the executable file for the client.

**Python:**
```bash
python3 klog.py
```

The logger will create a log file named key.log in the root directory of the project. It will dump all recognized keystrokes there. There is some basic formatting but nothing crazy.

It can also send input to a remote server which can be started with python only. All necessary configurations are within the *conf.py* file.

### The *conf.py* file

You can either rename/copy the *DEFAULT_conf.py* file to *conf.py* or simply run one of the scripts. Meaning the listener, logger or build script. The conf file will be created automatically if it's not found in the repo folder. 
> If possible change the *conf.py* file but not the *DEFAULT_conf.py* file!
