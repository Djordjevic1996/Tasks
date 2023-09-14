#RECORD A PERSON "REGISTER"

#Create class variables
class Person:
    def __init__(x, name, age, city):
        x.name = name
        x.age = age
        x.city = city

people = []

def create_person():
    name = input ("Enter the person's name: ")
    age = input ("Enter the person's age: ")
    city = input ("Enter the person`s city: ")
    person = Person(name, age, city)
    people.append(person)
    print(f"{name} has been added to the list.")

def list_people():
    if not people:
        print("No people in the list.")
    else:
        print("People in the list:")
        for idx, person in enumerate(people):
            print(f"{idx + 1}. Name: {person.name}, Age: {person.age}, City: {person.city}")

def main():
    while True:
        print("\nOptions:")
        print("1. Create a new person")
        print("2. List people")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_person()
        elif choice == "2":
            list_people()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()