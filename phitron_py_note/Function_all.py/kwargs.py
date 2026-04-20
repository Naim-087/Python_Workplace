'''You dont know how many named arguments will be passed
You want flexible functions
You want to handle dynamic data (like forms, configs, user info)'''


def user(**info):
    print(type(info))

    print(info)

user(name = "Mohammad Salah ",
     Club = " Liverpool",
     age =33,
     Country = "Egypt")

user(name="Ronaldo",
     club="Al nasser")

