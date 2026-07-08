def myers_diff_verbose(a: str, b: str) -> list[tuple[str, str]] | None:
    n, m = len(a), len(b)
    v: dict[int, int] = {0: 0}
    trace: list[dict[int, int]] = []

    print("\n=== START MYERS ===")
    print(f"String A: {a}")
    print(f"String B: {b}\n")

    max_d = n + m

    for d in range(max_d + 1):
        print(f"\n--------------------------------")
        print(f"   LEVEL d = {d}")
        print("--------------------------------")

        new_V: dict[int, int] = {}
        chosen_k = None

        for k in range(-d, d + 1, 2):
            print(f"\n  Diagonal k = {k}")

            # Base case: start from (0, 0)
            if d == 0 and k == 0:
                x_start = 0
                move = "start"
            elif k == -d:
                x_start = v.get(k + 1, 0)
                move = "insert (→)"
            elif k == d:
                x_start = v.get(k - 1, 0) + 1
                move = "delete (↓)"
            else:
                if v.get(k - 1, 0) + 1 > v.get(k + 1, 0):
                    x_start = v.get(k - 1, 0) + 1
                    move = "delete (↓)"
                else:
                    x_start = v.get(k + 1, 0)
                    move = "insert (→)"

            y_start = x_start - k

            print(f"    Move: {move}")
            print(f"    Start: (x={x_start}, y={y_start})")

            # Along diag
            x, y = x_start, y_start
            while x < n and y < m and a[x] == b[y]:
                print(f"    Match diag: A[{x}]={a[x]} == B[{y}]={b[y]}")
                x += 1
                y += 1

            print(f"    End diag advance → (x={x}, y={y})")

            new_V[k] = x

            # Obiettivo raggiunto
            if x >= n and y >= m:
                print("\n>>> OK TARGET")
                chosen_k = k
                break

        # Store full V array for reconstruction
        full_trace = {k: new_V.get(k, 0) for k in range(-d, d + 1, 2)}
        trace.append(full_trace)
        v = new_V

        if chosen_k is not None:
            break

    if chosen_k is None:
        return None

    return reconstruct_verbose(a, b, trace, chosen_k)


def reconstruct_verbose(a: str, b: str, trace: list[dict[int, int]], final_k: int) -> list[tuple[str, str]]:
    print("\n=== RECONSTRUCT ===")
    edits: list[tuple[str, str]] = []
    x, y = len(a), len(b)

    for d in reversed(range(len(trace))):
        print(f"\n-- up d = {d} --")
        V = trace[d]
        k = x - y
        print(f"  coords: (x={x}, y={y}), diag k={k}")

        # Find which k at previous level led to this k
        prev_d = d - 1
        if prev_d < 0:
            prev_k = 0
        else:
            prev_k = None
            for pk in range(-prev_d, prev_d + 1, 2):
                # Check if this prev_k could lead to current k
                if k == -d and pk == -prev_d:
                    prev_k = pk
                    break
                elif k == d and pk == prev_d:
                    prev_k = pk
                    break
                elif abs(k - pk) == 1:
                    prev_k = pk
                    break
            if prev_k is None:
                prev_k = k

        prev_x = V.get(prev_k, 0)
        op = "insert" if k == -d else "delete" if k == d else "insert"

        prev_y = prev_x - prev_k

        print(f"  from diag k={prev_k}")
        print(f"  prev point: (x={prev_x}, y={prev_y})")
        print(f"  Operations: {op}")

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