"""You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
Using this find out,

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
"""


heros=['spider man','thor','hulk','iron man','captain america']
print(heros)
# Question 1: Length of the list
print(len(heros))

# Question 2: Add 'black panther' at the end of this list
a = 'Black Panther'
heros.append(a)
print(heros)

# Question 3: You realize that you need to add 'black panther' after 'hulk', so remove it from the list first and then add it after 'hulk'
heros.remove('Black Panther')
heros.insert(3,'Black Panther')
print(heros)

# Question 4: Remove Thor and Hulk from list and replace them with Doctor Strange
heros[1:3]=['Docter Strange']
print(heros)

# Question 5: Sort the heros list in alphabetical order
sort = sorted(heros)
print(sort)

