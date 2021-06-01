'''Argument sifatida ismni o’qib olib,
 natija sifatida o’sha ismga
  salom deydigan funktsiya tuzing.'''
def greet(name):
    '''

    :parameter:
       name
    :return
         hello name
    '''
    print(f'Hello ,{name} !')
name = input("Ism kiriting ")
print(greet.__doc__,'\n',greet(name))
greet(name)
