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
    
    for element in processed_string:
        key, value = element.split("=", 1)
        if '{' in value:
            nested_dic = parse_string(value[1:-1])
            result[key] = nested_dic
        else:
            result[key] = value
        
    return result

string_dict = "A1=B1,C1={D1=E1,F1=G1},I1=J1"
print(json.dumps(parse_string(string_dict), indent = 2))
