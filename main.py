import time, webbrowser, os
WAIT_FOR = "Wait for how long before executing? (seconds): "
OPERATION = "What operation would you execute? (number): "
OP_LIST = """    (1) Restart
    (2) Shutdown
    (3) Fork bomb
    (4) Kill File Explorer
    (5) Rickroll
    (9) Custom Python file
    (q) Quit

> """

waittime = int(input(f"{WAIT_FOR}"))
print(f"{OPERATION}")
operation = input(f"{OP_LIST}")

SUCCESS = f"Success! The operation will execute in {str(waittime)} seconds and is currently in undercover."
ERROR = "Failed. The operation number is invalid. "
QUIT = "Quitting... "
def timesleeper(t):
    print(f"{SUCCESS}")
    time.sleep(t)

if operation == "1":
    timesleeper(waittime)
    os.system("shutdown -r -t 0")
elif operation == "2":
    timesleeper(waittime)
    os.system("shutdown -s -t 0")
elif operation == "3":
    timesleeper(waittime)
    import fork
elif operation == "4":
    timesleeper(waittime)
    os.system("taskkill /f /im explorer.exe")
elif operation == "5":
    timesleeper(waittime)
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
elif operation == "-":
    timesleeper(waittime)
    os.system("taskmgr")
elif operation == "9":
    timesleeper(waittime)
    import test
elif operation == "q":
    print(f"{QUIT}")
    exit()
else:
    print(f"{ERROR}")