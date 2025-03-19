import json
import os

data_file = 'library.txt'

def load_library():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    return []

def save_library(library):
    with open(data_file, 'w') as file:
        json.dump(library,file)     

def add_book(library):
    title = input('Enter the title of the Book:')
    author = input('Enter the Author of the Book:')
    year = input("Enter the Year of the Book:")
    genre = input("Enter the genre of the Book:")
    read = input("Have you read the Book? (yes/no):").lower() == 'yes'

    new_book = {
        'title':title,
        'author':author,
        'year':year,
        'genre':genre,
        'read':read
    }

    library.append(new_book)
    save_library(library)
    print(f"Book {title} Added Successfully.")

def remove_book(library):
    title = input("Enter the title of the book to remove from the library:")
    initial_length = len(library)
    library = [book for book in library if book ['title'].lower() != title] 
    if len(library) < initial_length:
        save_library(library)
        print(f"Book {title} remove successfully.")  
    else:
        print(f'Book {title} are not found in the library.') 


def search_library(library):
    search_term = input("Search by Title or Author: ").strip().lower()  # Stripping and lowercasing the input
    search_by = input("Enter the field to search by (e.g., 'title' or 'author'): ").strip().lower()

    results = []
    for book in library:
        if search_by in book:
            if search_term in book[search_by].lower(): 
                results.append(book)

    if results:
        print("Found books:")
        for result in results:
            print(result)  
    else:
        print("No books found.")


def display_all_books(library):
    if library:
        for book in library:
            status = "Read" if book['read'] else "Unread" 
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
    else:
        print('The library is empty.')        

def books_statistics(library):
    total_books = len(library)
    read_books = len([book for book in library if book ['read']])
    percentage = (read_books / total_books) * 100 if total_books > 0 else 0

    print(f'Total books: {total_books}')
    print(f'Percentage: {percentage:.2f}%')

def main():
    library = load_library()
    while True:
        print("Welcome! to your Personal Library Manager")
        print("Menu")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search by library")
        print("4. Display all books")
        print("5. Display Statistics")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_library(library)
        elif choice == '4':
            display_all_books(library)
        elif choice == '5':
            books_statistics(library)
        elif choice == '6':
            print('Exit from Library Goodbye!')
            break          
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__": 
    main()