import gd

toad = gd.memory.get_memory()
#insert another dumb comment here :)

while True:
    if toad.is_level_demon():
        toad.player_kill_enable()
    if toad.is_level_demon() == False:
        toad.player_kill_disable()
