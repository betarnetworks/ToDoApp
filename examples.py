filenames = ['experiments/filedoc.txt',
             'experiments/filepresentation.txt',
             'experiments/filereport.txt']

for fil in filenames:
    file = open(fil, 'r')
    content = file.readline()
    print(content)
    file.close()
# examples of list comprehension
filenames = ['1.doc','1.report', '1.presentation']
filenames = [filename.replace('.','-')+'.txt' for filename in filenames]

# examples of list comprehension with read files
file = open('todos.txt', 'r')
todos = file.readlines()
file.close()
new_todos =[item.strip('\n') for item in todos]

# examples of list comprehension with
user_names = [len(name) for name in user_names]
print(user_names)

# examples of list comprehension with

names = ["john smith", "jay santi", "eva kuki"]
names = [ name.title() for name in names]
print (names)
# examples of list comprehension with
user_entries = ['10', '19.1', '20']
user_entries = [float(entrie) for entrie in user_entries]

# examples of list comprehension with

temperatures = [10, 12, 14]
temperatures = [str(i) + '\n' for i in temperatures]
file = open("file.txt", 'w')

file.writelines(temperatures)