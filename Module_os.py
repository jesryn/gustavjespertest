import os
import sys
print('os.environ: ', os.environ)
print('os.getcwd()', os.getcwd())
print('sys.version: ', sys.version)  #String of Python verion
print('sys.path: ', sys.path)  # List containing search path for modules
print('sys.modules: ', sys.modules)  #Dictionary of currently loaded modules
print('sys.platform: ', sys.platform)  # String of operating system type
print('sys.executable: ', sys.executable) # String of pathname to Python interpreter

#sys.exit(val)

a = ['Gustav', 'Jesper', 'Maria']
age = {}
age['Gustav'] = 28
age['Jesper'] = 55
age['Maria'] = 53

for namn in a:
    print(namn, 'ålder:', age[namn])

print (age['Gustav'])
print(a)
a.append('Anna')
print(a)
a.insert(2,'Philip')
print(a)

stad = 'Enköping'
delavstad= stad[0:2]
print('*', delavstad)
if delavstad == 'En':
    print(stad)

for k in age.keys():
    print(k, age[k])



