from TomeRater import *

Tome_Rater = TomeRater()
Tome_Rater2 = TomeRater()
Tome_Rater3 = TomeRater()
#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678, 11)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345, 30)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452, 20)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938, 50)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010, 13)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000, 22)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")
Tome_Rater.add_user("David", "david@tieto.org")
Tome_Rater.add_user("Marr", "david@sadua.org")
Tome_Rater.add_user("Troll Marr", "david@computation.fi")
Tome_Rater.add_user("David Troll", "davidacomputation.org")


#Add a user with three books already read:
#Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
#Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)

Tome_Rater.add_book_to_user(nonfiction2, "david@tieto.org", 4)
Tome_Rater.add_book_to_user(nonfiction2, "david@sadua.org", 4)

#Uncomment these to test your functions:
Tome_Rater.add_user("Joni Kontturi", "kontturi@joni.com")
print("\n--------Testing change and get email commands for user:--------\n")
Tome_Rater.users["kontturi@joni.com"].change_email("joni@kontturi.com")
print(Tome_Rater.users["kontturi@joni.com"].get_email())
Tome_Rater.print_catalog()
Tome_Rater.print_users()


print("\n--------Most positive user:--------\n")
print(Tome_Rater.most_positive_user())
print("--------Highest rated book:--------\n")
print(Tome_Rater.highest_rated_book())
print("\nMost read book:\n")
print(Tome_Rater.most_read_book())
#testing user creation with used email
print("\n--------Add user with used email address:--------\n")
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
#User read book function reading test
print("\n--------User Read book function with ISBN check--------\n")
print(Tome_Rater.users["kontturi@joni.com"].read_book(book1, 3))
book20 = Tome_Rater.create_book("Double ISBN", 12345678)
Tome_Rater.print_catalog()
print("")
print("")
print("---------Content for another instances---------")
book4 = Tome_Rater2.create_book("Society of Mind", 12345678)
book5 = Tome_Rater3.create_book("Society of Mind", 12345678)
Tome_Rater2.add_user("Alan Turing", "alan@turing.com")
Tome_Rater3.add_user("Alan Turing", "alan@turing.com")

print("---------Equality check----------")
if Tome_Rater2 == Tome_Rater3:
    print("Equal contents")
else:
    print("not Equal")
if Tome_Rater2 == Tome_Rater:
    print("Equal contents")
else:
    print("not Equal")
print("---------Most read books----------")
print(Tome_Rater.get_n_most_read_books(4))
print("----------Most prolific reader---------")
print(Tome_Rater.get_n_most_prolific_readers(2))
print("---------catalog----------")
Tome_Rater.print_catalog()
print("---------most expensive----------")
print(Tome_Rater.most_expensive_book())
print("----------most 2 expensive books---------")
print(Tome_Rater.get_n_most_expensive_books(2))
print("--------worth of alan turing-----------")
print(Tome_Rater.get_worth_of_user("alan@turing.com"))
