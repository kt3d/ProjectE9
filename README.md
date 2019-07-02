# primes
Hello.
This is a solution to finding primes

Project Euler - #9 Primes

* The numbers we are looking for are in sequence

2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36
^ ^   ^   ^        ^      ^          ^     ^	         ^                  ^     ^

				   ^
				  15
				   1, 2, 3, 4, 5, … 15
				   3*5
				   same result as 5*3
				   turning point is nearest prime before it 3, 
				   15 is between 9 = 3*3 and 16 = 4*4
			smaller number 3, determines 15 is not prime before we get to 5 in sequence
				   Questing: Do we need to test beyond a squared integer larger 		
				                    than the number we are testing?
				   Answer: no
		 
But we don’t know if it’s the nearest prime before it until we generate a squared integer larger than the number we are testing.

If we store the prime numbers we found, we make the search more efficient, because we know that for any number made up of a non-prime (composite number), it must be non-prime also.  
Realizing this, we only have to store primes we found (I chose an “array”, a Python List) and iterate/loop through until we reach the 1st value whose square is equal to or larger than the number we are testing.  IF equal we know it has a square root, and thus NOT prime.   Otherwise it IS a prime and we add it to the array for future searches.

high_Squared < number  	  —>	continue
high_Squared == number   	—>	stop, number^2 not prime
high_Squared > number	    —>	begin loop through previously stored prime numbers “i”
	                    				if i^2 greater than number stop
			                  		  if number / i has no remainder, clean integer division, not prime
		                    			continue until i^2 is greater than number


3 cases (prime, divisible by prime,
               ^
          2*2     3*3                                     
          4        9
         4 < 7   9 < 7
         true    false
            


Sieve of Eratosthenes
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
