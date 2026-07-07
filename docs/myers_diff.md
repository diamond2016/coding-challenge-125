# Myers DIFF Algorithm in plain English

**Inputs:** Two sequences, often represented as strings, let's call them `A` and `B`.

**Goal:** Find the shortest edit script that transforms sequence `A` into sequence `B`. An edit script is a sequence of operations like insertions, deletions, and substitutions.

1. **Initialize the Matrix:**
   - Create a matrix with rows representing the characters of sequence `A` and columns representing the characters of sequence `B`.
   - The matrix will have dimensions `(M+1) x (N+1)`, where `M` is the length of sequence `A`, and `N` is the length of sequence `B`.

2. **Fill in the First Row and Column:**
   - Fill in the first row (row 0) with values from 0 to `N`, representing the number of insertions required to transform an empty string into the substring of `B`.
   - Fill in the first column (column 0) with values from 0 to `M`, representing the number of deletions required to transform substring of `A` into an empty string.

3. **Fill in the Matrix:**
   - For each cell `(i, j)` in the matrix where `i > 0` and `j > 0`, calculate the edit distance from `A[0:i]` to `B[0:j]` using the following rules:
     - If `A[i-1]` equals `B[j-1]`, the value at `(i, j)` is the same as the value at `(i-1, j-1)` (no edit needed).
     - If `A[i-1]` is not equal to `B[j-1]`, the value at `(i, j)` is the minimum of:
       - The value above `(i-1, j)` plus 1 (deletion in `A`).
       - The value to the left `(i, j-1)` plus 1 (insertion in `A`).
       - The value diagonally above-left `(i-1, j-1)` plus 1 (substitution or mismatch).

4. **Trace Back the Edit Script:**
   - Start at the bottom-right corner `(M+1, N+1)` and move towards the top-left corner `(0, 0)`.
   - Follow the path of least resistance by considering the values above, to the left, and diagonally above-left.
   - As you move, keep track of the operations taken (insertion, deletion, substitution) to reach each cell.

5. **Generate the Edit Script:**
   - Once you reach the top-left corner, you've found the shortest edit script.
   - Traverse the path from the bottom-right to top-left, using the recorded operations, to generate the actual edit script.

**Result:** The edit script represents the sequence of operations needed to transform sequence `A` into sequence `B` with the minimum number of insertions, deletions, and substitutions.

Keep in mind that this is a simplified explanation of the Myers Diff Algorithm. The actual implementation may involve optimizations and additional details. The algorithm's elegance lies in its ability to efficiently find the shortest edit script while minimizing the computational resources needed.