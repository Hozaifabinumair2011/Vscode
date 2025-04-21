import os
if os.path.exists('document.txt'):
    print("file exsist")
else:
    print("file does not exsist")

os.remove('new.txt')
os.rmdir('Sample')