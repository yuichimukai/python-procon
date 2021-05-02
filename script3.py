def shortest_word(string):
    string_list = string.split()
    list_min = min(string_list, key=len)
    print(len(list_min))


shortest_word(" blue yellow")
