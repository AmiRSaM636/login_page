import time
# ================================================================
'''
important!!

Set your password in the "my_password" then run the code

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!Note, user input is str.!!!!!!!!!
!!!!!!!!!!Set your password to str.!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''

# my_password = ("example")
my_password = ("1")

# ================================================================
wrong_pas = False
print ("Welcome ")
username = input("User name : ")
# ================================================================
def chek_pass():
    global wrong_pas
    input_ = input("password : ")
    count = 0
    
    while my_password != input_  and count <= 3 :
        print("wrong pass, try again !")
        input_ = input("password : ")
        count = count + 1
        wrong_pas = True
        
    while my_password != input_  and count > 3 :
        print("Wrong password, try again after 5 secend !")
        time.sleep(5)
        input_ = input("password : ")
        count = count + 1
        wrong_pas = True

    if my_password == input_:
        print(True)
        print(f"Hello {username} welcome! ")
        if wrong_pas == True :
            print(f"The wrong password was entered {count} times!!")
        else:
            pass
# ==================================================================
chek_pass()