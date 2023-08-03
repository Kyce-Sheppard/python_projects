from openpyxl import Workbook, load_workbook
import os

wb = load_workbook("C:\Documents\my_novel_library.xlsx")
ws = wb.active
library = "C:\Documents\my_novel_library.xlsx"

def add_book():
    title = input("What is the title of the book? ")
    length = input("How long is the book? ")
    genre = input("What genre is the book? ")
    status = input("What is your reading status? (Not started, reading, finished)").lower()
    if status == 'finished':
        review = input("What is your review of the book? ")
    else:
        review = None
    book_entry = [title.title(), length, genre.title(), status.title(), review]
    ws.append(book_entry)


def view_library(status=None, review=None, genre=None):
    os.startfile(library)

while True:
    mode = input("Hello! Would you like to add a book or view the library? (add, view) Press 'q' to quit ")

    if mode == 'q':
        break
    if mode == 'add':
        add_book()
        wb.save("C:\Documents\my_novel_library.xlsx")
    elif mode == 'view':
        view_library()
    else:
        print("Invalid Mode")
        continue