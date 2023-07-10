# personWeight = 22.54
# print(type(personWeight))
# isAlive = True
# isFemale= False
# print(type(isAlive))
# print(type(isFemale))




# mylist= ["apple", "banana", "cherry"]
# print(mylist[1][2:6])
# print(mylist[2])


# First= input("What's your first number?"  )
# Second= input("What's your second number?" )
# sum = float(First) + float(Second)
# print("sum: " + str(sum))

# First_name = "Jacob"
# print(First_name.upper())

# x= 3 >= 2
# print(x)

import mailbox


fruits = [
    'apple', 'banana', 'orange', 'grape', 'strawberry', 'watermelon', 'mango',
    'pineapple', 'kiwi', 'pear', 'cherry', 'blueberry', 'raspberry', 'lemon',
    'lime', 'peach', 'plum', 'apricot', 'pomegranate', 'coconut', 'avocado',
    'fig', 'guava', 'grapefruit', 'papaya', 'melon', 'cantaloupe', 'passionfruit',
    'dragonfruit', 'blackberry', 'raspberry', 'blackcurrant', 'cranberry',
    'gooseberry', 'kiwifruit', 'lychee', 'mangosteen', 'nectarine', 'persimmon',
    'quince', 'star fruit', 'tangerine', 'apricot', 'boysenberry', 'elderberry',
    'honeydew', 'jackfruit', 'mulberry', 'olive', 'rhubarb', 'soursop', 'ugli fruit',
    'yuzu', 'ackee', 'breadfruit', 'cherimoya', 'durian', 'feijoa', 'grapefruit',
    'kiwano', 'loquat', 'mandarin', 'pawpaw', 'plantain', 'salak', 'santol',
    'sapodilla', 'tamarillo', 'tamarind', 'ugli fruit', 'watermelon', 'ziziphus',
    'apricot', 'banana', 'coconut', 'date', 'elderberry', 'fig', 'grape', 'honeydew',
    'ilama', 'jambul', 'kiwi', 'lime', 'mango', 'nectarine', 'orange', 'papaya',
    'quince', 'raspberry', 'strawberry', 'tangerine', 'ugli fruit', 'vanilla',
    'watermelon', 'xigua', 'yangmei','zucchini'
]

# print(fruits[0:20])
# print(len(fruits))
# print(type(fruits))
# print(len(fruits[0:20]))

# fruits[3]= 'Africa'

# fruits[:2]= ['kofi', 'ama']
# print(fruits)

# fruits[0:5]= ['***','***','***','***', '***']
# print(fruits)

# fruits.insert(4,"qwerty")
# print(fruits)

# fruits.append("gari") will go to the end of the list
# print(fruits)

# .pop will take the index number to remove the item
# while .remove doesn't require an index number and delete the name of the item

# 'cantaloupe' in fruits
# change an item in a list without using the index number

# python- update Tuple
# fruits=('apple', 'banana', 'cherry','mango','pineapple','papaya')

# newFruits=list(fruits)

# newFruits[-2]= 'grape'

# print(newFruits)

# unpacking tuples
# (a,b,c,d,e,f)= fruits

# fruits = (
#     'apple', 'banana', 'orange', 'grape', 'strawberry', 'watermelon', 'mango',
#     'pineapple', 'kiwi', 'pear', 'cherry', 'blueberry', 'raspberry', 'lemon',
#     'lime', 'peach', 'plum', 'apricot', 'pomegranate', 'coconut', 'avocado',
#     'fig', 'guava', 'grapefruit', 'papaya', 'melon', 'cantaloupe', 'passionfruit',
#     'dragonfruit', 'blackberry', 'raspberry', 'blackcurrant', 'cranberry',
#     'gooseberry', 'kiwifruit', 'lychee', 'mangosteen', 'nectarine', 'persimmon',
#     'quince', 'star fruit', 'tangerine', 'apricot', 'boysenberry', 'elderberry',
#     'honeydew', 'jackfruit', 'mulberry', 'olive', 'rhubarb', 'soursop', 'ugli fruit',
#     'yuzu', 'ackee', 'breadfruit', 'cherimoya', 'durian', 'feijoa', 'grapefruit',
#     'kiwano', 'loquat', 'mandarin', 'pawpaw', 'plantain', 'salak', 'santol',
#     'sapodilla', 'tamarillo', 'tamarind', 'ugli fruit', 'watermelon', 'ziziphus',
#     'apricot', 'banana', 'coconut', 'date', 'elderberry', 'fig', 'grape', 'honeydew',
#     'ilama', 'jambul', 'kiwi', 'lime', 'mango', 'nectarine', 'orange', 'papaya',
#     'quince', 'raspberry', 'strawberry', 'tangerine', 'ugli fruit', 'vanilla',
#     'watermelon', 'xigua', 'yangmei','zucchini'
# )


# def dis_name(): 
#     print('Jacob Kondo')

# dis_name()

# def calc_body_mass(height,weight):
#     return (height*height)/weight
# print(calc_body_mass(1.7,65))

# def display_name(yourName='anonymous'):
#     return yourName
# print(display_name('jacob kondo'))
# print(display_name())

# input_db= 'passme123'
# input_password= 'passme123'

# if input_password== input_db:
#     print('password is correct you are logged in')
# else:
#     print('password is not correct please try again')

# email_db="jacobkondo4@gmail.com"
# phone_numbdb= '0544265497'
# user_namedb= 'jk'

# # input_email="jacobkondo4@gmail.com"
# # input_phone_numb= '0545265497'
# # input_user_name='jk'

# # if (input_email==email_db or input_phone_numb==phone_numbdb or input_user_name==user_namedb):
# #     if(input_email==email_db):
# #         print(f"email was used")
# #     print('Proceed to enter your password')
# # else:
# #     print('Email or phone_numb or user_name incorrect')

# def sign_in(input):
#     if input == email_db or input== phone_numbdb or input== user_namedb:
#        print(f"{input} was used, proceed to enter your password")
#     else:
#         print("not correct try again")

# sign_in('jacobkondo@gmail.com')


# def sign_in(input_email, input_phone, input_username):
#     if input_email == email_db :
#        print(f"email was used {input_email}, proceed to enter your password")
#     elif input_phone== phone_numbdb:
#         print(f'phone number was used {input_phone}, proceed to enter your password')
#     elif input_username== user_namedb:
#         print(f"username was used {input_username}, proceed to enter your password")
#     else:
#         print("not correct try again")

# sign_in('jacobkondo4gmail.com', '0544265497', 'jk') 


# personalInfor= [
#     {
#         "name": "marley",
#         "age": 20,
#         "address": {
#             "country": "Ghana",
#             "zip_code": "+233",
#             "phoneNumbers": [
#                 7777777, 
#                 900000
#             ],
#         },
#         "gender": "male",
#         "occupation": ("developer")
# }
# ]
# personalInfor[0]['occupation']='dancer'

# print(tuple(personalInfor[0]['address']['phoneNumbers']))

class Human:
    def __init__(self, name, color, height, age):
        self.name= name
        self.color= color
        self.height= height
        self.age= age
    
firstHuman= Human('kofi', 'red', '2.00', '30')
print('firstHuman:', 'name:', firstHuman.name, 'age:', firstHuman.age, 'color:', firstHuman.color, 'height:', firstHuman.height)






    
    
    
    




