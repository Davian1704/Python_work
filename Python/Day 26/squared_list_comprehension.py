# squared numbers
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#
# squared_numbers = [pow(number,2) for number in numbers]
#
# print(squared_numbers)

#even numbers

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#
# result = [number for number in numbers if number%2==0]
#
# print(result)

#Common numbers in 2 files

file1=open("file1.txt","r")
file2=open("file2.txt","r")

numbers1=file1.read()
numbers2=file2.read()

numbers1=numbers1.split("\n")
numbers2=numbers2.split("\n")

result = [number for number in numbers1 if number in numbers2]
print(result)