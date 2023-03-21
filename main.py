#Richard Romero
def encode(pw):
    pw_enc = ""
    for num in pw:
        num = int(num) + 3
        pw_enc += str(num)
    return pw_enc


if __name__ == "__main__":
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        opt = int(input("Please enter an option: "))

        if opt == 1:
            pw = input("Please enter your password to encode: ")
            encode(pw)  
            print(f"Your password has been encoded and stored!")
        elif opt == 2:
           pass
        elif opt == 3:
            break
