names_list = ["bob","jimmy","max b", "bernie", "jordan", "future hendrix"] 
longest_name = ""
for x in names_list:
    if len(x) > len(longest_name):
        longest_name=x

print ("the longest name is "+ longest_name)



