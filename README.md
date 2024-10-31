# Music Matchmaker

**A personalized concert recommendation system for music enthusiasts.**  
Live demo not available at the moment.

---

## Table of Contents

- [General Information](#general-information)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Screenshots](#screenshots)
- [Setup](#setup)
- [Usage](#usage)
- [Project Status](#project-status)
- [Room for Improvement](#room-for-improvement)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

---

## General Information

**Music Matchmaker** is a Python-based application that recommends concerts based on user preferences for music genre and date. The system returns a personalized concert suggestion along with a link to buy tickets.

**Problem Solved:** It simplifies the concert selection process by narrowing down options to match users’ interests, reducing decision fatigue.

**Purpose:** To offer a quick and easy way for users to find concerts they’d love to attend, with recommendations tailored to genre and date.

**Why I Undertook It:** As a music lover, I wanted a tool that could help others like me discover concerts aligned with their interests in a user-friendly way.

---

## Technologies Used

- Python 3.0+
- JSON for data handling
- Python `random` module
- Python `datetime` module

---

## Features

- Personalized concert recommendations based on genre and date.
- Randomized concert suggestion if multiple options match.
- Extensive data validation for genre and date inputs.
- Suggestions for alternate months if no concerts are available on a user’s selected date.

---

## Screenshots

*Example of command-line prompt and concert recommendation.*

---

## Setup

**Requirements:**

- Python 3.0 or higher
- JSON file with concert data (or integrated data structure as per code)

No external dependencies are needed for setup. You may set up your environment by downloading the project files and running the `main.py` file directly in Python IDLE or Visual Studio Code.

---

## Usage

**Steps to Use Music Matchmaker:**

1. Run the program by opening `main.py` in your Python environment.
2. Input your preferred music genre and date (format YYYY-MM) when prompted.
3. Receive a personalized concert recommendation or suggestions for other available months.
4. Follow the provided ticket link to purchase tickets.

**Example Usage:**
```python
# Choose genre and date
Enter your preferred genre (p = Pop, h = Hip-Hop/Rap, r = Rock, e = EDM, c = Country): p
Enter the month and year you want to attend a concert (YYYY-MM): 2024-10

## Project Status
Project is: Complete, but ongoing improvements are planned to integrate more advanced features, such as real-time API data for concert availability.

## Room for Improvement 
Areas for Improvement:

Expansion of concert data to include more cities and dates.
Refinement of error messages for enhanced user clarity.

To Do:

Integrate real-time data using an API for concert information.
Add location-based recommendations for improved personalization.

## Acknowledgements
This project was inspired by the desire to streamline concert discovery.
Special thanks to my classmates and instructor for their feedback and support throughout the development process.

## Contact
Created by Heidi Fricker - feel free to reach out with questions or suggestions!
Email: heidi.i.fricker@student.uts.edu.au


---




