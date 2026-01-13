import pickle
import os


def add_car():
    cars = []
    try:
        with open("car_data.dat", "rb") as f:
            while True:
                cars.append(pickle.load(f))
    except (FileNotFoundError, EOFError):
        pass
    while True:
        cid = input("Enter Car ID: ")
        found = False
        for car in cars:
            if car['id'] == cid:
                found = True
                break
        if found:
            print("This Car ID already exists. Try another one.")
            continue
        name = input("Enter Car Name: ")
        model = input("Enter Model: ")
        price = input("Enter Price: ")
        d = {'id': cid, 'name': name, 'model': model, 'price': price}
        with open("car_data.dat", "ab") as f:
            pickle.dump(d, f)
        cars.append(d)
        print("---------- Car added successfully ----------")
        ch = input("Do you want to continue (y/n)? ")
        if ch.lower() == 'n':
            break

def display_all():
    print("\nAll Cars in Showroom:\n")
    print("Car Id\tName\tModel\tPrice")
    print("-" * 50)
    flag = False
    try:
        with open("car_data.dat", "rb") as f:
            while True:
                x = pickle.load(f)
                print(x['id'], "\t", x['name'], "\t", x['model'], "\t", x['price'])
                flag = True
    except (FileNotFoundError, EOFError):
        pass
    if not flag:
        print("---------- No Car Found ----------")

def search_car():
    c = input("Enter Car ID to be searched: ")
    flag = False
    try:
        with open("car_data.dat", "rb") as f:
            while True:
                x = pickle.load(f)
                if x['id'] == c:
                    print("\nCar Found:\n")
                    print("Car Id\tName\tModel\tPrice")
                    print("-" * 40)
                    print(x['id'], "\t", x['name'], "\t", x['model'], "\t", x['price'])
                    flag = True
                    break
    except (FileNotFoundError, EOFError):
        pass

    if not flag:
        print("---------- No Car Found ----------")

def update_car():
    cid = input("Enter Car ID to be updated: ")
    flag = False
    try:
        f = open("car_data.dat", "rb")
        g = open("temp.dat", "wb")
        while True:
            rec = pickle.load(f)
            if rec['id'] == cid:
                print("\n---------- Current Details ----------")
                print("Name:", rec['name'])
                print("Model:", rec['model'])
                print("Price:", rec['price'])
                rec['name'] = input("Enter New Name: ")
                rec['model'] = input("Enter New Model: ")
                rec['price'] = input("Enter New Price: ")
                print("\n---------- Updated Details ----------")
                print("ID:", rec['id'])
                print("Name:", rec['name'])
                print("Model:", rec['model'])
                print("Price:", rec['price'])
                flag = True
            pickle.dump(rec, g)
    except EOFError:
        pass
    except FileNotFoundError:
        print("---------- File not found ----------")
        return
    finally:
        f.close()
        g.close()
    if not flag:
        print("---------- Car not found ----------")
        os.remove("temp.dat")
    else:
        os.remove("car_data.dat")
        os.rename("temp.dat", "car_data.dat")
        print("\nCar Record Updated Successfully")

def delete_car():
    cars = []
    flag = False
    try:
        with open("car_data.dat", "rb") as f:
            while True:
                cars.append(pickle.load(f))
    except (FileNotFoundError, EOFError):
        pass
    cid = input("Enter Car ID to be deleted: ")
    with open("car_data.dat", "wb") as f:
        for car in cars:
            if car['id'] == cid:
                print("---------- Car Deleted ----------")
                flag = True
                continue
            pickle.dump(car, f)
    if not flag:
        print("---------- Car not found ----------")

def main_menu():
    while True:
        print("\n".center(50, "-"))
        print("CAR SHOWROOM MANAGEMENT SYSTEM".center(50))
        print("-" * 50)
        print("1. Add New Car")
        print("2. Display All Cars")
        print("3. Search Car by ID")
        print("4. Update Car by ID")
        print("5. Delete Car by ID")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            add_car()
        elif choice == "2":
            display_all()
        elif choice == "3":
            search_car()
        elif choice == "4":
            update_car()
        elif choice == "5":
            delete_car()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()
