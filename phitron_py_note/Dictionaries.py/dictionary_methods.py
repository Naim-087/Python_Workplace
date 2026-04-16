student ={
  "Name":"Naim Islam",
  "Age" :21,
  "Academic inst. ":{#nested dict
      "Primary":"DGC",
      "Higher Secondary":"SASFM",
      "Secondary":"EUSC",
      "Undergrad":"DIU",
  },
  "reslt":{#nested dict
      "1st":5.00,
      "2nd":5.00,
      "3rd":"Unknown"
  }
}
print(len(student))#len of dic-->4
print(student.keys())#all keys of dict.
print(student.values())#all dict values 
print(student["Academic inst. "].values())#print specific dict values
#return key:val pairs as tupples
print(student.items())
print(student.get("Name"))#naim islam
new_dict={"Name":"Unknown"}
student.update(new_dict)
print(student)#name updated on main dict

