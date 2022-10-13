import time

print("*****************  Haliçbank  *****************")
time.sleep(0.5)
print("Welcome ismail murat")

ismailHesap = {
'Name': 'ismail murat',
'ID': '20091000055',
'password': 9653,
'money1': 1000
}

newHesap = {
"Name": "Ahmet",
"ID": "123456789012"
}

password = 9653
money1 = 1000
login = False
sayac = 3

while True:
      if login == False:
            passwd = int(input("password:"))
            if passwd == password:
                  login = True
                  print("Choose an action:\n"
                        "[1] Deposit\n"
                        "[2] Withdraw money\n"
                        "[3] Send money\n"
                        "[4] Info\n"
                        "[5] Exit")

                  choose = int(input("Your transaction:"))

                  if choose == 1:
                        yatirilacak_tutar = int(input("How much money do you want to deposit:"))
                        money1 = money1 + yatirilacak_tutar
                        time.sleep(0.5)
                        print(f"Your balance : {money1} tl")
                        break
                  elif choose == 2:
                        cekilecek_tutar = int(input("How much money do you want to withdraw:"))
                        if cekilecek_tutar < money1:
                              money1 = money1 - cekilecek_tutar
                              time.sleep(0.5)
                              print(f"Your balance : {money1} tl")
                              break
                        else:
                              print("Invalid transaction. Insufficient balance")
                              break
                  elif choose == 3:
                        gonderilecek_tutar = int(input("How much would you like to send:"))
                        ID = int(input("İban number:"))
                        if gonderilecek_tutar < money1:
                              money1 = money1 - gonderilecek_tutar
                              time.sleep(0.5)
                              print(f"Your balance : {money1} tl")
                              break
                        else:
                              print("Invalid transaction. Insufficient balance")
                              break
                  elif choose == 4:
                        time.sleep(0.5)
                        print(ismailHesap)
                        break
                  elif choose == 5:
                        exit = str(input("Press x to exit"))
                        time.sleep(0.5)
                        print("Thank you for choosing us."
                              "Hope to see you again...")
                        break
                  else:
                        print("You made a mistake. Try again.")
                        break
            else:
                  sayac -= 1
                  if sayac <= 0:
                        print("Your card is blocked. Please contact the bank...")
                        break