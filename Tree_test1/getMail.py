from random import randrange,choice
def get_length():
    irand = randrange(8, 22)
    print(irand)
    return irand
main_tree_data = []
for i in range(97, 123):
    main_tree_data.append(chr(i))
def print_mail():
    a=get_length()
    m=''
    for i in range(a):
        m += choice(main_tree_data)
    return m
def get_mail():
    c=print_mail()+'@gmail.com'
    return c
d=[]
for i in range(5):
    d.append(get_mail())
print(d)
text = open('mail.txt', 'w')
data = '\n'.join(d)
text.writelines(data)
text.close()

