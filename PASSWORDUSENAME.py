def check_userpassword():
    student_ID = ['123', '1234']
    student_passwords = ['password', 'password1']

    while True:
        user_input = input("Enter student ID: ")

        # Check if the entered student ID is valid
        if user_input in student_ID:
            # Find the index of the student ID
            index = student_ID.index(user_input)

            # Prompt for password
            password_input = input("Enter password: ")

            # Check if the entered password matches the one in the list
            if password_input == student_passwords[index]:
                print("Welcome!")
                break
            else:
                print("Incorrect password. Try again.")
        else:
            print("Student ID not found. Try again.")
