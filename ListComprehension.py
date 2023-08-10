'''[list comprehension]: Given a list of strings, create a new list that contains only the
strings with more than 5 characters using list comprehension.'''

list = ["Italy", "Myanmar", "Nepal", "USA", "China", "Veitnam"]
result_list = [word for word in list if len(word) > 5]
print(result_list)

'''[list comprehension] Given two lists of integers, create a list that contains the
product of each element of the first list with the corresponding element in the
second list using list comprehension.'''

list1 = [1, 2, 3, 4]
list2 = [10, 11, 15, 12]
product_list_items = [list1[i] * list2[i] for i in range(len(list1))]
print(product_list_items)