import time
import csv
import sys
import json
import requests

def job_deliver(parameter, punchline):
    '''
        Takes two String values and print them consecutively with a 2-sec interval

        Inputs:
            parameter - String, referring to the joke title
            punchline - String, referring to the joke answer.
    '''
    print(parameter)
    time.sleep(2)
    print("\n")
    print(punchline)

def next_joke():
    '''
        User-interactive function that takes 'next' or 'quit' to proceed:

        Outputs:
            True - if 'next'
            False - if 'quit'
            else asks user's response again.
    '''
    x = input('next or quit?')
    # TODO: handle the upper/lower cases
    if x == 'next' or x == 'n':
        return True
    elif x == 'quit' or x == 'q':
        return False
    else:
        print("I don't understand, please enter 'next' or 'quit'")
        next_joke()

def deliver_joke_from_file(filename):
    '''
        If user provides a local file's name,
        deliver jokes based on a local file(CSV).
        Delivers first joke upon called.
        Only delivers the next joke if the user replies 'next'
        Quit if user replies 'quit' or no more jokes available.

        Input:
            filename - String for the local filename
    '''
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_joke = True  # Maybe there is a more space-efficient way.
        for row in csv_reader:
            # print(row)
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

def deliver_joke_from_reddit():
    '''
        If no local file's name is provided,
        deliver jokes from reddit.
        Delivers first joke upon called.
        Only delivers the next joke if the user replies 'next'
        Quit if user replies 'quit' or no more jokes available.

        Delivers jokes with 2 more constraints:
            1. the joke must be 'over_18'
            2. the joke must start with 'Why', 'What' or 'How'

        Note: The function does not take care of pagination!
        Note: there might be a cleaner way to combine this method with the previous one.
            But I prefer this because it is more bug-free and test-friendly.
    '''
    #get the json of the reddit posts.
    #Regarding the details of the json, please check the link below.
    reddit_posts = requests.get(
        "https://www.reddit.com/r/dadjokes.json", headers={'User-agent': 'your bot 0.1'})
    data = reddit_posts.json()

    first_joke = True
    for row in data["data"]["children"]:
        title_first_world = row["data"]["title"].split(' ', 1)[0]

        if not row["data"]["over_18"]:
            continue
        if title_first_world != "Why" and title_first_world != "What" and title_first_world != "How":
            continue

        if first_joke:
            job_deliver(row["data"]["title"], row["data"]["selftext"])
            first_joke = False
            continue
        elif next_joke():
            job_deliver(row["data"]["title"], row["data"]["selftext"])
        else:
            break
    time.sleep(1)
    print("\nno more jokes today, go back to study CS")


def main():
    '''
        Main method: to check how many arguments user has provided:
            One argument - deliver_joke_from_reddit()
            Two arguments - deliver_joke_from_file(*filename)
            More than two - error and quit.
    '''
    if len(sys.argv) > 2:
        print("please provide no more than 1 jokes' file!")
        time.sleep(2)
        sys.exit()
    elif len(sys.argv) == 2:
        deliver_joke_from_file(sys.argv[1])
    else:
        deliver_joke_from_reddit()


if __name__ == '__main__':
    main()
