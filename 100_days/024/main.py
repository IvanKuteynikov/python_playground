def read_invited_names(filename):
    """read names from file"""
    with open(filename) as f:
        names_list = []
        names = f.readlines()
        for name in names:
            name.replace('\n', '')
            names_list.append(name.strip())
        return names_list

def create_letters(filename, names_list):
    """Creates letters from a template letter with a list of names"""
    with open(filename) as f:
        starting_letter = f.read()
        for i in range(len(names_list)):
            name_invited = names_list[i]
            starting_letters = starting_letter.replace("[name]", f"{name_invited}")
            with open(f"ReadyToSend/letter for {name_invited}.txt", "w") as f:
                f.write(starting_letters)

create_letters("starting_letter.txt", read_invited_names("invited_names.txt"))