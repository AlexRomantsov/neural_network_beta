import os
import time

def readf(file):
	f = open(file, 'r')
	ye = f.read()
	f.close()
	return ye

def write_a(file, data):
	f = open(file, 'a+')
	f.write(data)
	f.close()

print('-'*25 + '\nDefaults commands: \nexit, cls\n' + '-'*25)
while True:
	words = readf('words.gd').strip().replace('\n', '').split(';')
	ll = True
	msg = input('Speak: ').lower()
	msg = msg.replace('?','')
	msg = msg.replace('!','')
	if msg == 'exit' or msg == 'goodbye':
		print("Goodbye")
		time.sleep(0.5)
		exit()
	elif msg == 'cls':
		os.system('cls')
	else:
		for i in words:
			if ll:
				if i == msg:
					ll = False
					continue
				if words.count(msg) == 0:
					print('What is it?')
					write_rect = input('What is my reaction to this?: ')
					write_a('words.gd', ';\n'+msg+';'+write_rect)
					words = readf('words.gd').strip().replace('\n', '').split(';')
					print('Took note')
					ll = True
			else:
				print(i)
				ll = True
				continue