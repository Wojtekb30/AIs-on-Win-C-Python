import keyboard
import os
#import time
import psutil
import gc
import webbrowser #comment if unused

URLc = "https://chatgpt.com/" #ChatGPT URL
URL = "https://duckduckgo.com/?q=chat&ia=chat" #DuckDuckGo AI Chats URL.

def process_exists(processName): #Check if process exists/runs.
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

def on_win_c(): #Runs when Win+C is pressed.
    while True:
        if process_exists("Cortana.exe"): #Check if Cortana opened.
            os.system('taskkill /F /IM Cortana.exe') #kill Cortana.
            os.system("start "+URLc) #open ChatGPT (with os).
            webbrowser.open(URL) #open DDG AIs (with webbrowser, because OS fails at &s in strings).
            #if you comment out webbrowser.open() and not use webbrowser library again, comment 'import webbrowser' too.
            gc.collect() #clean garbage to not occupy memory.
            break

keyboard.add_hotkey('win+c', on_win_c) #React to Win+C.

keyboard.wait()
