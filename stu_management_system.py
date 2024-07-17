import os

def insert_pr():
    data = open("insert.txt", "a")
    roll = input("Enter Roll number: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    phone = input("Enter Phone No: ")
    dob = input("Enter DOB: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    student_data = roll + "  " + name + "  " + course + "  " + phone + "  " + dob + "  " + email + "  " + address + "\n"
    data.write(student_data)
    data.close()

def display_pr():
    data = open("insert.txt", "r")
    for i in data:
        r = i.strip().split("  ")
        print(r)
        print()
    data.close()

def search_pr():
    data = open("insert.txt", "r")
    x = input("Enter roll number: ")
    for d in data:
        r = d.strip().split("  ")
        if r[0] == x:
            print(r)
            break
    else:
        print("This roll number is not found in student data")
    data.close()

def delete_pr():
    old = open("insert.txt", "r")
    new = open("new_insert.txt", "w")
    x = input("Enter the roll number you want to delete: ")
    g = 0
    for data in old:
        xm = data.strip().split("  ")
        if xm[0] == x:
            g = 1
        else:
            new.write(data)
    if g == 0:
        print("Data not found")
    else:
        print("Delete successful")
    old.close()
    new.close()
    os.remove("insert.txt")
    os.rename("new_insert.txt", "insert.txt")

def update_pr():
    old = open("insert.txt", "r")
    new = open("new_insert.txt", "w")
    x = input("Enter the roll number you want to update: ")
    g = 0
    for i in old:
        data = i.strip().split("  ")
        if data[0] == x:
            g = 1
            while True:
                print("Press 0 to edit roll")
                print("Press 1 to edit name")
                print("Press 2 to edit course")
                print("Press 3 to edit phone")
                print("Press 4 to edit dob")
                print("Press 5 to edit email")
                print("Press 6 to edit address")
                print("Press e to exit")
                change = input("Enter the number: ")
                if change == "0":
                    creat = input("Create new roll number: ")
                    data[0] = creat
                elif change == "1":
                    creat = input("Create new name: ")
                    data[1] = creat
                elif change == "2":
                    creat = input("Create new course: ")
                    data[2] = creat
                elif change == "3":
                    creat = input("Create new phone: ")
                    data[3] = creat
                elif change == "4":
                    creat = input("Create new dob: ")
                    data[4] = creat
                elif change == "5":
                    creat = input("Create new email: ")
                    data[5] = creat
                elif change == "6":
                    creat = input("Create new address: ")
                    data[6] = creat
                elif change == "e":
                    break
            new.write("  ".join(data) + "\n")
        else:
            new.write(i)
    if g == 0:
        print("Not found")
    else:
        print("Update successful")
    old.close()
    new.close()
    os.remove("insert.txt")
    os.rename("new_insert.txt", "insert.txt")

print("1- Insert Record\n2- Display all records\n3- Search a particular record\n4- Delete a record\n5- Update a record")
choice = int(input("Enter the number: "))

if choice == 1:
    insert_pr()
elif choice == 2:
    display_pr()
elif choice == 3:
    search_pr()
elif choice == 4:
    delete_pr()
elif choice == 5:
    update_pr()
else:
    print("Invalid choice")
