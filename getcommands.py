def get(file : str):
    class Object(object):
        pass
    with open(file, 'r') as f:
        commands = []
        commands_response = []
        for line in f.readlines():
            if line.startswith('#'):
                #ignore a line if it is a command
                pass
            else:
                if 'response' in line:
                    #if the value is a response to a command
                    print(f"Found a response for command: {line}")
                    
                    commands_response.append(line)
                else:
                    #if the value is defining a new command
                    print(f"Found a new command: {line}")
                    print(line.bub)
                    
                    commands.append(line)
                    
if __name__ == '__main__':
    get('custom-commands.txt')