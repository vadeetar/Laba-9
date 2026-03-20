cat > python_app/app.py << 'EOF'
import requests
import os
import time
import subprocess
import json
import fastlib

GO_URL = os.getenv("GO_URL", "http://localhost:8080")

def call_go_http(numbers, retries=3):
    """Вызов Go HTTP сервиса"""
    for _ in range(retries):
        try:
            r = requests.post(f"{GO_URL}/calculate", json={"numbers": numbers}, timeout=2)
            return r.json()["result"]
        except Exception:
            time.sleep(1)
    raise Exception("Go HTTP service unavailable")

def call_go_subprocess(numbers):
    """Вызов Go калькулятора через subprocess (исходный код, нужно скомпилировать)"""
    # Сначала компилируем (если бинарника нет)
    if not os.path.exists("./go_calculator/calculator.exe"):
        subprocess.run(["go", "build", "-o", "./go_calculator/calculator.exe", "./go_calculator/main.go"])
    
    proc = subprocess.Popen(
        ["./go_calculator/calculator.exe"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    input_data = json.dumps({"numbers": numbers})
    stdout, stderr = proc.communicate(input_data.encode())
    if proc.returncode != 0:
        raise RuntimeError(f"Go calculator failed: {stderr.decode()}")
    output = json.loads(stdout)
    return output["sum"]

def encrypt():
    """Вызов Rust AES шифрования"""
    return fastlib.aes_encrypt([1] * 16, [2] * 16)

def main():
    print("=== Go HTTP Service ===")
    result_http = call_go_http([1, 2, 3, 4, 5])
    print(f"HTTP result: {result_http}")

    print("\n=== Go Subprocess Calculator ===")
    try:
        result_sub = call_go_subprocess([1, 2, 3, 4, 5])
        print(f"Subprocess result: {result_sub}")
    except Exception as e:
        print(f"Subprocess error: {e}")
        print("(Make sure Go is installed to compile the binary)")

    print("\n=== Rust AES Encryption ===")
    encrypted = encrypt()
    print(f"Encrypted: {encrypted}")

if __name__ == "__main__":
    main()
EOF