
def test_example():
    """Пример теста"""
    assert True

def test_addition():
    """Тест сложения"""
    assert 1 + 1 == 2

def test_imports():
    """Тест импортов"""
    try:
        import pytest
        import selenium
        assert True
    except ImportError:
        assert False, "Не все зависимости установлены"
