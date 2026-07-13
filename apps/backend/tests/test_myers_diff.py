# /backend/test_myers_diff.py
from src.diff.myers_diff import MyersDiff

def test_myers_diff_basic():
    """
    Tests the myers_diff method of MyersDiff class, with simple strings.
    """
    string_a = "ABCD"
    string_b = "ABECD"

    # Expected output for "ABCD" -> "ABECD"
    # Match A, Match B, Insert E, Match C, Match D
    expected_edits: list[tuple[str, str]] = [
        ("equal", "A"),
        ("equal", "B"),
        ("insert", "E"),
        ("equal", "C"),
        ("equal", "D"),
    ]

    # Call the verbose function
    diff = MyersDiff()

    # Assert that the actual edits match the expected edits
    assert diff.myers_diff(string_a, string_b) == expected_edits


def test_myers_diff_prettyp_html_output():
    """
    Tests that myers_diff_prettyp returns HTML instead of ANSI codes.
    """
    diff = MyersDiff()
    
    result = diff.myers_diff_prettyp("ABCD", "ABECD")
    
    # Should return HTML string, not ANSI codes
    assert isinstance(result, str)
    assert '<span' in result
    assert 'style=' in result
    assert 'background-color:#d5f5e3' in result  # green for inserted 'E'
    assert '\033' not in result  # No ANSI escape codes


def test_myers_diff_prettyp_deletion_html():
    """
    Tests deletion produces red HTML spans.
    """
    diff = MyersDiff()
    
    result = diff.myers_diff_prettyp("ABECD", "ABCD")
    
    assert isinstance(result, str)
    assert '<span' in result
    assert 'background-color:#fadbd8' in result  # red for deleted 'E'
    assert '\033' not in result  # No ANSI escape codes


def test_myers_diff_prettyp_identical_html():
    """
    Tests identical strings produce neutral HTML spans.
    """
    diff = MyersDiff()
    
    result = diff.myers_diff_prettyp("ABC", "ABC")
    
    assert isinstance(result, str)
    assert '<span' in result
    assert 'background-color:#f2f6f4' in result  # neutral for equal
    assert '\033' not in result  # No ANSI escape codes


def test_myers_diff_prettyp_empty_strings():
    """
    Tests empty strings return None.
    """
    diff = MyersDiff()
    
    result = diff.myers_diff_prettyp("", "")
    
    assert result is None


def test_myers_diff_prettyp_complex_html():
    """
    Tests complex diff produces HTML with multiple colors.
    """
    diff = MyersDiff()
    
    result = diff.myers_diff_prettyp("THE QUICK BROWN FOX", "THE SLOW BROWN DOG")
    
    assert isinstance(result, str)
    assert '<span' in result
    assert 'style=' in result
    # Should have multiple color variations
    assert result.count('<span') > 1
    assert '\033' not in result  # No ANSI escape codes
