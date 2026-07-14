# /backend/test_myers_diff_verbose.py
from app.utils.myers_diff import MyersDiff

def test_myers_diff_basic():
    """
    Tests the myers_diff methos of MyersDiff class, with simple strings.
    """
    string_a = """
    Arma virumque can Troiae
    oris qui primus
    """
    string_b= """ 
    Arma virumque cano 
    Troiae qui primus ab oris
    """

    # Expected output for "ABCD" -> "ABECD"

    # Call the verbose function
    diff = MyersDiff()
 
    # Assert that the actual edits match the expected edits
    assert diff.myers_traverse(string_a, string_b) > 5
    
    print(string_a)
    print(string_b)
    print(diff.diff_lines(string_a, string_b))
