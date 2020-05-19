from sys import argv 
script, input_file = argv

def print_all(f):
    print(f.read())
    
#this method will bring the cursor to the line the programer disires
def rewind(f):
    f.seek(0)
    
def rewind_to(f):
    f.seek()
    
def print_a_line(line_count, f):
    print(line_count, f.readline())
    
current_file = open(input_file)

print("First let's print the whole file: \n")

print_all(current_file)

print("Now let's rewind, kind of like a tape: \n")

rewind(current_file)

print("Let's print three lines: \n")

current_line = 1 
print_a_line(current_line, current_file)

current_line = current_line + 1 
print_a_line(current_line, current_file)

current_line = current_line + 1 
print_a_line(current_line, current_file)