# # Q.2] Write a python program to read an entire text file.

f = open("file handling\\read.txt",mode='r')
data = f.read()
print('\n',"Reading entire text file....")
print(data)
f.close()
# #------------------------------------------------------------------------------------------------------------------

# #Q.3] Write a python program to append text to a file and display the text 
# enter_add = input("Enter data to append in txt file: ")
# f = open("file handling\\append.txt",mode='a+')
# f.seek(0) #seek is used to move cursor
# print("Before Appending:-",'\n',f.read())
# f.write(" we can use seek function to move cursor from its position while using a+ mode")
# f.write(enter_add)
# f.seek(0)
# print("After Appending",'\n',f.read())
# f.close()
# #------------------------------------------------------------------------------------------------------------------
# #Q.4] Write a python program to read first n lines of a file

# n = int(input("Enter Number of lines: "))
# f = open("file handling\\firstN.txt",mode='r')
# print(f"\nReading first {n} lines of the file.....")

# for i in range(1,n+1):
#     data = f.readline()
#     if not data:
#         print("Given number is out of range!!!")
#         break
#     print('\n',data,end="")

# f.close()

# #------------------------------------------------------------------------------------------------------------------
# #Q.5] Write a python program to read last n line of a file
# lst = int(input("Enter last n line: "))
# f = open("file handling\\lastN.txt",mode='r')
# lines = f.readlines()
# last_lines = lines[-lst:]
# print(f"\nReading last {lst} lines of the file....")
# for i in last_lines:
#     print(i,end="")
# f.close()

# #------------------------------------------------------------------------------------------------------------------
# #Q.6] Write a python program to read file line by line and store it into a list.

# lst = []
# f = open("file handling\\linebylineList.txt",mode='r')

# for i in f: 
#     lst.append(i)   #here i will iterates line by line from file and appends all txt into lst

# print("Lines stored in list....")
# print(lst)
# f.close()

# #------------------------------------------------------------------------------------------------------------------
# #Q.7] Write a python program to read file line by line and store it into a variable.
# a = ""
# f = open("file handling\\linebylineVar.txt",mode='r')

# for i in f:
#     a+=i
# print(a)
# f.close()
# #------------------------------------------------------------------------------------------------------------------
# #Q.8] Write a python program to find the longest words.
# line = "apple banana cherry watermelon orange strawberry"
# words = line.split() #split whole line into words

# max_len = 0
# longest_word = []
# for word in words:
#     length = len(word)
#     if length > max_len: #checks the len of current word
#         max_len = length
#         longest_word = [word]
#     elif length == max_len:
#         longest_word.append(word) #add the longest word to the list
# print(f"Longest word: {max_len}")
# for word in longest_word:
#     print(word)

# #------------------------------------------------------------------------------------------------------------------
# #Q.9] Write a python program to count number of lines in a text file 

# f = open("file handling\\numofline.txt",mode='r')
# count = 0
# for i in f:
#     count+=1
# f.close()

# print('\n',"Total number of lines: ",count,'\n')
# f.close()
# #------------------------------------------------------------------------------------------------------------------
# #Q.10] Write a python program to count the freqency of words in file
# f = open("file handling\\wordfrq.txt",mode='r')
# txt = f.read()
# word = txt.split()
# count = 0
# for i in word:
#     count+=1
# print(count)
# f.close()
# #------------------------------------------------------------------------------------------------------------------
# #Q.11] Write a python program to write a list to a file
# lst = ["apple","banana","cherry","watermelon","orange","strawberry"]
# f = open("file handling\\listTofile.txt",mode='w')
# for i in lst:
#     f.write(i + '\n')
# print("List to file completed.......Open listTofile.txt......")

# f.close()

# #------------------------------------------------------------------------------------------------------------------
# #Q.12] Write a python program to copy the contents of file to another file

# copy = open("file handling\\copyToanother.txt",mode='r', encoding='utf-8')
# paste = open("file handling\\pastefile.txt",mode='w', encoding='utf-8')
# data = copy.readlines()
# for i in data:
#     paste.write(i)
# print(".....Data copied successfully.....")
# copy.close()
# paste.close()

# #------------------------------------------------------------------------------------------------------------------

