from api_client import get_weather

def test_invalid_city():
    result = get_weather("InvalidCity123")
    assert "error" in result

def test_empty_city():
    result = get_weather("")
    assert "error" in result
