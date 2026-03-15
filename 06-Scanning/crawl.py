#!/usr/bin/env python3
import sys, requests

if len(sys.argv) < 2:
    print("usage: crawl <base-url>")
    sys.exit(1)

BASE = sys.argv[1].rstrip("/")
TIMEOUT = 3

def fetch(path):
    url = BASE + "/" + path if path else BASE + "/"
    try:
        r = requests.get(url, timeout=TIMEOUT)
        return r.status_code, r.text
    except:
        return None, None

print(BASE.split("://",1)[-1])

stack = [{
    "path": "",
    "prefix": "",
    "children": None,
    "index": 0
}]

visited = set()

while stack:
    node = stack[-1]

    if node["children"] is None:
        key = node["path"].rstrip("/")
        if key in visited:
            stack.pop()
            continue
        visited.add(key)

        code, body = fetch(node["path"])
        if code is None or code == 404:
            stack.pop()
            continue

        lines = [l.strip() for l in body.splitlines() if l.strip()]
        node["children"] = lines
        node["index"] = 0
        continue

    if node["index"] >= len(node["children"]):
        stack.pop()
        continue

    entry = node["children"][node["index"]].rstrip("/")
    node["index"] += 1

    is_last = node["index"] == len(node["children"])
    branch = "└── " if is_last else "├── "

    prefix = node["prefix"]
    child_prefix = prefix + ("    " if is_last else "│   ")

    child_path = (node["path"] + "/" + entry).strip("/")

    code,_ = fetch(child_path)

    if code and code != 404:
        print(prefix + branch + entry)
        stack.append({
            "path": child_path,
            "prefix": child_prefix,
            "children": None,
            "index": 0
        })
        continue

    code,_ = fetch(child_path + "/")
    if code and code != 404:
        print(prefix + branch + entry)
        stack.append({
            "path": child_path + "/",
            "prefix": child_prefix,
            "children": None,
            "index": 0
        })
        continue

    print(prefix + branch + "-> " + entry)