import base64
from argparse import ArgumentParser

class Obfuscator:
    '''
    Python code obfuscator
    '''
    def __init__(self ,file):
        self.file = file
        self.payload ='''
import base64
exec(base64.b64decode('{}'.encode('UTF-8')).decode('UTF-8'))
        '''

    def check_file(self):
        file_extension = self.file.split('.')[-1]
        if file_extension != 'py':
            print('Error : file extension must be .py')
            exit()

    def obfuscate(self):
        try:
            with open(self.file ,'r') as file :
                py_file_content = file.read()
        except FileNotFoundError :
            print(f'Error : file ({self.file}) does not exist')
            exit()

        content_bytes = py_file_content.encode('UTF-8')
        base64_bytes = base64.b64encode(content_bytes)
        base64_msg = base64_bytes.decode('UTF8')
        #
        injected_payload = self.payload.format(base64_msg)
        final_payload = injected_payload
        #
        new_file_name = self.file.split('.')[0] + '_obfuscated.py'
        with open(new_file_name ,'w') as new_file :
            new_file.write(final_payload)

        print('Python code obfuscated successfully.')
        print('Obfuscated file --> ' + new_file_name)


def print_help():
    help_msg = '''
usage: psobfus.py [--file (Python file name or path)]
optional arguments:
  --file ,-file ,-f (Python file name or path e.g : myscript.py)
    '''
    print(help_msg)

if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('--file','-file','-f' ,metavar='(Python file name or path)')
    args ,unknown = parser.parse_known_args()
    if (args.file is not None) :
        obfuscator = Obfuscator(file=args.file)
        obfuscator.check_file()
        obfuscator.obfuscate()
    else:
        print_help()