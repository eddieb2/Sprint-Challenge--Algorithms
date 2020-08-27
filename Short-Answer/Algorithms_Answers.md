#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)

b) O(n*log(n))

c) O(n)

## Exercise II

Suppose that you have an n-story building and plenty of eggs. 
Suppose also that an egg gets broken if it is thrown off floor f or higher, 
and doesn't get broken if dropped off a floor less than floor f. 
Devise a strategy to determine the value of f such that the number 
of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode
AND give the runtime complexity of your solution.


///// psuedo code ///
main goal >> to find the value of f and minimize the num of broken eggs

--track the status of current egg dropped
-->this is our kill switch for the loop
egg broken starts at False 
    if the egg breaks change this to True

track num of dropped eggs
track num of broken eggs
track floor num by starting at ground level >>> level 0

loop until egg broken is true
    drop an egg
    increment dropped eggs variable
    >>
    check if egg is broken >> if true then...
        increment broken eggs variable
        set egg broken to true and this will stop the loop
    otherwise
        add 1 to the floor level // floor += 1

return the floor number, amount of dropped eggs, and how many eggs were broken. 

>> the num of eggs broken will be 1 
>> time complexity = O(n)