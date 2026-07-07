# 🎯 Educational Version of Myers' Algorithm

**Goals:**
- Linear and readable implementation
- No optimizations
- Only forward pass
- Simple path reconstruction
- Comments explaining why each line exists
- Central data structure: V[k] = x
- Ideal for study, debugging, visualization


# 📚 Detailed Analysis of Myers' Algorithm Educational Implementation

Let me break down this implementation step-by-step for educational purposes.

---

## 🎯 **Core Concepts**

### 1. **The Problem**
We need to find the **minimum edit distance** between two strings and the actual sequence of operations (insert, delete, match) to transform one into the other.

### 2. **Key Variables**
- `a`: First string (source)
- `b`: Second string (target)
- `n = len(a)`, `m = len(b)`: Lengths
- `x`: Position in string `a`
- `y`: Position in string `b`
- `k = x - y`: **Diagonal** (difference between positions)

### 3. **The Data Structure: V[k]**
```
V[k] = furthest x reached on diagonal k
```
- `k` ranges from `-m` to `+n`
- Each diagonal represents a relationship between positions in both strings
- We track the maximum `x` (progress in string `a`) for each diagonal

---

## 🔄 **Algorithm Flow**

### **Phase 1: Forward Pass (myers_diff)**

```
For each depth d = 0, 1, 2, ...
  For each diagonal k at this depth:
    1. Choose starting position (from k-1 or k+1)
    2. Move along diagonal while characters match
    3. Store result in new_V[k]
    4. If we reached end of both strings → DONE
```

### **Phase 2: Backward Reconstruction (reconstruct)**

```
Start from end (x=n, y=m)
For each depth level backwards:
  1. Determine which diagonal we came from
  2. Add matches along the diagonal
  3. Add the operation (insert/delete)
Reverse the result
```

---

## 📊 **Visualizing Diagonals**

```
String a: A B C A B B A
String b: C B A B A C

Diagonal k = x - y

k = 0: (0,0), (1,1), (2,2), ...  → x = y
k = 1: (1,0), (2,1), (3,2), ...  → x = y + 1
k = -1: (0,1), (1,2), (2,3), ... → x = y - 1
```

**Movement:**
- **Match**: Move diagonally (x+1, y+1) → k stays same
- **Insert**: Move right (x, y+1) → k decreases by 1
- **Delete**: Move down (x+1, y) → k increases by 1

---

## 🔍 **Step-by-Step Walkthrough**

### **Example: "ABCABBA" → "CBABAC"**

```
a = "ABCABBA" (n=7)
b = "CBABAC"  (m=6)
```

#### **Depth d=0**
- Only diagonal: k=0
- Start: x=0, y=0
- a[0]='A' ≠ b[0]='C' → no match
- V[0] = 0

#### **Depth d=1**
- Diagonals: k=-1, k=1

**k=-1 (insert):**
- Start from k+1=0: x_start = V[0] = 0
- y_start = 0 - (-1) = 1
- a[0]='A' ≠ b[1]='B' → no match
- V[-1] = 0

**k=1 (delete):**
- Start from k-1=0: x_start = V[0] + 1 = 1
- y_start = 1 - 1 = 0
- a[1]='B' ≠ b[0]='C' → no match
- V[1] = 1

#### **Depth d=2**
- Diagonals: k=-2, k=0, k=2

**k=0 (match):**
- Compare V[-1]+1 vs V[1]+1 → 0+1 vs 1+1 → choose delete (k-1)
- x_start = 1, y_start = 1
- a[1]='B' == b[1]='B' → MATCH! x=2, y=2
- a[2]='C' == b[2]='A' → NO MATCH
- V[0] = 2

*(This continues through all depths...)*

---

## 🧠 **Why This Implementation is Educational**

### ✅ **Pros:**
1. **Clear data structure**: `V[k]` is intuitive
2. **No optimizations**: Shows the raw algorithm
3. **Complete trace**: Records every depth level
4. **Simple reconstruction**: Easy to follow backwards
5. **Well-commented**: Explains each decision

