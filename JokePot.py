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
    if x.lower() == 'next' or x.lower() == 'n':
        return True
    elif x.lower() == 'quit' or x.lower() == 'q':
        return False
    else:
        print("I don't understand, please enter 'next' or 'quit'")
        return next_joke()


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

        Note: The function does NOT take care of pagination!
        Note: there might be a cleaner way to combine this method with deliver_joke_from_file().
            But I prefer this because it is more bug-free and test-friendly.
    '''
    # get the json of the reddit posts.
    # Regarding the details of the json, please check the link below.
    reddit_posts = requests.get(
        "https://www.reddit.com/r/dadjokes.json", headers={'User-agent': 'your bot 0.1'})
    data = reddit_posts.json()

    first_joke = True
    for row in data["data"]["children"]:
        title_first_world = row["data"]["title"].split(' ', 1)[0]

        if row["data"]["over_18"]:
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


def deliver_joke_from_reddit_pagination():
    '''
        This function works exactly the same as deliver_joke_from_reddit().
        The only difference is that this function DOES take care of pagination!

        Since Pagination is not required for this project, feel free deliver_joke_from_reddit()
        instead of this.
    '''
    # get the json of the reddit posts.
    # Regarding the details of the json, please check the link below:
    # https://www.reddit.com/r/dadjokes.json

    page_number = 0  # Which page we are currently on. Starts at 0.
    # Refers to the "after" string that is used to transfer to the next page.
    after_string = ""
    # Used to determine if the user wants to quit, thus terminate while loop.
    quit_jokepot = False
    while(True):
        # If-Else decides which weblink we should move to.
        if page_number == 0:
            reddit_posts = requests.get(
                "https://www.reddit.com/r/dadjokes.json", headers={'User-agent': 'your bot 0.1'})
        else:
            reddit_posts = requests.get(
                f"https://www.reddit.com/r/dadjokes.json?count={25 * page_number}&after={after_string}",
                 headers={'User-agent': 'your bot 0.1'})

        data = reddit_posts.json()
        after_string = data["data"]["after"]
        first_joke = True

        for row in data["data"]["children"]:
            title_first_world = row["data"]["title"].split(' ', 1)[0]

            if row["data"]["over_18"]:
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
                quit_jokepot = True
                break
        page_number += 1
        if quit_jokepot:
            break

    time.sleep(1)
    print("\nno more jokes today, go back to study CS")


def main():
    '''
        Main method: to check how many arguments user has provided:
            One argument - deliver_joke_from_reddit_pagination()
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
        '''
        Note: One can change the below function to deliver_joke_from_reddit()
        if one does not want the pagination functionality.
        '''
        deliver_joke_from_reddit_pagination()


if __name__ == '__main__':
    main()
