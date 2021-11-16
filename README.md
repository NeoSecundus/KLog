# KLog

A simple Key Logger that can run in the background.
(Really very simple)

## Dependencies

Python package dependencies:

- keyboard
- py2exe

(In [Requirements File](./requirements.txt))

## Build

The following command will create a minimal exe file within a `dist` folder

```bash
python3 klog_setup.py
```

## Usage

Either use Python or the Exe file.

**Python:**
```bash
python3 klog.py
```

The logger will create a log file named key.log in the root directory of the project. It will dump all recognized keystrokes there. There is some basic formatting but nothing crazy.
