names_list = ['bob','jimmy','max b', 'bernie', 'jordan', 'future hendrix']
count=0
s_count =0
even_number=[]


odd_number =[]

def split_name(names):
    for x in names:
        if ((len(x)%2)==0):
            even_number.append(x)
        elif ((len(x)%2)==1):
            odd_number.append(x)



split_name(names_list)

print(odd_number)
print(even_number)

for x in even_number:
    x = x.replace(x[0],'b')
    even_number[count] = x
    
    count+=1

for x in odd_number:
    x = x.replace(x[0],'c')
    odd_number[s_count] = x
    
    s_count+=1


print(odd_number)
print(even_number)