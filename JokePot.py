import time



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



def main():
    job_deliver("para", "punch")
    user_input()




if __name__ == '__main__':
    main()
