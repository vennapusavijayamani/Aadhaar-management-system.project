aadhaar_db = {}
# CREATE
def create_aadhaar():
    aadhaar_no = input("Enter Aadhaar Number: ")
    if aadhaar_no in aadhaar_db:
        print("Record Already Exists")
        return
    name = input("Enter Name: ")
    address = input("Enter Address: ")
    mobile = input("Enter Mobile Number: ")
    aadhaar_db[aadhaar_no] = {
        "name": name,
        "address": address,
        "mobile": mobile
    }
    print("Record Created Successfully")
# READ
def read_aadhaar():
    aadhaar_no = input("Enter Aadhaar Number: ")
    if aadhaar_no in aadhaar_db:
        print("\nAadhaar Details")
        print("Name:", aadhaar_db[aadhaar_no]["name"])
        print("Address:", aadhaar_db[aadhaar_no]["address"])
        print("Mobile:", aadhaar_db[aadhaar_no]["mobile"])
    else:
        print("Record Not Found")
# UPDATE
def update_aadhaar():
    aadhaar_no = input("Enter Aadhaar Number: ")
    if aadhaar_no not in aadhaar_db:
        print("Record Not Found")
        return
    name = input("Enter New Name: ")
    address = input("Enter New Address: ")
    mobile = input("Enter New Mobile Number: ")
    aadhaar_db[aadhaar_no] = {
        "name": name,
        "address": address,
        "mobile": mobile
    }
    print("Record Updated Successfully")
# DELETE
def delete_aadhaar():
    aadhaar_no = input("Enter Aadhaar Number: ")
    if aadhaar_no in aadhaar_db:
        del aadhaar_db[aadhaar_no]
        print("Record Deleted Successfully")
    else:
        print("Record Not Found")
# DISPLAY ALL RECORDS
def display_all():
    if not aadhaar_db:
        print("No Records Available")
        return
    for aadhaar_no, details in aadhaar_db.items():
        print("\nAadhaar Number:", aadhaar_no)
        print("Name:", details["name"])
        print("Address:", details["address"])
        print("Mobile:", details["mobile"])
# MAIN MENU
while True:
    print("\n===== Aadhaar Management System =====")
    print("1. Create Record")
    print("2. Read Record")
    print("3. Update Record")
    print("4. Delete Record")
    print("5. Display All Records")
    print("6. Exit")
    choice = input("Enter Your Choice: ")
    if choice == "1":
        create_aadhaar()
    elif choice == "2":
        read_aadhaar()
    elif choice == "3":
        update_aadhaar()
    elif choice == "4":
        delete_aadhaar()
    elif choice == "5":
        display_all()
    elif choice == "6":
        print("Thank You")
        break
    else:
        print("Invalid Choice")