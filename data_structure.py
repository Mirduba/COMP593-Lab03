# Defining complex data structures
def main():
    student_details = {
        'full_name': "Mirudhu bashini",
        'student_id': 10274143,
        'pizza_toppings':[
            'PineApple',
            'SauSage',
            'PePPeroni'
        ],
        'movies': [
            {
                'title':'Dune',
                'genre':'sci-fi',
            },
            {
                'title':'The Hangover',
                'genre': 'comedy',
            },
        ]
    }
    
    # Add another movie to the Data Structure
    new_movies ={
        'title': 'The Lord of the Rings!',
        'genre': 'fantasy movies',
    }
    student_details['movies'].append(new_movies)

    # Use a function to addd pizza toppings to the data structure
    # Accept two parameters and tuple the pizza toppings
    new_pizza_toppings = ('Bacon', 'Hot Peppers')
    print_name_id(student_details)
    pizza_bullet(student_details)
    new_pizza_toppings_function(student_details,new_pizza_toppings)
    pizza_bullet(student_details)
    print_movie_genres(student_details)
    print_movie_titles(student_details)

# Pizza toppings function
def new_pizza_toppings_function(student_details, new_pizza_toppings):
    student_details['pizza_toppings'].extend(new_pizza_toppings) # Append pizza toppings to tuple 
    student_details['pizza_toppings'].sort() # Sort all pizza toppings alphabetically
    # Convert all pizza toppings to lowercase
    for i,s in enumerate(student_details['pizza_toppings']):
        student_details['pizza_toppings'][i] = s.lower()

# Use a function to print student name and id
def print_name_id(student_details):
    print_name = f"My name is {student_details['full_name']}, but you can call me Ms.{student_details['full_name'].split()[0]}"
    print_id = f"My student ID is {student_details['student_id']}"
    print(print_name)
    print(print_id)

# Use a function to print a bullet list of pizza toppings
def pizza_bullet(student_details):
    print("\nMy favourite pizza toppings are\n")
    for s in student_details['pizza_toppings']:
        print(f"- {s}")
    
# Use a function to print a comma-separated list of movie genres
def print_movie_genres(student_details):
    print("\nI like to watch", end=' ')
    print(', '.join(m['genre'] for m in student_details['movies']), end='.\n')

# Use a function to print a comma-separated list of movie titles
def print_movie_titles(student_details):
    print("Some of my favourite movies are", end=' ')
    print(', '.join(m['title'] for m in student_details['movies']), end='.\n')

main()