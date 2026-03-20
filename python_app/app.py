import requests, os, time, fastlib

GO_URL = os.getenv("GO_URL","http://localhost:8080")

def call_go(numbers,retries=3):
    for _ in range(retries):
        try:
            r = requests.post(f"{GO_URL}/calculate", json={"numbers":numbers}, timeout=2)
            return r.json()["result"]
        except:
            time.sleep(1)
    raise Exception("Go unavailable")

def encrypt():
    return fastlib.aes_encrypt([1]*16,[2]*16)
