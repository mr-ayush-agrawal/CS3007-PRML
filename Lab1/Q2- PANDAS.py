import pandas as pd

df = pd.read_csv("data.csv")
print(df)

def Append():
    print("Enter the new Record")
    name = input("Enter the name")
    Acc = eval(input("Enter the Account_Number"))
    Type = eval(input("Enter the Acc_Type"))
    adhar = eval(input("Enter the Adhar_No"))
    bal = eval(input("Enter the Balance"))

    df.loc[len(df.index)] = [name, Acc, Type, adhar, bal]

    df.to_csv("data.csv")

    print("Your DataFrame After appending the record is")
    print(df)

def delAcc():
    Acc = eval(input("Enter the Account number to delete acc"))
    index = df[ (df['Account_Number'] == Acc)]

    df.drop(index, inplace=True)

    df.to_csv("./data.csv")

    print("Your DataFrame After droping the record is")
    print(df)

def Credit():
    Acc = eval(input("Enter the Account number to Cerdit acc"))
    amt = eval(input("Enter the Amount to Cerdit acc"))

    for rec in df.index():
        if df[rec]['Account_Number'] == Acc :
            df[rec]['Balance']+=amt

            print(f"Total balance of {df[rec]['Account_Number']} is {df[rec]['Balance']}")
            break

    df.to_csv("data.csv")
    
def Debit():
    Acc = eval(input("Enter the Account number to Debit acc"))
    amt = eval(input("Enter the Amount to Cerdit acc"))

    for rec in df.index():
        if df[rec]['Account_Number'] == Acc :
            if df[rec]['Balance'] < amt and df[rec]['Acc_Type'] == 'SB':
                print("Cant Debit the amount")
                break
            else :
                df[rec]['Balance']-=amt
            
                print(f"Total balance of {df[rec]['Account_Number']} is {df[rec]['Balance']}")
                break

    df.to_csv("data.csv")
    
def PrintDetails():
    Acc = eval(input("Enter the Account number to Show details"))
    for rec in df.index():
        if df[rec]['Account_Number'] == Acc :
            print(df.columns.values)
            print(df[rec])

def menu():
    print("1. Append the record")
    print("2. Delete the record")
    print("3. Credit the amount")
    print("4. Debit the amount")
    print("5. show details")
    ch = int(input("Enter your choice "))
    if ch == 1 :
        Append()
    elif ch == 2 :
        delAcc()
    elif ch == 3: 
        Credit()
    elif  ch ==4 :
        Debit()
    elif ch == 5 :
        PrintDetails()
    else :
        print("Invalid selection.... Exiting")
        exit()

while True :
    menu()