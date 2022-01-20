# PESAPAL INTERVIEW

- NAME     :Leah Ndirangu
- EMAIL    :leahndirangu95@gmail.com


## Question 1 (Web Server).
For this, the prerequisites is to have python3 installed

 Implemented a basic server using python inbuilt `http.server` package. No external dependancies are needed.

### Instructions
1. Clone repository
2. Run python3 problem.py -Get the address
3. Insert a basic file named index.html in your server directory with name
4. Insert another file of choice in the same directory
5. In your browser go to the address from step 2  above and append index.html eg [Localhost](HTTP://127.0.0.1:5000)
6. Try with the file you added
7. Send a curl POST request. ALternatively you can use [Download postman](https://www.postman.com/downloads/). The file you want to view should be in key called file_name and the content type should JSON


## Question 2 (Re-routing/forwarding communication).
Libraries needed:

- Flask

- Requests

This implements forwarding by receiving a request using flask and then forwarding it using the python request library.

The forwarding url request is a configurable variable. An improvement would be to allow the user to pass it dynamically via header or request body.

As per the current implementation, neither are the headers nor requests removed.

**Improvement**

Add assymetric key authorisation using private-public key encryption.

Rename problem2.py to app.py
In your terminal navigate to directory and run `flask run`

## Question 3 ( Diction & dictionary scrapping.)

Dependencies

- BeautifulSoup4

- Requests

This is a python function that when provided with a url returns a sorted list of unique words with counts of each.

It utilises the requests library to fetch a webpage

THe page's html contetnt is then passed on to the BeautifulSoup4 library which strips all html tags leaving us with one long sentence.
 
 Some processing is done on the sentence i.e
 
 1. Remove all new lines i.e '/n'
 2. Split the long sentence into individual words
 3. Clean the output from step 2 by removing blank words

 It then uses python inbuilt collectors. Counter package to count how many times each word occurs.
 Use set difference to find words not in the provided list

 **Improvement:**

 Provide a web interface

## Question 4 ( Markdown engine.)

 Dependencies
 - Markdown

 Instructions:


 1. In the same folder insert your mackdown file.

 2. Run `python3 problem4.py`

 3. Check the folder for the output.


 ## Question 5

Fermats near misses states that  no three integers a,b,c for n>2, satisfy the equation a $^n$ + b $^n$ = c $^n$.

Instructions:
1. Input the first digit a as num1.
2. Input the second digit b as num2.
3. Input the third digit c as num3
4. Input the fourth digit n as n
5. Obtain desired result from the system.

**Improvement**

The system can be improved by automatically detecting n>2 and giving the desired result.
