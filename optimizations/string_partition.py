def string_partition(s):
    last_appearance = {}  # has the last position of each word

    # Search the last time when the char appear in the string 
    for index, char in enumerate(s):
        last_appearance[char] = index
    # When the lenght  
    result = []
    end = 0
    start = 0
    for i in range(len(s)):
         end = max(end, last_appearance[s[i]])
         if i == end:
              result.append(len(s[start:i + 1]))
              start = i + 1
    return result


string = "azsdlkjaslkdjzww"
print(string_partition(string))