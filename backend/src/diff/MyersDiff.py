class MyersDiff:
    """
    Myers Diff algorithm - simple forward-only version.
    Supports both character-level and line-level diffing.
    """
    
    def __init__(self):
        # Trace stores the frontier (v) at every edit distance d for backtracking
        self.trace: list[dict[int, int]] = []
    
    def myers_traverse(self, a: list[str], b: list[str]) -> int:
        """
        Core forward phase of the Myers algorithm.
        Works on lists of elements (characters or whole lines).
        """
        n = len(a)
        m = len(b)
        max_d = n + m
        
        # v[k] = farthest x reached on diagonal k with current d
        v: dict[int, int] = {1: 0}
        
        for d in range(max_d + 1):
            self.trace.append(v.copy())
            
            for k in range(-d, d + 1, 2):
                # Choose whether we came from a delete or an insert
                if k == -d or (k != d and v.get(k - 1, -1) < v.get(k + 1, -1)):
                    x = v.get(k + 1, 0)      # came from insert (down)
                else:
                    x = v.get(k - 1, 0) + 1  # came from delete (right)
                
                y = x - k
                
                # Extend snake (free diagonal moves when elements are equal)
                while x < n and y < m and a[x] == b[y]:
                    x += 1
                    y += 1
                
                v[k] = x
                
                if x >= n and y >= m:
                    return d  # Found optimal path
        
        return -1
    
    def myers_diff(self, a_list: list[str], b_list: list[str]) -> list[tuple[str, str]]:
        """
        Returns list of operations:
            ('equal',  element)
            ('delete', element)
            ('insert', element)
        """
        self.trace = []
        final_d = self.myers_traverse(a_list, b_list)
        
        if final_d == -1:
            raise ValueError("Failed to compute diff")
        
        # Backtracking to reconstruct the path
        diffs: list[tuple[str, str]] = []
        x = len(a_list)
        y = len(b_list)
        
        for d in range(final_d, -1, -1):
            v = self.trace[d]
            k = x - y
            
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
            
            # Consume equal elements (diagonal moves)
            while x > prev_x and y > prev_y:
                x -= 1
                y -= 1
                diffs.append(('equal', a_list[x]))
            
            # Single edit move
            if d > 0:
                if came_from == 'insert':
                    y -= 1
                    diffs.append(('insert', b_list[y]))
                else:
                    x -= 1
                    diffs.append(('delete', a_list[x]))
            
            x, y = prev_x, prev_y
        
        diffs.reverse()
        return diffs
    
    def diff_text(self, text1: str, text2: str, by_lines: bool = True) -> list[tuple[str, str]]:
        """
        Convenient method to diff two strings.
        
        by_lines=True  -> line level diff (recommended for source code / text)
        by_lines=False -> character level diff
        """
        if by_lines:
            a = text1.splitlines(keepends=True)  # keep \n so we can reconstruct
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