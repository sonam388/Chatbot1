# Library Management System 

class Library():
    def __init__(s):
        s.book = {}
# 123

    def add_newBook(s):
        book_id = int(input("Enter Your Book Id : ")) 
        book_name = input("Enter Your Book Name")
        author = input("Enter Book Author Name")

        if book_id == "":
            print("Plz Enter Your Book Id")
        elif book_id in s.book:
            print("Id is Already Avalable")
            return
        s.book[book_id] = {
            "title":book_name,
            "author":author,
            "Avalable":True
        }

        print("Book Store Sucesfully")

    def ShowAllBooks(s):
        if not s.book:
            print("No Book Avalable")
            return
        for book_id , book in s.book.items():
            staus = "Avalable" if book["Avalable"] else ["Issued"]
            print(f"""
BookId : {book_id}
Title : {book["title"]}
Author : {book["author"]}
stutus : {staus}
""")
    def issued_book(s):
        book_name = input("Enter Your Book Name ")
        book_id = int(input("Enter Book id "))

        if book_id not in s.book:
            print(book_name ,"Book is not Avalable")

        if not s.book[book_id]["Avalable"]:
            print("Book is already issud")
            return

        s.book[book_id]["Avalable"] = False
        print("Book issued Sucessful")

    def return_book(s):
        book_id = int(input("Enter Book id "))
        if book_id not in s.book:
            print("Book is not Avalable")
        s.book[book_id]["Avalable"] = True
        print("Book Submit Sucessful")


obj = Library()
print("====== Welcome to Library ==========")
print("1.) Add New Book")
print("2 ) View All Book")
print("3 ) Issued Book")
print("4 ) Submit Book")
print("5 ) Exit")
while True:
    

    op = int(input("Enter Your Option "))

    if op == 1:
        obj.add_newBook()
    elif op == 2:
        obj.ShowAllBooks()
    elif op == 3:
        obj.issued_book()
    elif op == 4:
        obj.return_book()
    elif op == 5:
        break




        

# OPP

# Django / HTML , CSS