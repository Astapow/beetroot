def first_funk():
    def second_funk():
        print("second funk")

    return second_funk


first_funk()()
