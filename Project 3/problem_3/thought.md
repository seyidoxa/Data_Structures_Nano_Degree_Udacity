Noticed a pattern that the output is always a sequential alternation of the max elements, so I decided to use a max heap to sort the numbers. Then I popped off each number and alternated which output I appended to.

Time Complexity: O(nlog n)
Space Complexity: O(n)
