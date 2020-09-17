list_student_rolls = [19,27,62,24,21,2,51]
print("Insertion sort")

for i in range(j, len(list_student_rolls)):
    
    value = list_student_rolls[i]
    
    j = i-1
    
    while j >= 0 and value < list_student_rolls[j]:
        
        list_student_rolls[j+1] = list_student_rolls[j]
        j -= 1
        
    list_student_rolls[j+1] = value

print(list_student_rolls)

print("\n\nSelection sort")

for i in range(len(list_student_rolls)):
    min_val_index = i
    for j in range(i+1,len(list_student_rolls)):
        if list_student_rolls[min_val_index] > list_student_rolls[j]:
            min_val_index = j
            
    list_student_rolls[i], list_student_rolls[min_val_index] = list_student_rolls[min_val_index],list_student_rolls[i]
    
print(list_student_rolls)


print("\n\nBubble sort")

list_of_number = [9,6,4,18,100,60,50,99,80]

def bubbleSort(list_of_number):
    
    for i in range(len(list_of_number) - 1):
        
        for j in range(0, len(list_of_number)-i-1):
            
            if list_of_number[j] > list_of_number[j+1]:
                list_of_number[j], list_of_number[j+1] = list_of_number[j+1], list_of_number[j]
                
bubbleSort(list_of_number)
print(list_of_number)
