import itertools
import sys
list_of_answers = []
list_of_actual_answers = []

def main():
    header()    
    create_list(input("Enter file name of your Answers : "))
    create_answer_list(input("Enter file name of the Actual Answers : "))
    print("number of answers",number_of_answers())
    compare_answers()

def header():
    print("------------------------------")
    print("------------------------------")
    print("Welcome to the Answer Comparer")
    print("------------------------------")
    print("------------------------------")


def create_list(file_name1):
    with open(file_name1) as f:
        for line in f:
            just_data = line.strip()
            list_of_answers.append(just_data)

def create_answer_list(file_name2):
    with open(file_name2) as f:
        for line in f:
            just_data = line.strip()
            list_of_actual_answers.append(just_data)   

def number_of_answers():
    i = 0
    counter = itertools.count()
    for x in list_of_answers:
        i += 1
    return i

def compare_answers():
    results = sys.stdout
    with open('output.txt','w') as f:
        sys.stdout = f
        count_equal = 0
        count_notequal = 0
        for i,j in itertools.zip_longest(list_of_answers, list_of_actual_answers):
            if i == j:
                count_equal += 1
                # print(i, j)
                print("Correct", i, j)
            else:
                count_notequal += 1
                # print(i, j)
                print("Incorrect", i, j)
        dec_results = count_equal / number_of_answers()
        percent_results = (dec_results*100)
        print("Correct : ", count_equal, "Incorrect : ", count_notequal)
        print("Final Results :", percent_results,"%")
        sys.stdout = results



if __name__ == '__main__':
    main()