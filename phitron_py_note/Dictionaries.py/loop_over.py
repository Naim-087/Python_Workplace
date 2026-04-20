student ={
  "Name":"Naim Islam",
  "Age" :21,
  "Academic inst. ":{#nested dict
      "Primary":"DGC",
      "Higher Secondary":"SASFM",
      "Secondary":"EUSC",
      "Undergrad":"DIU",
  },
  "result" : " "
}

for x in student:
    print(student[x])

