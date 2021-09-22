import random
import gd

banana = gd.memory.get_memory()

while True:
    sex = random.randint(0,10000)
    if banana.is_in_level():
        banana.set_x_pos(sex)
        
