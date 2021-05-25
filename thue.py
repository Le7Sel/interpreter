from random import randint
import re
import fileinput

program_name = input("Program to run : ")
instructions = []
for line in fileinput.input(files = program_name):
   instructions.append(line[:-1])
discarded_instructions = []

pattern = re.compile('(.+)::=(.*)')

eof = False
data = ""
while len(instructions)!=0:
    last_instruction = instructions.pop()
    eof = last_instruction == '::='
    if eof :
        break
    else:
        if last_instruction.strip() == []:
            continue
        data = last_instruction + data
result = ""

def replace_random(data, find, replace):
    occurence_number_to_replace = randint(1, data.count(find))
    where = [m.start() for m in re.finditer(re.escape(find), data)][occurence_number_to_replace-1]
    before = data[:where]
    after = data[where:]
    after = after.replace(find, replace, 1)
    data = before + after
    return data

while True:
    if (instructions == [] or data == ""):
        break
    else:
        index = randint(1,len(instructions)) - 1
        regex_result = re.search(pattern, instructions[index])
        find = regex_result.group(1)
        replace = regex_result.group(2)
        if (not find in data):
            discarded_instructions.append(instructions.pop(index))
            continue
        else:
            print('data: ',data)
            print(f'instruction: {find}:=={replace}')
            if replace[0] == '~':
                data = replace_random(data, find, '')
                result += replace[1:]
            elif replace == ':::':
                replace = input('')
                data = replace_random(data, find, replace)
            else:
                data = replace_random(data, find, replace)
            while discarded_instructions != []:
                instructions.append(discarded_instructions.pop())

print('data: ',data)
print(result)
