import requests

r = requests.get("https://api.github.com/users/codewitharry")

if r.status_code == 200:
    with open("codewitharry.txt", "w", encoding="utf-8") as f:
        f.write(r.text)
    print("Saved successfully ✅")
else:
    print("Request failed:", r.status_code)
