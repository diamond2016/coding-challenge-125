from src.diff import MyersDiff

diff_obj: MyersDiff = MyersDiff()

if __name__ == 'main':
    for op, char in differ.diff_text("kitten", "sitting", by_lines=False):
        print(f"{op:7} '{char}'")


    text1 = """Hello world
    This is Python
    Great language"""

    text2 = """Hello world
    This is awesome Python
    Great language"""

    for op, line in differ.diff_lines(text1, text2):
        if op == 'equal':
            print(f"  {line.rstrip()}")
        elif op == 'delete':
            print(f"- {line.rstrip()}")
        elif op == 'insert':
            print(f"+ {line.rstrip()}")