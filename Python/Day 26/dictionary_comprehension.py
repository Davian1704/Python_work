#Letters in each word in sentence

# sentence = "I would have got a copy pasta but I'm lazy"
#
# sentence_list = sentence.split(" ")
#
# result = {word: len(word) for word in sentence_list}
#
# print(result)



#temperature conversion

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
#
# result = {day:temperature*9/5 + 32  for (day,temperature) in weather_c.items()}
# print(result)



#Panda dict thingies

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56,76,98],
}

import pandas

student_df = pandas.DataFrame(student_dict)

#Loop through rows of a data frame

for (index, row) in student_df.iterrows():
    if row.student == "Angela":
        print(row.score)