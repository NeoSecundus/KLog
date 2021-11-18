import PyInstaller.__main__ as PyInstaller
import platform, os

my_sys = platform.system()
install_options = [
    "klog.py", 
    "--onefile", 
    "--nowindow", 
    "--noconfirm",
    "-p.", 
    "-nKLog"
    ]

if my_sys == "Linux" or my_sys == "Windows":
    PyInstaller.run(install_options)
elif my_sys == "Darwin":
    install_options.append("--osx-bundle-identifier net.anonymous.klog")
    PyInstaller.run(install_options)
else:
    print(f"Not implemented: Build for os '{my_sys}' cannot be run!")
    exit(1)

try:
    os.remove("./KLog.spec")
except FileNotFoundError:
    print("\033[33mNo Spec file to remove! Skipping optional cleanup...\033[0m")
