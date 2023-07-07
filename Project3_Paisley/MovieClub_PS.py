# Paisley Samuel
# BMME 8050 , Summer Semester
# Project 3 - MovieClub_PS.py

# create dictionary
movies = {'Mary': {'Big':
    {
        'Watched': 1,
        'Rating': 'G'},
    'Superman':
        {
            'Watched': 3,
            'Rating': 'PG'},
    'Forrest Gump':
        {
            'Watched': 3,
            'Rating': 'PG-13'
        }},
    'Frank': {'Beauty and the Beast':
        {
            'Watched': 1,
            'Rating': 'G'
        },
        'Kung Fu Panda':
            {
                'Watched': 5,
                'Rating': 'G'},
        'Cinderella':
            {'Watched': 1,
             'Rating': 'G'
             }
    }
}


# define functions for each option
def display_members():
    print("Movie Club Members")
    print("=" * 15)
    for user, info in movies.items():
        print(user)
    print("=" * 15)


def display_member_info():
    name = input("Please enter member's name: ").capitalize()
    if name in movies:
        print('{:<20s}{:<20s}{:<20s}'.format('Movie', 'Watched', 'Rating'))
        print("=" * 50)
        for key, value in movies[name].items():
            print(key)
            for w, r in movies[name][key].items():
                print(str(r)),
            print()
        return
    else:
        print("Member not found. Please try again.")


def increment():
    name = input("Please enter member's name: ").capitalize()
    if name in movies:
        movie = input("Please enter the name of the movie: ").capitalize()
        if movie in movies[name]:
            movies[name][movie]['Watched'] += 1
            print("Times watched incremented")
            return
        else:
            print("Movie title not found. Please try again.")
            return
    else:
        print("Member not found. Please try again.")


def add_movies():
    name = input("Please enter member's name: ").capitalize()
    if name in movies:
        movie = input("Please enter the name of the movie: ").capitalize()
        if movie in movies[name]:
            print("Movie title already watched by", name,".")
            return
        else:
            movies[name][movie] = {}
            watched = int(input('Enter times watched: '))
            movies[name][movie]['Watched'] = watched
            rating = input('Enter movie rating: ')
            movies[name][movie]['Rating'] = rating
            print("Movie Added.")
            return
    else:
        print("Member not found. Please try again.")


def add_members():
    name = input("Please enter member's name: ").capitalize()
    if name in movies:
        print(name, "already exists in Movie Lover's Club.")
        return
    movies[name] = {}
    print(name,"has been added to the Movie Lover's Club Member list!")


# print Welcome message and menu options
print("Welcome to the Movies Lover's Club!")
while True:
    print("\n1. Display all members")
    print("2. Display all movie information for a member")
    print("3. Increment the times a specific movie was watched by a member")
    print("4. Add a movie for a member")
    print("5. Add a new member")
    print("Q. Quit\n")
    option = input("Please enter desired menu option: ").strip().upper()
    if option not in ["1", "2", "3", "4", "5", "Q"]:
        print("Invalid selection. Please try again.")
    elif option == "1":
        display_members()
    elif option == "2":
        display_member_info()
    elif option == "3":
        increment()
    elif option == "4":
        add_movies()
    elif option == "5":
        add_members()
    elif option == "Q":
        break

print("\n=" * 55)
print("Thank you for using the Movie Lover's Club application!")
