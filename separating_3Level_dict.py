import json
def parse_string(json_string):  
    # separate the principal values
    nest = 0
    counter_char = 0  # it will count how many ; is in the string without considering the nested dictionaries
    preclean_string = ""
    for c in json_string:
        if c == '{':
            nest += 1
        elif c == '}':
            nest -= 1
        elif nest == 0 and c == ';':
            counter_char += 1
            if counter_char%3 == 0:  # If is the third ; then i know the next word is going to be a User
                preclean_string += '_'
                continue
            preclean_string += ','
            continue
        preclean_string += c
    
    # creating the dictionary
    user_data_raw = preclean_string.split("_")
    users = {}
    #print(user_data_raw)
    for user in user_data_raw:
        data = {}
        #print(user)
        if ':' in user:
            user_key, unprocessed_user_data = user.split(':')
        else:
            unprocessed_user_data = user
            user_key = ''
        processed_data = unprocessed_user_data.split(',')        
        for element in processed_data:
            key, value = element.split("=", 1)
            if '{' in value:
                nested_dic = parse_string(value[1:-1])
                data[key[:-1]] = nested_dic
            else:
                data[key[:-1]] = value
        if user_key != '':
            users[user_key] = data
        else:
            return data

    #print(json.dumps(users, indent=2))
    return users

def update_dict(dictionary, key, update_value):
    for k in dictionary:
        if k == key:
            dictionary[k] = update_value
        elif isinstance(dictionary[k], dict):
            update_dict(dictionary[k], key, update_value)


def solution(input_string, user_index, pref_key, new_value):
    
    solution_dict = parse_string(input_string)
    #print(json.dumps(solution_dict, indent=2))
    if isinstance(user_index,int):
        user_index = 'User'+str(user_index)

    update_dict(solution_dict[user_index], pref_key, new_value)
    
    return solution_dict
    
    
    
    
string_input = "User1:Age1=21;Location1=USA;Preferences1={Food1=Italian;Sport1=Fencing};User2:Age2=30;Location2=Canada;Preferences2={Music2=Jazz;Color2=Blue}"
print(json.dumps(solution(string_input, "User1", "Location", "Chile"), indent=2))