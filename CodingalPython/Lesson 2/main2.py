#data type, slicing, User Input, typecasting, concatenation

# PART 1: Ask the club member for their details
name = input("Enter your real name, Club Member: ")
club = input("Enter your school club name: ")
 
# PART 2: Store the member's details using different data types
member_number = 8
points_earned = 9.5
event_count = 6
meeting_hours = 1.5
is_active = True
 
# PART 3: Print each detail along with its data type
print("Name:", name, "-> type:", type(name))
print("Club:", club, "-> type:", type(club))
print("Member Number:", member_number, "-> type:", type(member_number))
print("Points Earned:", points_earned, "-> type:", type(points_earned))
print("Event Count:", event_count, "-> type:", type(event_count))
print("Meeting Hours:", meeting_hours, "-> type:", type(meeting_hours))
print("Is Active:", is_active, "-> type:", type(is_active))
 
# PART 4: Typecast the numbers and true/false value into text
member_number_text = str(member_number)
event_count_text = str(event_count)
points_text = str(points_earned)
status_text = str(is_active)
 
print("Member Number as text:", member_number_text, "-> type:", type(member_number_text))
print("Event Count as text:", event_count_text, "-> type:", type(event_count_text))
print("Points as text:", points_text, "-> type:", type(points_text))
print("Status as text:", status_text, "-> type:", type(status_text))
 
# PART 5: Slice the name to create a badge code
first_three = name[0:3]
last_letter = name[-1:]
badge_code = first_three + last_letter
 
print("First 3 letters of name:", first_three)
print("Last letter of name:", last_letter)
print("Badge Code:", badge_code)
 
# PART 6: Reverse the club name using slicing
reversed_club = club[::-1]
print("Reversed Club Name:", reversed_club)
 
# PART 7: Join everything together to build the final badge message
badge_line_1 = "CLUB MEMBER " + badge_code.upper()
badge_line_2 = "ID: " + member_number_text + " | EVENTS: " + event_count_text
badge_line_3 = "POINTS: " + points_text + " | ACTIVE: " + status_text
badge_line_4 = "SECRET CLUB CODE: " + reversed_club.upper()
 
# PART 8: Print the complete school club badge
print("")
print("===== SCHOOL CLUB MEMBER BADGE =====")
print(badge_line_1)
print(badge_line_2)
print(badge_line_3)
print(badge_line_4)


