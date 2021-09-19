import gd
import time

markus = gd.memory.get_memory()


while True:
    if markus.attempt == 10:
        markus.player_freeze()
    if markus.is_dead():
        print(markus.attempt)
        time.sleep(1.2)
