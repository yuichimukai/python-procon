def shortest_word(string):
    string_list = string.split()
    list_min = min(string_list, key=len)
    return len(list_min)


end

shortest_word("red blue yellow")
