# student ={}  # create empty dictionary          
# student["name"] = "vishnu"  # add key-value pair to dictionary  
# student["age"] = 30  # add key-value pair to dictionary

student={
    "name=":"abc",
    "age":23
}
# addeing new  key-value pair to a dictionary
student["Job-title"]="Software Engineer"
print(student);# it will print dictionary => {'name': 'abc', 'age': 23, 'Job-title': 'Software Engineer'}   
#Updateding the value of a specific key in a dictionary
student["Job-title"]="Data Scientist"
print(student);# it will print dictionary => {'name': 'abc', 'age': 23, 'Job-title': 'Data Scientist'}
#deleting the value of a specific key in a dictionary
del student["Job-title"]
print(student);# it will print dictionary => {'name': 'abc', 'age': 23}
# adding List to dictionary
student["skills"]=["java","python","react"]
print(student);# it will print dictionary => {'name': 'abc', 'age': 23, 'skills': ['java', 'python', 'react']}
student["skills"].append("docker")
print(student);# it will print dictionary => {'name': 'abc', 'age': 23, 'skills': ['java', 'python', 'react', 'docker']}
# adding tupple to dictionary
student["address"]=("Noida","Madhubani","Patna","Bihar","India")
print(student);# it will print dictionary => {'name': 'abc', 'age': 23, 'skills': ['java', 'python', 'react', 'docker'], 'address': ('Noida', 'Madhubani', 'Patna', 'Bihar', 'India')}
del student["address"]# delete Address 
#addeing disctionary to dictionary
student["address"]={
    "city":"Noida",
    "state":"Uttar Pradesh",
    "pincode":201301
}

# addeding  nested disctionary to dictionary
student["Education details"]={
           "B.tech":{
            "Branch":"Electrical Engineering",
            "university":"Bihar Engineering University",
            "year":2019-2023
           },
              "Intermidiate":{
            "collage":" PDKG College Andhrathardhi ",
            "board":"BSEB Board",
            "year":2016-2018
          } ,
          "10th":{
            "collage":" PDKG College Andhrathardhi ",   
            "board":"BSEB Board",       
            "year":2015-2016
          }
            
}
print("=========================== student details ===========================")
print(student)
  


