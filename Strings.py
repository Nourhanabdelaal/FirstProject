a = '123456\n5846'
print(a)
print(a.splitlines())

print('--------------------------')

b = '456789\\nsdsdsd'
print(b)

print('--------------------------')

c = 'dsjdkbsd\tdjfbfjf'
print(c)
print(c.split())
print(c.splitlines())
print(c[2])

d = '1234567\t4896464\tdhjvshd\tffdfdf'
print(d)
print(d[2])

print(d.split())
print(d.split('\t'))

m = '123456\tdsnfsfubf\t468445666'

mn = m.split('\t')

print(mn[0])

sd = 'fkgfsgf\ndfflskfs\n6469++646'

s = sd.split()

print(s)
print(s[1])

d = 'nmssjkfbsf\nfsfhsfnm'

# count is counting the number of objects, while index gives the first place of it
# Find also gives the place of certain object
# rindex gives the last occurence of an object within a string
print(d.count('nm'))
print(d.index('nm'))
print(d.find('nm'))
print(d.rindex('nm'))


# Another way of formatting instead of f , to use %s' %
print('Count D as: %s '% d.count('nm'))
print('INDEX: %s'% d.index(('j')))
print('Find my symbol: %s'% d.find('b'))

# Difference between index and find that, if value not found then index would give an error while find would give -1
print('Find: %s'% d.find('A'))
# Throws ValueError if not found
print('Index:%s'% d.index('n'))

print('----------------------------')

#strip removes any spaces from left and right, rstrip removes the right space, while lstrip removes the left space.
Hello = '              hsddhvdvsdx      fskfkfkkff      sffsfsfsfsfs        '
print(Hello.strip())
print(Hello.rstrip())
print(Hello.lstrip())















































































