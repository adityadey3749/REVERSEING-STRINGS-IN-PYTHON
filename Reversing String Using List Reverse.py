#REVERSE A STRING USING LIST REVERSE

def reverse_string(j):
    temporary_list = list(j)
    temporary_list.reverse()
    return ''.join(temporary_list)
    
input_string = 'Aditya Dey'
print("reverse of string using reverse is : ",reverse_string(input_string))
