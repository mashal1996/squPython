#!/usr/bin/env python2.7 

import urllib2
#link to the website
url="https://www.squ.edu.om/Portals/21/section.htm"

#read info from the website
req= urllib2.Request(url)
read=urllib2.urlopen(req).read()

#reading the date and time
time=read.split('\n')[20]

#split header and footer to remove unwanted information
read='\n'.join(read.split('\n')[23:-14])

#split college 
ReadSection=read.split('\n\n')

#ceate lists to save the certain information
x=[]
college=[]
course=[]
section=[]
name=[]
taken=[]
Max=[]

#store all data row by row
for i in range(len(ReadSection)):
   x.append('\n'.join(ReadSection[i].split('\n')[2:]))
fullSection=('\n'.join(x)).split('\n')

#store data to the lists
for n in range(len(fullSection)):
    college.append(fullSection[n].split()[0])
    course.append(fullSection[n].split()[1])
    section.append(fullSection[n].split()[2])
    name.append(fullSection[n][18:38])
    taken.append(fullSection[n].split()[-4])
    Max.append(fullSection[n].split()[-1])

#read avaliable elective  
r=open("elective.txt","r")
s= r.read().split()

print "1. search\n2. available elective"
key=input("Enter the number: ")

if key == 1 :
    course_key=raw_input("Enter the course: ")
    for n in range(len(course)):
        if course[n]==course_key.upper():
            print college[n]+"\t"+course[n]+"\t"+section[n]+"\t"+name[n]+"\t"+taken[n]+"/"+Max[n]

elif key == 2 :
    print "University Elective Available"
    for m in range(len(s)):
        for n in range(len(course)):
            if course[n]==s[m].upper():
                if int(taken[n])<int(Max[n]):
                    print college[n]+"\t"+course[n]+"\t"+section[n]+"\t"+name[n]+"\t"+taken[n]+"/"+Max[n]
else :
    print "wrong input"

#print time
print"TIME:"+time





