# This function allows users to enter thier zipcodes and find other users with the same zip code or around the same area
def SquashMate():
    # Dictionary to store user profiles (key: zip code, value: user profile)
    user_profiles = {
        "12345": {"name": "User1", "email": "user1@example.com"},
        "12346": {"name": "User2", "email": "user2@example.com"},
        "67890": {"name": "User3", "email": "user3@example.com"},
        # Add more profiles as needed
    }

    UsersOnline = ["MoBanz","LuB","Bennie Ben","Mymom","KayPinkie", "LifeIsGood"]
    
    
    # Ask the current user for their zip code
    current_user_zip = input("Enter zip code: ")
    
    # Check if there's a user with the same zip code
    if current_user_zip in user_profiles:
        # Retrieve the profile of the user with the same zip code
        matching_user_profile = user_profiles[current_user_zip]
    
        # Display the matching user's profile
        print(f"Players around you:\nName: {matching_user_profile['name']}, Email: {matching_user_profile['email']}")

    
    print("These are more players around you")
    for user in UsersOnline:
        print(user)
            
    
    # Ask the user if they want to make a connection
    make_connection = input("Do you want to make a connection with this player? (yes/no): ").lower()
    
    if make_connection == "yes":
        
        connections = []  # This could be a database or another data structure 
        connections.append(matching_user_profile)
            # For now, let's print a connection message
        print(f"A connection request has been sent to {matching_user_profile['name']}.")
    else:
            # Find and display profiles of users with similar zip code prefixes
        similar_zip_users = [profile for zip_code, profile in user_profiles.items() if zip_code.startswith(current_user_zip[:3])]
    
        if similar_zip_users:
                # Display profiles of users with similar zip codes
                print("Here are other players around you:")
                for user in similar_zip_users:
                    print(f"Name: {user['name']}, Email: {user['email']}")
        else:
                print("No users around found.")
      
    

    SearchAgain = True

    while SearchAgain:
        SearchAgain = input("Do you want to search again? (yes/no): ").lower()
        if SearchAgain == "yes":
            SquashMate()
            break 
        elif SearchAgain == "no":
            print("Thank you for using SquashMate!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            
            
    


# invokes the function
SquashMate()

