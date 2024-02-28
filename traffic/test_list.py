#Create a list of tupples and then split it out into arrays

#MAke some tupples
t_1=(3,2)
t_2=(4,5)
t_3=(6,7)

#Add the tupples to a list
#Empty list
t_lists=[]
t_lists.append(t_1)
t_lists.append(t_2)
t_lists.append(t_3)

print(t_lists)
a_part=[]
b_part=[]
for t_list in t_lists:
    a_part.append(t_list[0])
    b_part.append(t_list[1])

print(a_part)
print(b_part)
