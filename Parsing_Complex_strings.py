import json
def parse_string(json_string):  
    # separate the principal values
    nest = 0
    preclean_string = ""
    for c in json_string:
        if c == '{':
            nest += 1
        elif c == '}':
            nest -= 1
        elif nest == 0 and c == ',':
            preclean_string += ';'
            continue
        preclean_string += c
    
    # creating the dictionary
    processed_string = preclean_string.split(";")
    result = {}
    #print(processed_string)
    for element in processed_string:
        key, value = element.split("=", 1)
        if '{' in value:
            nested_dic = parse_string(value[1:-1])
            result[key] = nested_dic
        else:
            result[key] = value
        
    return result

def update_dict(dictionary, key, update_value):
    if '(' in update_value:
        update_value = update_value.replace(";", ',')
        update_value = update_value.replace("(", '{')
        update_value = update_value.replace(")", '}')
        update_value = parse_string(update_value[1:-1])
    for k in dictionary:
        if k == key:
            dictionary[k] = update_value
        elif isinstance(dictionary[k], dict):
            update_dict(dictionary[k], key, update_value)


def solution(data, userid, key, new_value):
    # TODO: implement the solution following the task description
    # replace the ';' into ','
    data = data.replace(";", ',')
    data = data.replace("(", '{')
    data = data.replace(")", '}') 
    user_dictionary = {}
    users = data.split('\n')
    #print(users)
    for user in users:
        user_id = user[:3]
        user_data_parsed = parse_string(user[4::])
        user_dictionary[user_id] = user_data_parsed
    #print(json.dumps(user_dictionary, indent=2))
    update_dict(user_dictionary[userid], key, new_value)

    return [{user_id: data} for user_id, data in user_dictionary.items()]

input = '001,Name=John,Address=(Street=Main St;City=NY;Zip=10001),Email=john@gmail.com\n002,Name=Jane,Address=(Street=2nd St;City=LA;Zip=90001),Email=jane@hotmail.com'
correct = [{'001': {'Name': 'John', 'Address': {'Street': 'Main St', 'City': 'NY', 'Zip': '10001'}, 'Email': 'john@gmail.com'}}, {'002': {'Name': 'Jane', 'Address': {'Street': '3rd Ave', 'City': 'SF', 'Zip': '94101'}, 'Email': 'jane@hotmail.com'}}]
print(json.dumps(solution(input, '002', 'Address', '(Street=3rd Ave;City=SF;Zip=94101)'),indent=2))
print("------------- Separation ---------------")
print(json.dumps(correct,indent=2))
