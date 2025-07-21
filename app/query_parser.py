import re

def parse_query(query):
    age = re.findall(r'\d{2}', query)
    location = re.findall(r"in\s+(\w+)", query)
    policy = re.findall(r"(\d+)-month", query)
    treatment = "knee surgery" if "knee" in query.lower() else "unknown"
    return {
        'age': int(age[0]) if age else None,
        'location': location[0] if location else None,
        'policy_duration': int(policy[0]) if policy else None,
        'treatment': treatment
    }
