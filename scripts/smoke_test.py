"""Exercise an actual running API, including the Docker container in CI."""
import json
import math
import sys
from urllib.error import HTTPError
from urllib.request import Request, urlopen

base = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8000"


def get(path):
    with urlopen(base + path, timeout=30) as response:
        return json.load(response)


assert get("/") == {"Hello": "World"}
apple = get("/embedding?word=apple")
orange = get("/embedding?word=orange")
for data in [apple, orange]:
    assert data["model"] == "en_core_web_lg"
    assert data["dimensions"] == len(data["embedding"]) == 300
    assert all(math.isfinite(x) for x in data["embedding"])
    assert any(x != 0 for x in data["embedding"])
assert apple["embedding"] != orange["embedding"]
for path, code in [("/embedding", 422), ("/embedding?word=two%20words", 422),
                   ("/embedding?word=zzzxqvzzzxqvzzzxqv", 404)]:
    try:
        get(path)
        raise AssertionError(f"Expected HTTP {code}: {path}")
    except HTTPError as exc:
        assert exc.code == code
body = json.dumps({"start_word": "generating", "length": 4}).encode()
with urlopen(Request(base + "/generate", data=body, headers={"Content-Type": "application/json"}), timeout=30) as response:
    assert json.load(response) == {"generated_text": "generating text based on"}
print(json.dumps({"status": "PASS", "dimensions": apple["dimensions"],
                  "apple_first_5": apple["embedding"][:5],
                  "checks": "real embeddings, distinct words, input errors, original generation"}, indent=2))
