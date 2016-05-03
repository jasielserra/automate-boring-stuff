#! python3
# bulletPointAdder.py - Acrescenta marcadores da Wikipedia no início
# de cada linha de texto do clipboard.

import pyperclip
text = pyperclip.paste()

# Separa as linhas e acrescenta os astericos
lines = text.split('\n')
for i in range(len(lines)):         #percorre todos os indices da lista "lines" em um loop.
    lines[i] = '*  '+   lines[i]        #acrescenta um asterico em cada string da lista "lines"

text = '\n'.join(lines)
pyperclip.copy(text)
