import sys

# open file function
def load_dictionary(file):
    try:
        with open(file) as in_file:
            loaded_text = in_file.read().strip().split('\n')
            loaded_text = [x.lower() for x in loaded_text]
            return loaded_text
    except IOError as e:
        print(f'{e} \n error opening {in_file}. Terminating Program',
              file = sys.stderr)
        sys.exit(1)

#file_text = load_dictionary('iventWithPythonDict.txt')
#print(file_text)