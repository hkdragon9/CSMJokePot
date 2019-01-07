# CSMJokePot
CSM Tech Committee Project
This project is a small take-home individual project assigned by the CSM Tech Committee in January 2019. 
The project's spec is here:
https://github.com/csmberkeley/tech-comm-takehome-exercise

### Introduction
As a brief summary, the JokePot is a program that can tell jokes with the following procedures:
1. Deliver prompt
2. Wait 2s
3. Deliver punchline
4. Wait for user input
    - if “next”, goto 1.
    - if “quit”, exit program
    - else, print error message and wait for new input
5. Exit when no more jokes to tell

The JokePot can only two valid types of inputs: with a local file or without one.
1. If the user has a local file, the JokePot will deliver jokes from it.
2. Otherwise, the JokePot will find jokes from online Reddit posts.


## Notes:
1. In part 2, the job is to find jokes from Reddit posts if the user does not provide a local joke file. 
  The Reddit posts' JSON data are extracted from: 
  https://www.reddit.com/r/dadjokes.json.
  
   The link above only shows the top 25 posts from /r/dadjokes. The original web page is:
   https://www.old.reddit.com/r/dadjokes
   
2. In part 2, if the JokePot extracts jokes from Reddit, there are two constraints when choosing the jokes:
    - Safe for Work only (filter out posts where `over_18` is True)
    - Start with a question (filter out posts whose post titles don't start with "Why", "What" or "How")

3. (MOST IMPORTANT) Pagination is not required in the spec. 
  However, without it, JokePot can only "scan" the top 25 jokes from Reddit.
  Thus I implemented two functions:
    - deliver_joke_from_reddit(): The one that does not deal with pagination and thus will terminate if it scans all 25 jokes.
    - deliver_joke_from_reddit_pagination(): The one that can "turn" pages. Unless the user chooses to "quit" (or it runs through all Reddit jokes), it will never terminate. Credit to Mudit who gives me a hint about how to implement this functionality.
    The only change that needs to switch between these two functionalities is in the main method. 
