# CoE 163 Recommender

I have two main program files, parser.py and main.cpp. The parser program is just used to get the data from the csv file and print it so that it can be copy-pasted into a c++ program.

### Variables
We have the following variables for the c++ file. 
- movies: `map(string, vector<int>)` 
  - it has the form of `(movie title, indices of the genre that it corresponds to)`
- userx10000: `map(string, array<int, 20>)`
  - the string is the UserID of the user and the array represents the weights of the user to each genre
- pq: `priority_queue <P, vector<P>, greater<P>>`
  - this is the priority queue to place the rankings in. It has `O(log(n))` insertion time and `O(1)` retrieval time
  - `P` is given as `pair<int, string>`
    - the `int` represents the core of the movie and the `string` is its name

### Functionality

1. The user will first input the `UserID`
2. For each movie, we will compute its score with the `UserID` being the judge
   - This is done with the function `int fma(string user, string movie) -> score`
   - We will push these scores to the priority queue. Note that we push `{-fma(input, movie), movie}`. Because the priority queue is in a decreasing order, we will have the movie with the higher `score` at the top and ties will be arrange alphabetically.
3. We will then `pop()` the top 10 movies as suggested by our program to the user. 