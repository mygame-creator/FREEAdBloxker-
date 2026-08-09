import json

# 1. Read the text blocklist line by line
with open("blocklist.txt", "r") as f:
    # Ignore empty lines or lines starting with comments (#)
    domains = [line.strip() for line in f if line.strip() and not line.startswith("#")]

rules = []

# 2. Loop through each domain and build a declarativeNetRequest rule
for index, domain in enumerate(domains, start=1):
    rule = {
        "id": index,
        "priority": 1,
        "action": {
            "type": "block"
        },
        "condition": {
            "urlFilter": f"||{domain}",
            "resourceTypes": [
                "script",
                "image",
                "sub_frame",
                "stylesheet",
                "xmlhttprequest"
            ]
        }
    }
    rules.append(rule)

# 3. Save the result as rules.json
with open("rules.json", "w") as f:
    json.dump(rules, f, indent=2)

print(f"Successfully generated rules.json with {len(rules)} rules!")