import time
import csv
import sys



def job_deliver(parameter, punchline):
    print(parameter)
    time.sleep(2)
    print(punchline)



def next_joke():
    x = input('next or quit?')
    if x == 'next':
        return True
    elif x == 'quit':
        return False
    else:
        print("I don't understand, please enter 'next' or 'quit'")
        next_joke()

def deliver_joke(filename):
    #make sure to add the edge case: if the file does not exist
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_joke = True
        line_count = 0
        for row in csv_reader:
            #print(row)
            if first_joke:
                job_deliver(row[0], row[1])
                first_joke = False
                continue
            elif next_joke():
                job_deliver(row[0], row[1])
            else:
                break
        time.sleep(1)
        print("\nno more jokes today, go back to study CS")


def main():
    #job_deliver("para", "punch")

    if len(sys.argv) > 2:
        print("please provide no more than 1 jokes' file!")
        time.sleep(2)
        sys.exit()
    elif len(sys.argv) = 2:
        deliver_joke(sys.argv[1])
    else:
        




if __name__ == '__main__':
    main()
