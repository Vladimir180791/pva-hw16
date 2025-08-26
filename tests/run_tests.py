"""
Script для запуска тестов с автоматической установкой зависимостей
"""

import subprocess
import sys
import os

def install_dependencies():
    """Установить зависимости для тестов"""
    try:
        print("Установка зависимостей...")
        dependencies = [
            "pytest==7.4.0",
            "pytest-html==3.2.0",
            "selenium==4.15.0",
            "webdriver-manager==4.0.0"
        ]
        
        for package in dependencies:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при установке зависимостей: {e}")
        return False

def find_test_directory():
    """Найти папку с тестами"""
    possible_paths = [
        "tests",
        "test",
        "Tests",
        "Test",
        "../tests",
        "./tests"
    ]
    
    for path in possible_paths:
        if os.path.exists(path) and os.path.isdir(path):
            print(f"Найдена папка с тестами: {path}")
            return path
    
    print("Папка с тестами не найдена. Ищу тесты в текущей директории...")
    return "."

def run_tests():
    """Запустить тесты pytest"""
    test_dir = find_test_directory()
    
    try:
        print(f"Запуск тестов из: {test_dir}")
        result = subprocess.run([
            sys.executable, "-m", "pytest",
            "-v",
            "--html=report.html",
            "--self-contained-html",
            test_dir
        ], check=True, capture_output=True, text=True)
        
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
            
        return result.returncode == 0
        
    except subprocess.CalledProcessError as e:
        print(f"Тесты завершились с ошибкой (код {e.returncode}):")
        print("STDOUT:", e.stdout)
        print("STDERR:", e.stderr)
        return False

def check_dependencies():
    """Проверить установлены ли основные зависимости"""
    try:
        subprocess.check_call([sys.executable, "-c", "import pytest"])
        subprocess.check_call([sys.executable, "-c", "import pytest_html"])
        subprocess.check_call([sys.executable, "-c", "import selenium"])
        return True
    except subprocess.CalledProcessError:
        return False

def create_sample_test():
    """Создать пример теста если нет тестов"""
    test_dir = "tests"
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
    
    sample_test = os.path.join(test_dir, "test_sample.py")
    if not os.path.exists(sample_test):
        with open(sample_test, "w") as f:
            f.write('''
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
''')
        print(f"Создан пример теста: {sample_test}")
        return sample_test
    return None

if __name__ == "__main__":
    print("=" * 50)
    print("Запуск тестовой системы")
    print("=" * 50)
    
    if not check_dependencies():
        print("Зависимости не установлены. Устанавливаем...")
        if not install_dependencies():
            print("Не удалось установить зависимости")
            sys.exit(1)
    
    created_test = create_sample_test()
    if created_test:
        print("Создан пример теста для проверки")
    
    success = run_tests()
    
    if success:
        print("✅ Тесты успешно завершены")
        print("📊 Отчет сохранен в report.html")
    else:
        print("❌ Тесты завершились с ошибками")
    
    sys.exit(0 if success else 1)