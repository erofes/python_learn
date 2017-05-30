import re



Text = "# Reeeeeal9 Nugget78RJ ReSlaveBoomerRea."


patt = re.compile('.') #.	Один любой символ, кроме новой строки \n.
print(patt.findall(Text))
#['#', ' ', 'R', 'e', 'e', 'e', 'e', 'e', 'a', 'l', '9', ' ', 'N', 'u', 'g',

patt = re.compile('R?') #?	0 или 1 вхождение шаблона слева
print(patt.findall(Text))
#['', '', 'R', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''

patt = re.compile('Re+') #+	1 и более вхождений шаблона слева (e)
print(patt.findall(Text))
#['Reeeee', 'Re', 'Re']
patt = re.compile('\w+')
print(patt.findall(Text))
#['Reeeeeal9', 'Nugget78RJ', 'ReSlaveBoomerRea']

patt = re.compile('Rea*') #*	0 и более вхождений шаблона слева (a)
print(patt.findall(Text))
#['Re', 'Re', 'Rea']

patt = re.compile('\W') #\w	Любая цифра или буква (\W — все, кроме буквы или цифры)
print(patt.findall(Text))
#['#', ' ', ' ', ' ', '.']
patt = re.compile('\w')
print(patt.findall(Text))
#['R', 'e', 'e', 'e', 'e', 'e', 'a', 'l', '9', 'N', 'u', 'g', 'g'

patt = re.compile('\D') #\d	Любая цифра [0-9] (\D — все, кроме цифры)
print(patt.findall(Text))
#['#', ' ', 'R', 'e', 'e', 'e', 'e', 'e', 'a', 'l', ' ', 'N', 'u',
patt = re.compile('\d')
print(patt.findall(Text))
#['9', '7', '8']

patt = re.compile('\S')#\s	Любой пробельный символ (\S — любой непробельнй символ)
print(patt.findall(Text))
#['#', 'R', 'e', 'e', 'e', 'e', 'e', 'a', 'l', '9', 'N', 'u', 'g',
patt = re.compile('\s')
print(patt.findall(Text))
#[' ', ' ', ' ']

patt = re.compile(r'\b')#\b	Граница слова ???
print(patt.findall(Text))
#['', '', '', '', '', '']

patt = re.compile('[^Rex]') #[..]	Один из символов в скобках ([^..] — любой символ, кроме тех, что в скобках)
print(patt.findall(Text))
#['#', ' ', 'a', 'l', '9', ' ', 'N', 'u', 'g', 'g', 't', '7', '8', 'J',
patt = re.compile('[Rex]') #[..]	Один из символов в скобках ([^..] — любой символ, кроме тех, что в скобках)
print(patt.findall(Text))
#['R', 'e', 'e', 'e', 'e', 'e', 'e', 'R', 'R', 'e', 'e', 'e', 'R', 'e']

patt = re.compile('\.')#\	Экранирование специальных символов (\. означает точку или \+ — знак «плюс»)
print(patt.findall(Text))
#['.']

patt = re.compile('^# Re')#^ и $	Начало и конец строки соответственно
print(patt.findall(Text)) #Поиск с привязкой к началу по заданному шаблону
#['# Re']
patt = re.compile('a\.$') #Конец строки
print(patt.findall(Text))
#['a.']

patt = re.compile('e{3,6}')#{n,m}	От n до m вхождений ({,m} — от 0 до m)
print(patt.findall(Text))
#['eeeee']

patt = re.compile('Nug|Sla') #a|b	Соответствует a или b
print(patt.findall(Text))
#['Nug', 'Sla']

patt = re.compile('(Nug|Sla)ve')#()	Группирует выражение и возвращает найденный текст
print(patt.findall(Text))
#['Sla']
patt = re.compile('(Sla)(ve)')
print(patt.findall(Text))
#[('Sla', 've')]

patt = re.compile('\n') #\t, \n, \r	Символ табуляции, новой строки и возврата каретки соответственно
print(patt.findall(Text))
#[]


Text = "Reeeeeal9 Nugget78RJ ReSlaveBoomerRea."
patt = re.compile(r'\b\w.')#\b	Граница слова ??? - only r'' - отключить экранирование
print(patt.findall(Text))