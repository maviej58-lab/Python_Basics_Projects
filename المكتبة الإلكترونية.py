library = []
first1 = input("Enter the name of a book you own:")
if first1:
    library.append(first1)
    sec1 = input("Enter the name of another book you own (or press 'enter' to skip)")
    if sec1:
        library.append(sec1)
        print("your library")
        print(library)
        fir2 = input("Enter the name of a book you wish to have in the future:")
        if fir2:
            wishlist = []
            wishlist.append(fir2)
            sec2 = input("Enter the name of another book you wish to have(or press'enter' to skip):")
            if sec2:
                wishlist.append(sec2)
                print("your wishlist")
                print(wishlist)
                fir3 = input("Enter the name of a book your wishlist you've acquired (or press'enter' to skip)")
                if fir3 and fir3 in wishlist:
                    wishlist.remove(fir3)
                    library.append(fir3)
                    print("updated library:")
                    print(library)
                    print("updated wishlist")
                    print(wishlist)
                    sec3 = input("Enter the name of a book from your library you wish to donate(or press'enter' to skip)")
                    if sec3 and sec3 in library:
                        library.remove(sec3)
                        print("final library after donations:")
                        print(library)
                else:
                    sec3 = input("Enter the name of a book from your library you wish to donate(or press'enter' to skip)")
                    if sec3 and sec3 in library:
                        library.remove(sec3)
                        print("final library after donations:")
                        print(library)
            else:
                fir3 = input("Enter the name of a book your wishlist you've acquired (or press'enter' to skip)")
                if fir3 and fir3 in wishlist:
                    wishlist.remove(fir3)
                    library.append(fir3)
                    print("updated library:")
                    print(library)
                    print("updated wishlist:")
                    print(wishlist)
                    sec3 = input("Enter the name of a book from your library you wish to donate(or press'enter' to skip)")
                    if sec3 and sec3 in library:
                        library.remove(sec3)
                        print("final library after donations:")
                        print(library)
    else:
        print("your library")
        print(library)
        fir2 = input("Enter the name of a book you wish to have in the future:")
        if fir2:
            wishlist = []
            wishlist.append(fir2)
            sec2 = input("Enter the name of another book you wish to have(or press'enter' to skip):")
            if sec2:
                wishlist.append(sec2)
                print("your wishlist")
                print(wishlist)
                fir3 = input("Enter the name of a book your wishlist you've acquired (or press'enter' to skip)")
                if fir3 and fir3 in wishlist:
                    wishlist.remove(fir3)
                    library.append(fir3)
                    print("updated library:")
                    print(library)
                    print("updated wishlist:")
                    print(wishlist)
                    sec3 = input("Enter the name of a book from your library you wish to donate(or press'enter' to skip)")
                    if sec3 and sec3 in library:
                        library.remove(sec3)
                        print("final library after donations:")
                        print(library)
else:
    print("you forgot to enter a name of a book")