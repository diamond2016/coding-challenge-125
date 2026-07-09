from src.diff.myers_diff import MyersDiff

diff_obj: MyersDiff = MyersDiff()

if __name__ == '__main__':
    string_a = "ABCD"
    string_b = "ABECD"
    print(f"diff (# of edits) from {string_a} and {string_b}: {diff_obj.myers_traverse(string_a, string_b)}" )

