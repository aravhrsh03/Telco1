import random
from multiprocessing import Pool

categories = ["Positive", "Negative", "Complaint", "Escalation"]

chat_logs = []

for i in range(1, 100001):

    chance = random.random()

    if chance < 0.01:
        chat_logs.append({
            "id": i,
            "category": random.choice(categories)
        })

    elif chance < 0.02:
        chat_logs.append({
            "id": i,
            "text": "",
            "category": random.choice(categories)
        })

    elif chance < 0.03:
        chat_logs.append("CORRUPTED_LOG")

    # Valid record
    else:
        chat_logs.append({
            "id": i,
            "text": f"Conversation {i}",
            "category": random.choice(categories)
        })

def validate(record):
    try:
        if not isinstance(record, dict):
            raise ValueError("Corrupted Log")
        
        if "text" not in record:
            raise KeyError("Missing Conversation")
        
        if "id" not in record:
            raise KeyError("Missing id")
        
        if "category" not in record:
            raise KeyError("Missing category")

        id_ = record["id"]
        text = record["text"]
        category = record["category"]

        if not isinstance(text, str):
            raise TypeError("Text")
        
        if not isinstance(id_, int):
            raise TypeError("id")
        
        if not isinstance(category, str):
            raise TypeError("Category")

        if text == "":
            raise ValueError("Empty Text")
        
        return True, None

    except ValueError as e:
        return False, f"ValueError: {e}"
    except KeyError as e:
        return False, f"KeyError: {e}"
    except Exception as e:
        return False, f"Invalid d_type: {e}"

def analyze(records):
    result_dict = {
        "Positive": 0,
        "Negative": 0,
        "Complaint": 0,
        "Escalation": 0
    }

    for log in records:
        ok, err = validate(log)
        if ok:
            result_dict[log["category"]] += 1
    
    return result_dict
        
def worker(records):
    return analyze(records)

if __name__ == "__main__":
    chunks = []
    chunk_size = 100

    for i in range(0, len(chat_logs), chunk_size):
        chunks.append(chat_logs[i:i + chunk_size])
    
    output = []
    with Pool(50) as pool:
        output = pool.map(worker, chunks)

    result_dict = {
        "Positive": 0,
        "Negative": 0,
        "Complaint": 0,
        "Escalation": 0
    }

    for j in output:
        result_dict["Positive"] += j["Positive"]
        result_dict["Negative"] += j["Negative"]
        result_dict["Complaint"] += j["Complaint"]
        result_dict["Escalation"] += j["Escalation"]
    print(result_dict)
    