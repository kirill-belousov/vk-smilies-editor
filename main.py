def command(c):
	if c == "exit": exit()
	if c == "save": savefile()
	if c == "open": openfile()

def savefile():
	name = input("введите имя файла для сохранения")
	f = open(name, "w", encoding="utf_8_sig")
	i = d.items()
	for item in i:
		f.write("{symbol}\t{word}\t0\t0\n".format(symbol=item[0], word=item[1]))
	f.close()
	print("файл сохранён")

def openfile():
	n = input ("введите имя файла, который нужно открыть")
	f = open(n, "r", encoding="utf_8_sig")
	for line in f:
		s = line.split("\t")
		if len(s) <= 1: continue
		d[s[0]] = s[1]
	f.close()


d = dict()
openfile()

while True:
	cmd = input("введите команду или символ: ")
	if cmd[0] == "/": command(cmd[1:]);continue
	if d.get(cmd):
		print(d[cmd])
		s = input("изменить описание символа? введите новое описание или /, чтобы оставить старое")
		if s == "/": continue
		else:
			d[cmd] = s
	else:
		s = input("символ не найден в словаре. добавить? введите описание символа или / для отмены")
		if s == "/": continue
		else:
			d[cmd] = s

