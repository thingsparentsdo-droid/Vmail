
import time
import firebase_admin
from firebase_admin import credentials, firestore
import os
cred = credentials.Certificate("/Users/Vivaan/Downloads/vmail-6c9b7-firebase-adminsdk-fbsvc-adb9b144d3.json")
firebase_admin.initialize_app(cred)
os.system("clear")

db = firestore.client()

ref = db.collection("Vmail_Database")
mesageindex = 1
def signup(nvmail,passw,):
     na = db.collection("Vmail_Database").document(nvmail)
     na.set({
          "passtemp" : passw,
          "user_Vmail" : []
    })
while True:
    
    
    try:
        vmailthing = input("Hello. Welcome to Vmail. If you already have an account enter your Vmail. If you don't have an account Press R: ")
        curent_doc = ref.document(vmailthing)
        if vmailthing == "R"or vmailthing == "r":
             os.system("clear")
             vm = input("First Enter your new Vmail:\nyourname@Vmail.com\r")
             ref = ref.document(vm)
             check = ref.get().to_dict()
             if check is None:
                signup(vm,input("\nCome up with a secure password:\n"))
                vmailthing = vm
                os.system("clear")
                print("U're all signed up")
                break
             else:
                  input("This Vmail is already taken")
                  os.system("clear")
        else:
             curent_user_data = curent_doc.get().to_dict()
             vmailpass = input("Please enter your password: ")
             if curent_user_data["passtemp"] == vmailpass:
                for i in curent_user_data["user_Vmail"]:
                    prewiew = "\033[1m" + i["subject"] + "\033[0m | " + i["content"][0:70]
                    print(f"\n{mesageindex} | {i["sender"]} | {prewiew}\n")
                    mesageindex += 1
             mesageindex = 1
             
                 
             
             curent_user_data = curent_doc.get().to_dict()
             vmailpass = input("Please enter your password: ")
             if curent_user_data["passtemp"] == vmailpass:
                 for i in curent_user_data["user_Vmail"]:
                     prewiew = "\033[1m" + i["subject"] + "\033[0m | " + i["content"][0:70]
                     print(f"\n{mesageindex} | {i["sender"]} | {prewiew}\n")
                     mesageindex += 1
                 mesageindex = 1
                 break
             else:
                 print("Get Out Of Here Chump!")
    except Exception as e:
        print("You Chump!")
        print(e)
def Write(c,r,s):
    #try:
        r_doc = ref.document(r)
        r_r = r_doc.get().to_dict()
        r_r = r_r
        mesage = {
             "content" : c,
             "sender" : vmailthing,
             "subject" : s
        }
        r_r["user_Vmail"].insert(0,mesage)
        r_doc.set(r_r)
   
while True:
    curent_user_data = curent_doc.get().to_dict()
    os.system("clear")
    for i in curent_user_data["user_Vmail"]:
                prewiew = "\033[1m" + i["subject"] + "\033[0m | " + i["content"][0:70]
                print(f"\n{mesageindex} | {i["sender"]} | {prewiew}\n")
                mesageindex += 1
    mesageindex = 1
    option = input("N = New Message\nE = Exit\nR = Read Message\nG = VGames\n|")
    if option == "N":
         os.system("clear")
         r = input("To: ")
         s = input("\nSubject:")
         c = input("\n")
         Write(c,r,s)
    elif option == "E":
         break
    elif option == "R":
         index = int(input("\nWhich message do you want to read\n|"))
         print(f"\n{mesageindex} | {curent_user_data["user_Vmail"][index - 1]["sender"]} | {curent_user_data["user_Vmail"][index - 1]["content"]}\n")
         done = input("\nPress Enter When done\nor R to respond\n|")
         if done == "r" or done == "R":
              r = input("To: ")
              s = input("\nSubject:")
              c = input("\n")
              Write(c,r,s)
    elif option == "G":
         pass