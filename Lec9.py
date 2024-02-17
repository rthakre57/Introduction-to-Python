 # Working with a dictionary

students= {}
print(type(students))

students['Roll']= '20MAT100'

students['Name']= 'Jonty Singh'

students['Gender']= 'Male'

students['DOB']='19/10/1995'

print(students)

print(students.keys())

print(students.values())

print(students.items())

students = {'20MAT101':{'FirstName': 'Rajesh','MiddleName':'Kumar','Surname':
'Singh','Gender':'Male',

'Marks':{'Math':87,'Phy':69,'Chem':79,'Eng':77,'Bio':66}},
'20MAT102':{'FirstName': 'Bharat','MiddleName':'Shresth','Surname':
'Pathak','Gender':'Male',

'Marks':{'Math':78,'Phy':66,'Chem':82,'Eng':77,'Bio':

79}},

'20MAT103':{'FirstName': 'Rajesh','MiddleName':'Kumar','Surname':

'Singh','Gender':'Male','Marks':{'Math':87,'Phy':69,'Chem':79,'Eng':77,'Bio':

66}},

'20MAT104':{'FirstName': 'Neha','MiddleName':

'Kumari','Surname':'Gupta','Gender':'Female',

'Marks':{'Math':97,'Phy':99,'Chem':79,'Eng':76,'Bio':65}}
,'20MAT105':{'FirstName': 'Sarah','MiddleName':

'John','Surname':'Abraham','Gender':'Female',

'Marks':{'Math':79,'Phy':59,'Chem':89,'Eng':74,'Bio':

58}}}

students['20MAT103']['Marks']['Math']

Output:

<class 'dict'>
{'Roll': '20MAT100', 'Name': 'Jonty Singh', 'Gender': 'Male', 'DOB': '19/10/1995'}
dict_keys(['Roll', 'Name', 'Gender', 'DOB'])
dict_values(['20MAT100', 'Jonty Singh', 'Male', '19/10/1995'])
dict_items([('Roll', '20MAT100'), ('Name', 'Jonty Singh'), ('Gender', 'Male'), ('DOB', '19/10/1995')])
