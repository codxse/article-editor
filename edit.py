f = open('article.txt')
lines = f.readlines()
f.close()

f = open('article.txt', 'w')
lines2 = list(lines)
line0 = lines2[0]
char0 = line0[0]
f.write('<span class="drop_cap">' + str(char0) + '</span>')
for line in lines:
	if line == lines[0]:
		f.write(line[1:])
	else:
		f.write(line[:])
f.close()

with open('article.txt', 'r') as src:
	with open('new_article.txt', 'w') as out:
		for line in src:
			if line[-2] == '.' or line[-2] == '!':
				out.write('<p>%s</p>\n\n' % line.rstrip('\n'))
			elif line == '***\n' or line == '**\n':
				out.write('<p class="aligncenter">%s</p>\n\n' % line.rstrip('\n'))
			elif line[0].isupper() and line[-2].isupper():
				out.write('<h2>%s</h2>\n\n' % line.rstrip('\n'))
			else:
				out.write('<h3>%s</h3>\n\n' % line.rstrip('\n'))