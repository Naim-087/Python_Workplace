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

print(student.items())