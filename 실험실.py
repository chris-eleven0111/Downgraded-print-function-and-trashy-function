def upanddown(string, mode):
    
    string_list = list(string)
    sample = 0

    if mode == 1:
        for i in range(0, len(string)):
            if i % 2 == 0:
                sample = string_list[i]
                string_list[i] = sample.upper()
            elif i % 2 == 1:
                sample = string_list[i]
                string_list[i] = sample.lower()
    if mode == 0:
        for i in range(0, len(string)):
            if i % 2 == 1:
                sample = string_list[i]
                string_list[i] = sample.upper()
            elif i % 2 == 0:
                sample = string_list[i]
                string_list[i] = sample.lower()                
    new_string = ''.join(string_list)
    return new_string.replace("mnbzxc", "")

def println(*args, **kwargs):
    if "type" in kwargs:
        type = kwargs.get("type")
        if type == "horizontal":
            for i in range(0, len(args)):
                print(args[i], end='')
            return 0
        elif type == "vertical":   
            args = list(args)    
            for i in range(0, len(args)):
                args[i] = list(args[i])
                for j in range(0, len(args[i])):
                    print(args[i][j])
            return 0
        elif type == "normal":
            for i in range(0, len(args)):
                print(args[i], end=' ')
        else:
            for i in range(0, len(args)):
                print(args[i], end=' ')
    else:
        for i in range(0, len(args)):
            print(args[i], end=' ')

a = "australophytekhus"
println("My name is", a, "!!")