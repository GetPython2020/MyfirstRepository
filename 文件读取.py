
with open('new_file.text','r') as f:
    data=f.read()
with open ('new_file_copy.text','w') as fcopy:
    fcopy.write('This is a copy' + '\n'+data)