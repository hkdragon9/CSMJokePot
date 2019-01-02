import time
import csv
import sys
import json
import requests


def job_deliver(parameter, punchline):
    print(parameter)
    time.sleep(2)
    print("\n")
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


def deliver_joke_from_file(filename):
    # make sure to add the edge case: if the file does not exist
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_joke = True
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
    reddit_posts = requests.get(
        "https://www.reddit.com/r/dadjokes.json", headers={'User-agent': 'your bot 0.1'})
    reddit_json = reddit_posts.json()
    # print(reddit_json)
    data = reddit_json
    #data = json.dumps(reddit_json)
    first_joke = True
    # print(data["data"]["children"][0])

    for row in data["data"]["children"]:
        title_first_world = row["data"]["title"].split(' ', 1)[0]

        # if not row["data"]["over_18"]:
        #    continue

        if title_first_world != "Why" and title_first_world != "What" and title_first_world != "How":
            continue

        if first_joke:
            # print(row)
            print()
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
    #job_deliver("para", "punch")

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
