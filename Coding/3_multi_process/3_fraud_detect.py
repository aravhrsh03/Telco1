from multiprocessing import Pool

transactions = [
    {"transaction_id": 101, "user_id": "U001", "amount": 300,  "time": "10:00"},
    {"transaction_id": 102, "user_id": "U002", "amount": 7000, "time": "11:00"},
    {"transaction_id": 103, "user_id": "U003", "amount": 450,  "time": "12:30"},
    {"transaction_id": 104, "user_id": "U002", "amount": 6500, "time": "11:03"},
    {"transaction_id": 105, "user_id": "U004", "amount": 5200, "time": "14:10"},
    {"transaction_id": 106, "user_id": "U004", "amount": 5400, "time": "14:14"},
    {"transaction_id": 107, "user_id": "U005", "amount": 200,  "time": "15:20"},
    {"transaction_id": 108, "user_id": "U006", "amount": 8000, "time": "16:00"},
    {"transaction_id": 109, "user_id": "U006", "amount": 100,  "time": "16:20"},
    {"transaction_id": 110, "user_id": "U007", "amount": 5500, "time": "17:00"},
    {"transaction_id": 111, "user_id": "U008", "amount": 6000, "time": "18:00"},
    {"transaction_id": 112, "user_id": "U008", "amount": 6500, "time": "18:04"},
]

def get_user_ids():
    users = set()
    for rec in transactions:
        if rec["user_id"] not in users:
            users.add(rec["user_id"])
    
    return users

def get_chunk_by_id(id):
    chunk = []
    for rec in transactions:
        if rec["user_id"] == id:
            chunk.append(rec)
    return chunk

def parseTime(time):
    hours = int(time[0] + time[1])
    minutes = int(time[3] + time[4])

    minutes += hours * 60
    return minutes

def validate(record):
    try:
        transaction_id = record["transaction_id"]
        user_id = record["user_id"]
        amount = record["amount"]
        time = record["time"]

        if user_id is None or not user_id.startswith("U"):
            raise ValueError("Invalid User Id")
        
        if not isinstance(user_id, str):
            raise TypeError("user_id")
        
        if not isinstance(time, str):
            raise TypeError("time")
        
        if not isinstance(amount, int):
            raise TypeError("amount")
        
        return True, None

    except TypeError as t:
        return False, f"Type Err: {t}"
    
    except ValueError as v:
        return False, f"Value Err: {v}"

def analyze(records):
    transact_logs = []

    update_time = 0

    if len(records) == 1:
        ok, err = validate(records[0])
        transaction_id = records[0]["transaction_id"]
        if ok and records[0]["amount"] > 5000:
            transact_logs.append({transaction_id: "Fraud"})
        elif not ok:
            transact_logs.append({transaction_id: err})
        else:
            transact_logs.append({transaction_id: "Normal"})
    
    if len(records) >= 2:
        ok, err = validate(records[0])
        transaction_id_0 = records[0]["transaction_id"]
        if not ok:
            transact_logs.append({transaction_id_0: err})
        
        ok, err = validate(records[1])
        transaction_id_1 = records[1]["transaction_id"]
        if not ok:
            transact_logs.append({transaction_id_1: err})

        update_time = parseTime(records[1]["time"]) - parseTime(records[0]["time"])

        if records[0]["amount"] > 5000:
            transact_logs.append({transaction_id_0: "Fraud"})
        else:
            transact_logs.append({transaction_id_0: "Normal"})

        if records[1]["amount"] > 5000 or update_time <= 5:
            transact_logs.append({transaction_id_1: "Fraud"})
        else:
            transact_logs.append({transaction_id_1: "Normal"})
        
    for rec in range(3, len(records)):
        transaction_id = records[rec]["transaction_id"]

        ok, err = validate(records[rec])
        if not ok:
            transact_logs.append({transaction_id: err})

        amount = records[rec]["amount"]
        time = parseTime(records[rec]["time"])
        
        update_time = parseTime(records[rec]["time"]) - parseTime(records[rec - 1]["time"])

        if records[rec]["amount"] > 5000 or update_time <= 5:
            transact_logs.append({transaction_id: "Fraud"})
        else:
            transact_logs.append({transaction_id: "Normal"})
    
    return transact_logs

def worker(records):
    return analyze(records)

if __name__ == "__main__":
    users = get_user_ids()

    items = []
    for user in users:
        chunk = get_chunk_by_id(user)
        items.append(chunk)
    
    output = None
    with Pool(5) as pool:
        output = pool.map(worker, items)
    
    for recs in output:
        for lis in recs:
            for id, res in lis.items():
                print(f"Transaction {id} -> {res}")