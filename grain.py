import gd
import webbrowser
import time

never = gd.memory.get_memory()


while True:
    if never.is_dead():
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        time.sleep(1.2)
