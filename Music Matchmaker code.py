import random
from datetime import datetime

# Dictionary of concerts with ticket links and dates
concerts = {
    "p1": {  # Pop
        "artist": "FLETCHER",
        "ticket_link": "https://www.jambase.com/show/fletcher-hordern-pavilion-20241027",
        "dates": ["2024-10-27"]
    },
    "p2": {  # Pop
        "artist": "Kim Wilde",
        "ticket_link": "https://www.jambase.com/show/kim-wilde-enmore-theatre-20241019",
        "dates": ["2024-10-19", "2024-10-20"]
    },
    "p3": {  # Pop
        "artist": "Stray Kids",
        "ticket_link": "https://www.jambase.com/show/stray-kids-allianz-stadium-20241026",
        "dates": ["2024-10-26"]
    },
    "h1": {  # Hip-Hop/Rap
        "artist": "Ski Mask the Slump God",
        "ticket_link": "https://www.jambase.com/show/ski-mask-the-slump-god-enmore-theatre-20241112",
        "dates": ["2024-11-12"]
    },
    "h2": {  # Hip-Hop/Rap
        "artist": "Childish Gambino",
        "ticket_link": "https://www.jambase.com/show/childish-gambino-qudos-bank-arena-20250204",
        "dates": ["2025-02-04", "2025-02-05"]
    },
    "h3": {  # Hip-Hop/Rap
        "artist": "Karan Aujla",
        "ticket_link": "https://www.jambase.com/show/karan-aujla-qudos-bank-arena-20241025",
        "dates": ["2024-10-25"]
    },
    "r1": {  # Rock
        "artist": "Skegss",
        "ticket_link": "https://www.bandsintown.com/t/105945477?affil_code=js_skegss.com&app_id=js_skegss.com&came_from=242&utm_campaign=ticket&utm_medium=web&utm_source=widget",
        "dates": ["2024-10-18"]
    },
    "r2": {  # Rock
        "artist": "Empire of the Sun",
        "ticket_link": "https://tixel.com/au/music-tickets/2024/10/24/empire-of-the-sun-the-hordern-pa",
        "dates": ["2024-10-24"]
    },
    "r3": {  # Rock
        "artist": "The Grogan’s",
        "ticket_link": "https://tixel.com/au/music-tickets/2024/11/01/the-grogans-oxford-art-factory-s",
        "dates": ["2024-11-01"]
    },
    "e1": {  # Electronic Dance Music (EDM)
        "artist": "Dennis Ferrer",
        "ticket_link": "https://tixel.com/au/music-tickets/2024/11/16/dennis-ferrer-ivy-sydney-club-sy",
        "dates": ["2024-11-16"]
    },
    "e2": {  # Electronic Dance Music (EDM)
        "artist": "Dom Dolla",
        "ticket_link": "https://www.jambase.com/show/dom-dolla-the-domain-sydney-20241129",
        "dates": ["2024-11-29"]
    },
    "e3": {  # Electronic Dance Music (EDM)
        "artist": "Patrick Topping",
        "ticket_link": "https://www.jambase.com/show/patrick-topping-ivy-sydney-20241130",
        "dates": ["2024-11-30"]
    },
    "c1": {  # Country
        "artist": "Chris Stapleton",
        "ticket_link": "https://premier.ticketek.com.au/events/CHRSTAP24/venues/SSD/performances/ESSD2025668CS/tickets",
        "dates": ["2025-03-04", "2025-03-05"]
    },
    "c2": {  # Country
        "artist": "Luke Combs",
        "ticket_link": "https://www.jambase.com/show/tyler-childers-hordern-pavilion-20250211",
        "dates": ["2025-02-11", "2025-02-12"]
    },
    "c3": {  # Country
        "artist": "Dylan Gossett",
        "ticket_link": "https://www.jambase.com/show/dylan-gossett-metro-theatre-20241206",
        "dates": ["2024-12-06", "2024-12-07"]
    }
}

# Function to check available concerts in a specific month and year
def check_concerts_in_month(selected_month_year):
    available_concerts = []
    for key, concert in concerts.items():
        for date in concert["dates"]:
            if selected_month_year in date:
                available_concerts.append((key, concert))
    return available_concerts

# Function to get all unique months available in the concerts dictionary
def get_available_months():
    available_months = set()
    for concert in concerts.values():
        available_months.update(date[:7] for date in concert['dates'])
    return sorted(list(available_months))

# Function to list concerts for a specific month
def list_concerts_for_month(month):
    concerts_in_month = check_concerts_in_month(month)
    for key, concert in concerts_in_month:
        print(f"- {concert['artist']} - Buy tickets here: {concert['ticket_link']}")

# Disclaimer message for users
def show_disclaimer():
    print("DISCLAIMER: This concert recommendation system only covers concerts in Sydney.")
    print("The available concert dates range from October 2024 to March 2025.")
    print("Please make sure to enter a date within this range (YYYY-MM format).")
    print("Thank you for using Music Matchmaker!.")

# Function to validate the genre input
def validate_genre(genre):
    valid_genres = ['p', 'h', 'r', 'e', 'c']
    if genre not in valid_genres:
        return False
    return True

# Function to validate the date format
def validate_date(date_text):
    try:
        # making sure the date is in the correct YYYY-MM format
        datetime.strptime(date_text, '%Y-%m')
        return True
    except ValueError:
        return False

# Main loop to allow retrying
def main():
    while True:
        # Show the disclaimer to user
        show_disclaimer()

        # Ask the user for their preferred genre and date (month and year)
        while True:
            preferred_genre = input("Enter your preferred genre (p = Pop, h = Hip-Hop/Rap, r = Rock, e = EDM, c = Country): ").lower()
            if validate_genre(preferred_genre):
                break
            else:
                print("Invalid genre entered. Please enter one of the following: p, h, r, e, c.")
        
        while True:
            selected_month_year = input("Enter the month and year you want to attend a concert (YYYY-MM): ")
            if validate_date(selected_month_year):
                break
            else:
                print("Invalid date format. Please enter the date in YYYY-MM format.")

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
