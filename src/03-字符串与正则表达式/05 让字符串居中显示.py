# question1
'''

1：center方法
2：format方法
'''

# question2
# center(n)
print('<' + 'hello'.center(30) + '>')
print('<' + 'hello'.center(30, '#') + '>')

# ''.format(str)
print('<{:^30}{:^30}>'.format('hello', 'word'))
print('<{:#^30}>'.format('hello'))

# format(str, '')
print("--------------")
print('<', format('hello', '^28'), '>')
