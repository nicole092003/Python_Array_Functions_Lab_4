# Nicole Thomas
# Lab01BP1.py
# January 22, 2024


def main():
    # List to store the user's registered courses

    # def course_registration():
    courses = []

    while True:
        print("\nEnter A to add course, D to drop course, or E to exit")
        choice = input("Enter your choice: ").upper()

        if choice == 'A':
            course_to_add = input("Enter the course to add: ")
            if course_to_add in courses:
                print("You are already registered in this course.")
            else:
                courses.append(course_to_add)
                courses.sort()
                print("Course added. ")
                print("Your course list:", courses)

        elif choice == 'D':
            course_to_drop = input("Enter the course to drop: ")
            if course_to_drop not in courses:
                print("You are not registered in that course.")
            else:
                courses.remove(course_to_drop)
                print("Course dropped.")
                print("Your course list:", courses)

        elif choice == 'E':
            print("Exiting the course registration system. Your final course list", courses)
            break

        else:
            print("Invalid choice. Please enter A, D, or E,")


if __name__ == '__main__':
    main()
