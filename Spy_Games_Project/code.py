# --------------
##File path for the file 
file_path 
def read_file(path):
    file = open(path,'r+')
    sentence =file.read()
    file.close()
    return sentence



sample_message = read_file(file_path)
print(sample_message)
#Code starts here


# --------------
#Code starts here
file_path_1 
file_path_2

def read_file(path):
    file = open(path,"r")
    message= file.read()
    file.close()
    return message

def fuse_msg(message_a,message_b):
    quotient =int(message_b)//int(message_a)
    return quotient

message_1 = read_file(file_path_1)
message_2 = read_file(file_path_2)
secret_msg_1= str (fuse_msg(message_1,message_2))
print(message_1)
print(message_2)
print(secret_msg_1)


# --------------
#Code starts here
file_path_3

def read_file(path):
    file = open(path,'r')
    message = file.read()
    file.close()
    return message

def substitute_msg(message_c):
    if message_c == 'Red':
        sub =  'Army General'
        return sub
    elif message_c =='Green':
        sub = 'Data Scientist'  
        return sub
    elif message_c == 'Blue':
       sub ='Marine Biologist'
       return sub
             
           


message_3 = read_file(file_path_3)
secret_msg_2 = substitute_msg(message_3)
print(message_3)
print(secret_msg_2)




# --------------
# File path for message 4  and message 5
file_path_4
file_path_5

#Code starts here

def read_file(path):
    file = open(path,'r+')
    message =file.read()
    file.close()
    return message
    
    
def compare_msg(message_d,message_e):
      a_list,b_list = [],[]
      a_list= message_d.split(" ")
      b_list = message_e.split(" ")
      c_list =[i for i in a_list if i not in b_list]
      final_msg= " ".join(c_list)
      return final_msg

message_4 = read_file(file_path_4)    
message_5 = read_file(file_path_5)
secret_msg_3 =compare_msg(message_4,message_5)

print(message_4)  
print(message_5)
print(secret_msg_3)


# --------------
#Code starts here
file_path_6

def read_file(path):
    file = open(path,"r")
    message =file.read()
    print(message)
    file.close()
    return message

def extract_msg(message_f):
  a_list,even_word=[],[]
  a_list = message_f.split(" ")
  print(a_list)
  even_word = list(filter(lambda x: True if (len(x) % 2 == 0) else False ,a_list))
  b_list=even_word
  final_msg =" ".join(b_list)
  return final_msg
  

message_6=read_file(file_path_6)
secret_msg_4 =extract_msg(message_6)
print(secret_msg_4)



# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]
final_path= user_data_dir + '/secret_message.txt'

#Code starts here

secret_msg=" ".join(message_parts)

#Function to write inside a file
def write_file(secret_msg,path):
       
#     #Opening a file named 'secret_message' in 'write' mode
    file = open(path, 'a+')

#     #Writing to the file
    file.write(secret_msg)

#     #Closing the file
    file.close()

# #Calling the function to write inside the file    
write_file(secret_msg, final_path)

#Printing the entire secret message
print(secret_msg)

#Code ends here


