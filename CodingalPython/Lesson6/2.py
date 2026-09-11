homework = input("Have you completed your homework? (yes/no): ")
day = input("What day is it today? (e.g., Monday, Tuesday, etc.): ")

# Topic 4 - NOT operator
if not (homework == "yes"):
    print("Homework : Not done yet. Finish it before going out!")
# not-equal operator
if day != "Saturday":
    print("It is a school week day.")