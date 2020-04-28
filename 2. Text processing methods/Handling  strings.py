# Handling  strings
#Creating a string

String_v1 = "I am exploring NLP"
#To extract particular character or range of characters 
from string
print(String_v1[0])

#To extract exploring
print(String_v1[5:14])


#Replace “exploring” with “learning” in the above string
String_v2 = String_v1.replace("exploring", "learning")
print(String_v2)

#Concatenating two strings
s1 = "nlp"
s2 = "machine learning"
s3 = s1+s2
print(s3)

#Searching for a substring in a string
var="I am learning NLP"
f= "learn"
var.find(f) # returns index of the first match

