names_list = ["bob","jimmy","max b", "bernie", "jordan", "future hendrix"] 

def get_largest_name(names):
    longest_name = ""
    for x in names_list:
        if len(x) > len(longest_name):
            longest_name=x
    return longest_name


big_name = get_largest_name(names_list)
print ("the big name is "+ big_name)


   