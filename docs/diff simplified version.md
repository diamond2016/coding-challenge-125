# 🎯 Educational Version of Myers' Algorithm

**Goals:**
- Linear and readable implementation
- No optimizations
- Only forward pass
- Simple path reconstruction
- Comments explaining why each line exists
- Central data structure: V[k] = x
- Ideal for study, debugging, visualization

![Excel Chart Colors](https://analyticsempire.com/wp-content/uploads/2023/01/how-to-change-chart-colors-in-Excel-From-Page-Layout-Ribbon-and-Colors-Option-1024x572.png)
from dataclasses import dataclass

@dataclass
class Edit:
    op: str   # "match", "insert", "delete"
    char: str

def myers_diff(a: str, b: str):
    """
    Educational version of Myers' algorithm.
    - No optimization
    - Only forward pass
    - Simple path reconstruction
    """

    n, m = len(a), len(b)

    # V[k] = furthest x reached on diagonal k = x - y
    # Using a dict for educational simplicity
    V = {0: 0}

    # Track each depth level to reconstruct the path
    trace = []

    max_d = n + m  # theoretical maximum limit

    for d in range(max_d + 1):
        new_V = {}

        # Possible diagonals at depth d range from -d to +d with step 2
        for k in range(-d, d + 1, 2):

            # Choose whether to come from k-1 (delete) or k+1 (insert)
            # Myers' rule: choose the move that advances furthest
            if k == -d:
                # Can only do insert (move right)
                x_start = V[k + 1]
            elif k == d:
                # Can only do delete (move down)
                x_start = V[k - 1] + 1
            else:
                # Choose the best move
                if V[k - 1] + 1 > V[k + 1]:
                    # delete → move down
                    x_start = V[k - 1] + 1
                else:
                    # insert → move right
                    x_start = V[k + 1]

            y_start = x_start - k

            # Advance along the diagonal while characters match
            x, y = x_start, y_start
            while x < n and y < m and a[x] == b[y]:
                x += 1
                y += 1

            new_V[k] = x

            # If we've reached the end of both strings → done
            if x >= n and y >= m:
                trace.append(new_V)
                return reconstruct(a, b, trace)

        trace.append(new_V)
        V = new_V

    raise RuntimeError("Theoretically impossible to not find a diff")


def reconstruct(a: str, b: str, trace):
    """
    Educational path reconstruction.
    Follows the paper but in simplified form.
    """

    edits = []
    x, y = len(a), len(b)

    # Traverse depth levels backwards
    for d in reversed(range(len(trace))):
        V = trace[d]
        k = x - y

        # Determine which diagonal we came from
        if k == -d:
            prev_k = k + 1
            prev_x = V[prev_k]
            op = "insert"
        elif k == d:
            prev_k = k - 1
            prev_x = V[prev_k] + 1
            op = "delete"
        else:
            if V.get(k - 1, -1) + 1 > V.get(k + 1, -1):
                prev_k = k - 1
                prev_x = V[prev_k] + 1
                op = "delete"
            else:
                prev_k = k + 1
                prev_x = V[prev_k]
                op = "insert"

        prev_y = prev_x - prev_k

        # Add matches along the diagonal
        while x > prev_x and y > prev_y:
            edits.append(Edit("match", a[x - 1]))
            x -= 1
            y -= 1

        # Add the actual operation
        if op == "insert":
            edits.append(Edit("insert", b[prev_y]))
            y -= 1
        else:
            edits.append(Edit("delete", a[prev_x - 1]))
            x -= 1

    return list(reversed(edits))

    
result = myers_diff("ABCABBA", "CBABAC")
for e in result:
    print(e)

