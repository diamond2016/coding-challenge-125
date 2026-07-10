class MyersDiff:
    """
    Simple forward-only Myers Diff algorithm.
    Works on strings (character level or line level).
    """

    def __init__(self):
        # Trace stores a copy of the frontier (v) for every edit distance d
        # This allows us to reconstruct the actual edit path later
        self.trace: list[dict[int, int]] = []

    def myers_traverse(self, a: str, b: str) -> int:
        """
        Forward phase of Myers algorithm.
        Explores the edit graph layer by layer (by edit distance d).

        Returns the final d (number of edits) when solution is found.
        """
        n = len(a)
        m = len(b)
        max_d = n + m

        # v[k] = farthest x reached on diagonal k with current d
        # k = y - x  (diagonal identifier)
        v: dict[int, int] = {1: 0}

        for d in range(max_d + 1):
            # Save current state for backtracking
            self.trace.append(v.copy())

            # Explore all possible diagonals for this d
            # Step by 2 because parity is preserved (k and d must have same parity)
            for k in range(-d, d + 1, 2):

                # Decide whether we come from delete (right) or insert (down)
                if k == -d or (k != d and v.get(k - 1, -1) < v.get(k + 1, -1)):
                    # Came from insert (vertical move)
                    x = v.get(k + 1, 0)
                else:
                    # Came from delete (horizontal move)
                    x = v.get(k - 1, 0) + 1

                y = x - k

                # Extend the "snake" - follow diagonal as long as characters match
                # These moves are free (don't increase edit count)
                while x < n and y < m and a[x] == b[y]:
                    x += 1
                    y += 1

                v[k] = x

                # Solution found!
                if x >= n and y >= m:
                    return d  # This is the minimal number of edits

        return -1  # Should never happen

    def myers_diff(self, a: str, b: str) -> list[tuple[str, str]]:
        """
        Computes the diff between two strings.

        Returns a list of tuples:
            ('equal',  char)
            ('delete', char)
            ('insert', char)

        The list is in forward order (from start to end).
        """
        # Reset trace for new diff
        self.trace = []

        final_d = self.myers_traverse(a, b)
        if final_d == -1:
            raise ValueError("Failed to compute diff")

        # Backtracking phase - reconstruct the path
        diffs: list[tuple[str, str]] = []
        x = len(a)
        y = len(b)

        # Go backwards through the trace
        for d in range(final_d, -1, -1):
            v = self.trace[d]
            k = x - y

            # Determine where we came from
            if k == -d or (k != d and v.get(k - 1, -1) < v.get(k + 1, -1)):
                prev_k = k + 1
                prev_x = v.get(prev_k, 0)
                prev_y = prev_x - prev_k
                came_from = 'insert'
            else:
                prev_k = k - 1
                prev_x = v.get(prev_k, 0)
                prev_y = prev_x - prev_k
                came_from = 'delete'

            # First, consume all diagonal (equal) moves
            while x > prev_x and y > prev_y:
                x -= 1
                y -= 1
                diffs.append(('equal', a[x]))

            # Then the single edit move (if not at start)
            if d > 0:
                if came_from == 'insert':
                    y -= 1
                    diffs.append(('insert', b[y]))
                else:
                    x -= 1
                    diffs.append(('delete', a[x]))

            # Move to previous position
            x, y = prev_x, prev_y

        # We built the path backwards, so reverse it
        diffs.reverse()
        return diffs

    def myers_diff_prettyp(self, a: str, b: str) -> str | None:
        result: list[tuple[str, str]] = self.myers_diff(a, b)
        result_str: str = ""
        if result:
    # Colour-code additions in green, deletions in red, and leave unchanged lines cyan for matches
            for oper, c in result:
                if (oper == 'insert'):
                    result_str = result_str + self.colorize_string(1, c)
                elif (oper == 'delete'):
                    result_str = result_str + self.colorize_string(0, c)
                elif (oper == 'equal'):
                    result_str = result_str + self.colorize_string(6, c)
            return result_str
        
        return None
    
    def diff_text(self, text1: str, text2: str, by_lines: bool = True) -> list[tuple[str, str]]:
        """
        Convenient method to diff two strings.
        
        by_lines=True  -> line level diff (recommended for source code / text)
        by_lines=False -> character level diff
        """
        if by_lines:
            # keep \n so we can reconstruct
            a = text1.splitlines(keepends=True)
            b = text2.splitlines(keepends=True)
        else:
            a = list(text1)
            b = list(text2)

        return self.myers_diff(a, b)

    def diff_lines(self, text1: str, text2: str) -> list[tuple[str, str]]:
        """
        Line-level diff between two text blocks.
        Returns list of ('equal'|'delete'|'insert', line)
        """
        return self.diff_text(text1, text2, by_lines=True)
    

    def colorize_string(self, index: int, c: str) -> str:
        # Python program to color each character of a string individually
        # ANSI color codes for foreground text
        COLORS: list[str] = [
            "\033[31m",  # Red     0
            "\033[32m",  # Green   1
            "\033[33m",  # Yellow  2
            "\033[34m",  # Blue    3
            "\033[35m",  # Magenta 4 
            "\033[36m",  # Cyan    5
            "\033[37m",  # White   6
        ]

        RESET = "\033[0m"  # Reset to default color
        """
        Color each character of the string in a repeating pattern.
        """

        colored_chars: str = ""
        color: str = COLORS[index]
        colored_chars = colored_chars + (f"{color}{c}{RESET}")

        return colored_chars