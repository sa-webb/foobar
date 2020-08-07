'''
with keyword is syntactic sugar for a try/catch exception handler and close() file
'''

with open('output.txt', 'w') as open_file:
    open_file.write('Output written to file')