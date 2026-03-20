cat > tests/test_all.py << 'EOF'
import pytest
import fastlib
import subprocess
import json
import os

# ========== Тесты Rust ==========

def test_aes_encrypt():
    """Тест AES шифрования"""
    data = [0] * 16
    key = [1] * 16
    result = fastlib.aes_encrypt(data, key)
    assert len(result) == 16
    assert result != data

def test_aes_encrypt_invalid_key():
    """Тест на неверный размер ключа"""
    data = [0] * 16
    key = [1] * 15
    with pytest.raises(Exception):
        fastlib.aes_encrypt(data, key)

def test_resize_image_not_exists():
    """Тест на отсутствие файла изображения"""
    with pytest.raises(Exception):
        fastlib.resize_image("not_exists.jpg", "output.jpg", 100, 100)

# ========== Тесты Go subprocess ==========

def test_go_subprocess():
    """Тест вызова Go калькулятора через subprocess"""
    # Компилируем если нужно
    if not os.path.exists("./go_calculator/calculator.exe"):
        subprocess.run(["go", "build", "-o", "./go_calculator/calculator.exe", "./go_calculator/main.go"])
    
    proc = subprocess.Popen(
        ["./go_calculator/calculator.exe"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    input_data = json.dumps({"numbers": [1, 2, 3]})
    stdout, stderr = proc.communicate(input_data.encode())
    assert proc.returncode == 0
    output = json.loads(stdout)
    assert output["sum"] == 14
EOF