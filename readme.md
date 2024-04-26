# CoE 163 Recommender

I have two main program files, parser.py and main.cpp. The parser program is just used to get the data from the csv file and print it so that it can be copy-pasted into a c++ program.

### Variables

We have the following variables for the c++ file.

- movies: `unordered_map(string, array<int, 20>)`
  - it has the form of `(movie title, values of the vector)`
  - we use an `unordered_map` because the amortized runtime is `O(1)`
- userx10000: `unordered_map(string, array<int, 20>)`
  - the string is the UserID of the user and the array represents the `weights` of the user to each genre
- pq: `priority_queue <P, vector<P>, greater<P>>`
  - this is the priority queue to place the rankings in. It has `O(log(n))` insertion time and `O(1)` retrieval time
  - `P` is given as `pair<int, string>`
    - the `int` represents the score of the movie and the `string` is its name

### Functionality

1. The user will first input the `UserID`
2. For each movie, we will compute its score with the `UserID` being the judge
   - This is done with the function `inner_product()`
   - We will push these scores to the priority queue. Note that we push `{-inner_product(), movie}`. Because the priority queue is in a decreasing order, we will have the movie with the higher `score` at the top and ties will be arrange alphabetically.
3. We will then `pop()` the top 10 movies as suggested by our program to the user.

### Optimizations

Using the UvLE code runner, we get the following runtimes. [^1]

| Optimization | U18 | U6 | U36 | U88 |
| ------------ | --- | -- | --- | --- |
| original | 3.917 | 3.971 | 3.655 | 3.688 |
| unordered_map| 3.319 | 2.921 | 3.115 | 3.347 |
| using inner product (needed to change representation of the movie genre to a vector of bits) | 2.670 | 2.846 | 3.082 | 3.280| 
| inner product string-array map instead of string-vector | 2.773 | 3.117 | 2.558 | 3.300 |

I have found another parallelizable function called transform_reduce. However, it is not supported by the code-runner. It is a functionality offered after C++17. I will compare it to the inner_product optimization.

| Optimization | U18 | U6 | U36 | U88 |
| ------------ | --- | -- | --- | --- |
| inner product | 1.195 | 1.190 | 0.900 | 1.080 |
| transform_reduce | 1.354 | 1.006 | 1.350 |1.305 | 

There isn't really much of an improvement. I think if the genre vector is larger. We would see a benifit in parallelization. 


[^1]:  Code runner doesn't have a constant evaluation for the runtime. So the time listed here may differ once compiled and ran again in the compiler.