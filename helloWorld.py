def display_anime_info():
    best_selling_anime = "One Piece"
    worst_anime_to_watch = "Pupa"
    
    print("Welcome to the Anime Info Program!")
    user_input = input("Would you like to know the best-selling anime or the worst anime to watch? (best/worst): ").strip().lower()
    
    if user_input == "best":
        print(f"The best-selling anime is: {best_selling_anime}")
    elif user_input == "worst":
        print(f"The worst anime to watch is: {worst_anime_to_watch}")
    else:
        print("Invalid input. Please enter 'best' or 'worst'.")

if __name__ == "__main__":
    display_anime_info()
