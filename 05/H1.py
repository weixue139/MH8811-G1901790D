#####################    Begining of Homework H1   by Wei Xue  ################
#Import modules:
import json
#Define functions:
#User input function:
def ask_usr_input():
    filename = input('Please enter the path to the json file:\n')
    try:
        fh = open(filename)
        data = json.load(fh)
        print('Input data structure is:')
        print(type(data))
        print('Data is:')
        print(data)
        fh.close()
        return data
    except:
        print('Cannot load file!')    

#Function to convert a string back to its original type:
def conv_back (inp_str):
    data = inp_str.split('-')[0]
    data_type = inp_str.split('-')[1]
    if data_type == 'i':
        return int(data)
    elif data_type == 'f':
        return float(data)
    elif data_type == 's':
        return str(data)
    else:
        print('Unknown data type!')

#Function to serialize a list into a string:
def serialize_list(inp_list):
    inp_str = ';'.join([str(item)+'-'+type(item).__name__[0] for item in inp_list])
    return 'type=list|data=' + inp_str

#Function to deserialize a string back to a list:
def deserialize_list(inp_str):
    return [conv_back(item) for item in inp_str.split(';') if item]
    
#Function to serialize a dictionary into a string:
def serialize_dict(inp_dict):
    inp_str = ';'.join(['{}:{}-{}'.format(k,v,type(v).__name__[0]) for k,v in inp_dict.items()])
    return 'type=dict|data=' + inp_str

#Function to deserialize a string back to a dictionary:
def deserialize_dict(inp_str):
    inp_str_list = inp_str.split(';')
    oup_dict = {}
    for item in inp_str_list:
        if item:
            (k,v) = item.split(':')
            oup_dict[k] = conv_back(v)
    return oup_dict

#Overall function to serialize either a list or a dictionary into a string:
def serialize_list_or_dict(inp_list_or_dict):
    #if input is a list:
    if type(inp_list_or_dict) == type([]):
        serialized_data = serialize_list(inp_list_or_dict)
        return serialized_data
    #if input is a dictionary:
    elif type(inp_list_or_dict) == type({}):
        serialized_data = serialize_dict(inp_list_or_dict)
        return serialized_data
    else:
        print('Invalid Input Format: Not List or Dictionary!')
        
#Overall function to deserialize a string into either a list or a dictionary:
def deserialize_list_or_dict(inp_str):
    lst_of_str = inp_str.split('|')
    type_of_data = lst_of_str[0].split('=')[1]
    data_str=lst_of_str[1].split('=')[1]
    #if input is a list:
    if type_of_data == 'list':
        deserialized_data = deserialize_list(data_str)
        return deserialized_data
    #if input is a dictionary:
    elif type_of_data == 'dict':
        deserialized_data = deserialize_dict(data_str)
        return deserialized_data
    else:
        print('Unknown Input Format!')  

#Comparison Functions:
#Compare if two lists are equal:
def compare_list (list1, list2):
    if len(list1)==len(list2) and all(item1 == item2 and type(item1) == type(item2) for item1, item2 in zip(list1, list2)):
        print('Lists are equal!')
    else:
        print('Lists are not equal!')

#Compare if two dictionaries are equal:
def compare_dict (dict1, dict2):
    if len(dict1)==len(dict2) and all(dict2[k] == v and type(dict2[k]) == type(v) for (k,v) in dict1.items()):
        print('Dictionaries are equal!')
    else:
        print('Dictionaries are not equal!')
        
#Overall function to compare two lists or dictionaries:
def my_compare(ds1, ds2):
    if type(ds1) == type(ds2):
        if type(ds1) == type([]):
            compare_list(ds1,ds2)
        elif type(ds1) == type({}):
            compare_dict(ds1,ds2)
        else:
            print('Not list or dictionary!')
    else:
        print('Not the same data structure type!')

#Function to ask user for output file name:
def ask_usr_file_name():
    return input('Please input the file name to store the serialized string:\n')

#Function to write the serialized string to the store file:
def write_str_to_file(file_name, str_to_write):
    try:
        fh = open(file_name, 'w')
        print('Writing serialized string to file\n' + file_name)
        fh.write(str_to_write)
        fh.close()
    except:
        print('Can not write to file!')
    
#Function to read the serialzed string from the store file:
def read_str_from_file(file_name):
    try:
        fh = open(file_name, 'r')
        print('Reading serialized string from file' + file_name)
        str_to_read = fh.read()
        print('The string read back from file is:')
        print(str_to_read)
        fh.close()
        return str_to_read
    except:
        print('Can not read from file!')
        
# =============================================================================
# ################################Overall Steps################################
# =============================================================================
#Ask user for a path to the json file and load load the data structure from the json file
inp_ds = ask_usr_input()

#Use serializer to convert the original data structure into a string
serialized_str = serialize_list_or_dict(inp_ds)
print('Serialzed data type is:')
print(type(serialized_str))
print('Serialized string is:')
print(serialized_str)

#Ask user for output file name
store_file_name = ask_usr_file_name()
#Write the string to a file
write_str_to_file(store_file_name, serialized_str)
#Read the string back from the file
str_from_file = read_str_from_file(store_file_name)

#Pass the string to deserialization function and restore data structure
deserialized_ds = deserialize_list_or_dict(str_from_file)
print('Deserialzed data structure is:')
print(type(deserialized_ds))
print('Data is:')
print(deserialized_ds)

#Compare the two data structures
print('Now comparing the following two data structures:')
print(inp_ds)
print(deserialized_ds)
my_compare(inp_ds, deserialized_ds)

# ============================End==============================================

