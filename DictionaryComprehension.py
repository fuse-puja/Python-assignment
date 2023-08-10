''' [dictionary comprehension] Given two lists - one containing keys and another
containing values, create a dictionary using dictionary comprehension. '''

keys = ["book_name","author","genre","released_year"]
values = ["Palpasa Cafe","Narayan Wagle","Historical Fiction","2005"]

result = {keys[i]:values[i] for i in range(0,len(keys))}
print(result)


''' [dictionary comprehension] Given a dictionary with students' names as keys and
their respective scores as values, create a new dictionary that contains only the
students who scored more than 80 using dictionary comprehension.'''

student_dict = {"Ram": 59, "Shyam": 97, "Hari":95, "Geeta":60}
high_scores = {name:score for name,score in student_dict.items() if score>80}

print(high_scores)