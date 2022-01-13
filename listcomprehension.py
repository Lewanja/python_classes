h_letters=[letter for letter in "humans"]
print(h_letters)

g_letters=[]
for name in  "character":
     g_letters.append(name)

print(g_letters)

#x_word=[]
#word="letters"
#x_word.append(word)
#print(x_word)

text=list(map(lambda x:x, "personality"))
print(text)

num_list=[y for y in range(30) if y%2==0 and y%3==0]
print(num_list)

obj=["Even" if x%2==0 else "Odd" for x in range(15)]
print(obj)

#nested list comprehension
transposed=[]
matrix=[[1,2,3,4],[4,6,8,10],[3,5,7,9]]

for i in range(len(matrix[1])):
     transposed_row=[]

     for row in matrix:
          transposed_row.append(row[i])
     transposed.append(transposed_row)

print(transposed)