### ⚠️ **Considerations for Study:**

| Aspect | Educational Value | Performance |
|--------|------------------|-------------|
| `max_d = n + m` | Shows theoretical bound | O(n+m) iterations |
| Dict for V | Clear key-value access | O(1) but slower than array |
| Full trace | Perfect for debugging | O(n+m) memory |
| Simple reconstruction | Easy to understand | O(n+m) time |

---

## 📋 **Key Questions to Explore**

1. **Why does k step by 2?** (Each depth adds exactly one operation)
2. **Why check k=-d and k=d separately?** (Boundary conditions)
3. **What does "choose the move that advances furthest" mean?** (Greedy choice)
4. **Why reverse the edits at the end?** (We traced backwards)
5. **What's the time complexity?** (O(n+m) with optimizations)

---
A possible implementation

```python
def myers_diff_verbose(a: str, b: str):
    n, m = len(a), len(b)
    V = {0: 0}
    trace = []

    print("\n=== INIZIO ALGORITMO DI MYERS ===")
    print(f"Stringa A: {a}")
    print(f"Stringa B: {b}\n")

    max_d = n + m

    for d in range(max_d + 1):
        print(f"\n--------------------------------")
        print(f"   LIVELLO d = {d}")
        print("--------------------------------")

        new_V = {}

        for k in range(-d, d + 1, 2):
            print(f"\n  Diagonale k = {k}")

            # Scegli la mossa (insert o delete)
            if k == -d:
                x_start = V[k + 1]
                move = "insert (→)"
            elif k == d:
                x_start = V[k - 1] + 1
                move = "delete (↓)"
            else:
                if V[k - 1] + 1 > V[k + 1]:
                    x_start = V[k - 1] + 1
                    move = "delete (↓)"
                else:
                    x_start = V[k + 1]
                    move = "insert (→)"

            y_start = x_start - k

            print(f"    Scelta mossa: {move}")
            print(f"    Punto di partenza: (x={x_start}, y={y_start})")

            # Avanza lungo la diagonale
            x, y = x_start, y_start
            while x < n and y < m and a[x] == b[y]:
                print(f"    Match diagonale: A[{x}]={a[x]} == B[{y}]={b[y]}")
                x += 1
                y += 1

            print(f"    Fine avanzamento diagonale → (x={x}, y={y})")

            new_V[k] = x

            # Obiettivo raggiunto
            if x >= n and y >= m:
                print("\n>>> RAGGIUNTO OBIETTIVO (fine di entrambe le stringhe)")
                trace.append(new_V)
                return reconstruct_verbose(a, b, trace)

        trace.append(new_V)
        V = new_V


def reconstruct_verbose(a: str, b: str, trace):
    print("\n=== RICOSTRUZIONE DEL PERCORSO ===")
    edits = []
    x, y = len(a), len(b)

    for d in reversed(range(len(trace))):
        print(f"\n-- Risalgo livello d = {d} --")
        V = trace[d]
        k = x - y
        print(f"  Coordinate attuali: (x={x}, y={y}), diagonale k={k}")

        # Determina la mossa precedente
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

        print(f"  Provenivo da diagonale k={prev_k}")
        print(f"  Punto precedente: (x={prev_x}, y={prev_y})")
        print(f"  Operazione: {op}")

        # Match lungo la diagonale
        while x > prev_x and y > prev_y:
            print(f"    Match: {a[x-1]}")
            edits.append(("match", a[x - 1]))
            x -= 1
            y -= 1

        # Operazione effettiva
        if op == "insert":
            print(f"    Insert: {b[prev_y]}")
            edits.append(("insert", b[prev_y]))
            y -= 1
        else:
            print(f"    Delete: {a[prev_x - 1]}")
            edits.append(("delete", a[prev_x - 1]))
            x -= 1

    edits.reverse()

    print("\n=== DIFF FINALE ===")
    for op, ch in edits:
        print(f"{op.upper():7} {ch}")

    return edits
```

Example:`myers_diff_verbose("ABCD", "ABECD")`
