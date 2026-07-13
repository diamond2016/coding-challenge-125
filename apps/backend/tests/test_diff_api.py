import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestDiffPrettypAPI:
    """Test suite for /api/diff-prettyp endpoint"""
    
    def test_diff_prettyp_simple_insertion(self):
        """Test diff with simple insertion (ABCD -> ABECD)"""
        response = client.post(
            "/api/diff-prettyp/",
            json={"string_a": "ABCD", "string_b": "ABECD"}
        )
        assert response.status_code == 200
        result = response.json()
        assert "diff" in result
        assert result["diff"] is not None
        # Should contain HTML span for inserted 'E' (green)
        assert '<span' in result["diff"]
        assert 'style=' in result["diff"]
        assert 'background-color:#d5f5e3' in result["diff"]  # green background
        print(f"✓ Simple insertion test passed")
        print(f"  Result: {result['diff'][:200]}...")
    
    def test_diff_prettyp_simple_deletion(self):
        """Test diff with simple deletion (ABECD -> ABCD)"""
        response = client.post(
            "/api/diff-prettyp/",
            json={"string_a": "ABECD", "string_b": "ABCD"}
        )
        assert response.status_code == 200
        result = response.json()
        assert "diff" in result
        assert result["diff"] is not None
        # Should contain HTML span for deleted 'E' (red)
        assert '<span' in result["diff"]
        assert 'style=' in result["diff"]
        assert 'background-color:#fadbd8' in result["diff"]  # red background
        print(f"✓ Simple deletion test passed")
        print(f"  Result: {result['diff'][:200]}...")
    
    def test_diff_prettyp_identical_strings(self):
        """Test diff with identical strings"""
        response = client.post(
            "/api/diff-prettyp/",
            json={"string_a": "ABC", "string_b": "ABC"}
        )
        assert response.status_code == 200
        result = response.json()
        assert "diff" in result
        assert result["diff"] is not None
        # Should contain HTML spans for equal characters (white/neutral)
        assert '<span' in result["diff"]
        assert 'style=' in result["diff"]
        assert 'background-color:#f2f6f4' in result["diff"]  # neutral background
        print(f"✓ Identical strings test passed")
        print(f"  Result: {result['diff'][:200]}...")
    
    def test_diff_prettyp_empty_strings(self):
        """Test diff with empty strings"""
        response = client.post(
            "/api/diff-prettyp/",
            json={"string_a": "", "string_b": ""}
        )
        assert response.status_code == 200
        result = response.json()
        assert "diff" in result
        assert result["diff"] is None
        print(f"✓ Empty strings test passed")
        print(f"  Result: {result['diff']}")
    
    def test_diff_prettyp_complex_diff(self):
        """Test diff with complex changes"""
        response = client.post(
            "/api/diff-prettyp/",
            json={"string_a": "THE QUICK BROWN FOX", "string_b": "THE SLOW BROWN DOG"}
        )
        assert response.status_code == 200
        result = response.json()
        assert "diff" in result
        assert result["diff"] is not None
        # Should contain HTML spans with different colors
        assert '<span' in result["diff"]
        assert 'style=' in result["diff"]
        # Check for multiple color variations (red, green, neutral)
        has_red = 'background-color:#fadbd8' in result["diff"]
        has_green = 'background-color:#d5f5e3' in result["diff"]
        has_neutral = 'background-color:#f2f6f4' in result["diff"]
        assert has_red or has_green or has_neutral
        print(f"✓ Complex diff test passed")
        print(f"  Result: {result['diff'][:300]}...")
    
    def test_diff_prettyp_missing_fields(self):
        """Test diff with missing fields"""
        response = client.post(
            "/api/diff-prettyp/",
            json={"string_a": "ABC"}
        )
        assert response.status_code == 422  # Validation error
        print(f"✓ Missing fields test passed (validation error)")
    
    def test_diff_prettyp_both_empty(self):
        """Test diff with both strings empty"""
        response = client.post(
            "/api/diff-prettyp/",
            json={"string_a": "", "string_b": ""}
        )
        assert response.status_code == 200
        result = response.json()
        assert result["diff"] is None
        print(f"✓ Both empty strings test passed")
        print(f"  Result: {result['diff']}")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
