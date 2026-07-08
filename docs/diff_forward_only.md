## The class MyersDiff

### Methods
MyersDiff has the following components:

**__init__(self):** Initialize work structures:
- v[k] (coords of diagonals)
- trace (history of diags for every "edit difference" d.

**myers_traverse(self, a, b):**
Creates matrix of differences
Implements search "Snake" to fine optiomal diagonal for every d.
Returns trace: maps d to k (the chosen diagonal).

**myers_diff(self, trace, a, b):** 
Reconstruct diff from intermediate `trace`
starts from final point in trace
Backtracking along path: operations (Add, Del, Eq)
Returns list of tuples ordered correctly.

### Data structures

A. Trace
Memorizes for every level of difference d the optiomal diag k and the coord x where path stopped.
List[d] = (k, x).

B. v vector
v[k] = value of x on k diagonal.
v[k] (as dict) = x


### Implementation

This is a forward-only implementation.

It has no optimizations.

Complexity O(N^2)

Allows study of algorithm having as intermediate outout the trace.