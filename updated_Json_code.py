import json
import random

# Load the concert data from the JSON file
with open('concerts.json', 'r') as json_file:
    concerts = json.load(json_file)

# Function to check available concerts in a specific month and year
def check_concerts_in_month(selected_month_year):
    available_concerts = []
    for key, concert in concerts.items():
        for date in concert["dates"]:
            if selected_month_year == date:
                available_concerts.append((key, concert))
    return available_concerts

# Function to get all unique months available in the concerts dictionary
def get_available_months():
    available_months = set()
    for concert in concerts.values():
        available_months.update(concert['dates'])
    return sorted(list(available_months))

# Function to list concerts for a specific month
def list_concerts_for_month(month):
    concerts_in_month = check_concerts_in_month(month)
    for key, concert in concerts_in_month:
        print(f"- {concert['artist']} - Buy tickets here: {concert['ticket_link']}")

# Disclaimer message
def show_disclaimer():
    print("DISCLAIMER: This concert recommendation system only covers concerts in Sydney.")
    print("The available concert dates range from October 2024 to March 2025.")
    print("Please make sure to enter a date within this range (YYYY-MM format).")
    print("Thank you for using Music Matchmaker!.")

# Main loop to allow retrying
def main():
    while True:
        # Show the disclaimer to the user
        show_disclaimer()

        # Ask the user for their preferred genre and date (month and year)
        preferred_genre = input("Enter your preferred genre (p = Pop, h = Hip-Hop/Rap, r = Rock, e = EDM, c = Country): ").lower()
        selected_month_year = input("Enter the month and year you want to attend a concert (YYYY-MM): ")

        # Get available concerts in that month and year
        available_concerts = check_concerts_in_month(selected_month_year)

        # Check if any concerts match the genre and date
        if available_concerts:
            # Filter concerts by the chosen genre
            genre_concerts = [concert for key, concert in available_concerts if key.startswith(preferred_genre)]
            
            if genre_concerts:
                # Randomly select a concert from the filtered list
                selected_concert = random.choice(genre_concerts)
                print(f"\nYou should go to a {selected_concert['artist']} concert!")
                print(f"Buy tickets here: {selected_concert['ticket_link']}")
            else:
                print(f"\nSorry, no concerts available in the {preferred_genre} genre for {selected_month_year}.")
        else:
            available_months = get_available_months()
            print(f"\nWe don't have knowledge of concerts available for {selected_month_year}.")
            print(f"Check the Ticketek website (https://premier.ticketek.com.au/) for more options!")

            # Suggest 3 random months that have concerts available
            random_suggestions = random.sample(available_months, min(2, len(available_months)))
            print(f"Here are some other months when concerts are available:")
            for month in random_suggestions:
                print(f"\nConcerts available in {month}:")
                list_concerts_for_month(month)

        # Ask the user if they want to try again
        retry = input("\nWould you like to search for another concert? (yes/no): ").lower()
        if retry != 'yes':
            print("Thank you for using Music Matchmaker!")
            break

# Run the main loop
main()
