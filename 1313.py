import sys

print("\n" + "="*40)
print("  PASSWORD MANAGER")
print("="*40)
print(" 1. Register new password")
print(" 2. Exit")
print("="*40)
name = input("please say your name:  ")
print (" hello Mr./Miss./Mrs." + name )
title = input ("pleae enter your title of your phone number like +98 or +356 or ext...")
phonenumber = input (" tanks " + name + " for your name now please say your phone number ")
if phonenumber.startswith (title):
    print("thanks a lot ")
else:
    sys.exit()
email = input(" thanks " + name + " now please say your e-addres ")
print("thanks a lot ")
if "@" not in email or "." not in email:
    sys.exit()
password = input("thanks a lot for your e-address now please set up a password: ")
if len(password)< 6:
    print("weak password")
elif len(password)< 10:
    print("medium password")
else:
    print("strong password!")

print("\n" + "="*40)
print("YOUR DATA SUMMERY ")
print("="*40)
print("Name : " + name)
print("="*40)
print("Phone: " + phonenumber)
print("="*40)
print("Email: " + email)
print("="*40)
print("Password: " + password)
print("="*40)
correct = input ("\n is all information is true (yes/no)")
if correct.lower() == "no":
    print("plese return and correct your information ")
    sys.exit()
save = input("DO you want to save this data as a text file (yes/no): ")
if save.lower() == "yes":
    filename = name + "_data.txt"
    with open(filename, "w") as f:
        f.write("="*40 + "\n")
        f.write("YOUR DATA SUMMARY: \n")
        f.write("="*40 + "\n")
        f.write("Name:" + name + "\n")
        f.write("Phone:" + phonenumber + "\n")
        f.write("Email:" + email + "\n")
        f.write("Password:" + password + "\n")
        f.write("="*40 + "\n")
    print("Data saved in " + filename )

print("\n registration complete!")

# question for again
again = input("\n register another? (yes/no): " )
if again.lower() != "yes":
    print("\n goodbye " + name + " ! ")
    sys.exit()
