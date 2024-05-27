def display_anime_info():
    # Define the best-selling anime and the worst anime to watch
    best_selling_anime = "One Piece"
    worst_anime_to_watch = "Pupa"
    
    # Welcome message
    print("Welcome to the Anime Info Program!")
    
    # Prompt the user for input
    user_input = input("Would you like to know the best-selling anime or the worst anime to watch? (best/worst): ").strip().lower()
    
    # Check the user's input and respond accordingly
    if user_input == "best":
        # If the user wants to know the best-selling anime
        print(f"The best-selling anime is: {best_selling_anime}")
    elif user_input == "worst":
        # If the user wants to know the worst anime to watch
        print(f"The worst anime to watch is: {worst_anime_to_watch}")
    else:
        # If the user enters an invalid option
        print("Invalid input. Please enter 'best' or 'worst'.")

# Main guard to ensure the script runs only if it is executed directly
if __name__ == "__main__":
    display_anime_info()
