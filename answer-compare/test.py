list_of_answers = []

def header():
    print("------------------------------")
    print("------------------------------")
    print("Welcome to the Answer Comparer")
    print("------------------------------")
    print("------------------------------")


def create_list():
    with open("answers.txt") as f:
        for line in f:
            just_data = line.strip()
            list_of_answers.append(just_data)
    print(list_of_answers)

header()
create_list()
