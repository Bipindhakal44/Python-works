b = input("enter your first name: ")
i = input("enter your last name")
p = input("enter your email address here: ")
e = input("Enter a password: ")
n = input("reenter the password: ")

if e == n:
    print("Hii", b, "you've created an ola account successfully, "
                    "Now you can log into it by entering "
                    "your email id and password")
elif e != n:
    print("Sorry", b, "Your confirmation password doesn't matched, Retype it.")
    s = input("Re enter the password again")
    print(s)

f = open("you.txt", "w")
f.write(b)
f.write(i)
f.write(p)
f.write(e)
f.write(n)
f.close()

d = input("FOR LOGIN "
          "Enter your email id:"
          "")
h = input("Enter your password: "
          "")
if p == d and n == h:
    print("Welcome to the world of OLA SANSAR")
else:
    print("Check your email or password and try it again!!")
    # name password regestered no need to enter again
    # file import to compare datas
