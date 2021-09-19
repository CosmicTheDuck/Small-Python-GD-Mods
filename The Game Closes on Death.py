import gd
import time
import os

meme = gd.memory.get_memory()

while True:
	if meme.is_dead():
		print('bad')
		os.system("taskkill /f /im \"GeometryDash.exe\"")
		time.sleep(1.2)
	if meme.percent >= 100:
		print('good')