import subprocess

def install_prerequisites():
    prerequisites = ["selenium", "tkinter"]
    try:
        for i in prerequisites:
            subprocess.call(f"pip install {i}")

    except:
        pass