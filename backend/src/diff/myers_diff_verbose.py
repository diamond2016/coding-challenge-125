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