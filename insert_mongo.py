import pymongo
from criminal import insert_rec

mydict1 = {"ACCUSED ID":"RJ27MJ1410","NAME":"Hardik Jaroli","AGE":20,"SEX": "M","HEIGHT": 185,"EYE COLOR": "Blue","CITY": "Bangalore","NATIONALITY": "India","CRIME": "Sedition","PREVIOUS RECORD":"Clean"}
mydict2 = {"ACCUSED ID":"GJ07MJ3679","NAME":"Abhinav Chaudary","AGE":22,"SEX": "M","HEIGHT": 165,"EYE COLOR": "Black","CITY": "Ahmedabad","NATIONALITY": "India","CRIME": "Fraud","PREVIOUS RECORD":"Acuused"}
mydict3 = {"ACCUSED ID":"UP69MJ2001","NAME":"Gopal Gupta","AGE":21,"SEX": "M","HEIGHT": 150,"EYE COLOR": "Brown","CITY": "Kanpur","NATIONALITY": "Nepal","CRIME": "Road Rash","PREVIOUS RECORD":"Clean"}

insert_rec(mydict1)
insert_rec(mydict2)
insert_rec(mydict3)
