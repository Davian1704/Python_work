
with open("names.txt","r") as file:
    names=file.read()
    names=names.split("\n")
    for name in names:
        with open(f"Mails/letter_for_{name}.txt","w") as email:
            email.write(f"Dear {name},\nYou have been invited blah blah blah")