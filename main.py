lst = ["Mercedes" , "BMW" , "Tesla" , "Ferrari" , "Lamborghini"]

print("length of the list:", len(lst))
print("First Element:",lst[0])
print("Last Element:",lst[-1])

lst.append("Suzuki")
print("Updated list:",lst)

lst.remove("BMW")
print("Updated list:" ,lst)

lst.sort()
print("Sorted List:",lst)

lst.pop(1)
print("Popped list:",lst)

lst.reverse()
print("Reversed list:",lst)

print("Multiplication of list:",lst*2)

lst = lst[:2]
print("Sliced list:",lst)

lst.clear()
print("cleared list:",lst)

