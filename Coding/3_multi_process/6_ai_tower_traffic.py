from multiprocessing import Pool

# Mock traffic data for telecom towers
traffic_data = {
    "Chennai": [
        {"tower": "Tower A", "users": 6500},   # High
        {"tower": "Tower B", "users": 3500},   # Medium
        {"tower": "Tower C", "users": 1200},   # Low
        {"tower": "Tower D", "users": 7200},   # High
        {"tower": "Tower E", "users": 4800},   # Medium
        {"tower": "Tower F", "users": 900},    # Low
        {"tower": "Tower G", "users": 5600},   # High
        {"tower": "Tower H", "users": 2200},   # Medium
        {"tower": "Tower I", "users": None},   # Missing data
        {"tower": "Tower J", "users": -150},   # Negative users
    ],

    "Bangalore": [
        {"tower": "Tower K", "users": 8100},   # High
        {"tower": "Tower L", "users": 2600},   # Medium
        {"tower": "Tower M", "users": 1700},   # Low
        {"tower": "Tower N", "users": 9200},   # High
        {"tower": "Tower O", "users": 4300},   # Medium
        {"tower": "Tower P", "users": 1950},   # Low
        {"tower": "Tower Q", "users": 6100},   # High
        {"tower": "Tower R", "users": 3100},   # Medium
        {"tower": "Tower S", "users": None},   # Missing data
        {"tower": "Tower T", "users": -400},   # Negative users
    ],

    "Hyderabad": [
        {"tower": "Tower U", "users": 7000},   # High
        {"tower": "Tower V", "users": 3900},   # Medium
        {"tower": "Tower W", "users": 1600},   # Low
        {"tower": "Tower X", "users": 5400},   # High
        {"tower": "Tower Y", "users": 2800},   # Medium
        {"tower": "Tower Z", "users": 1000},   # Low
        {"tower": "Tower AA", "users": 8500},  # High
        {"tower": "Tower AB", "users": 4700},  # Medium
        {"tower": "Tower AC", "users": None},  # Missing data
        {"tower": "Tower AD", "users": -50},   # Negative users
    ]
}

def analyze(record):
    try:
        tower = record["tower"]
        users = record["users"]

        if not isinstance(tower, str):
            raise TypeError("tower")
        if isinstance(users, type(None)):
            raise ValueError("Missing data")
        if users < 0:
            raise ValueError("Negative users")
        if not isinstance(users, int):
            raise TypeError("users")
        
        ret = None
        if users > 5000:
            ret = "High"
        elif users < 5000 and users >= 2000:
            ret = "Medium"
        else:
            ret = "Low"

    except TypeError as e:
        ret = e
    except ValueError as e:
        ret = e
    except Exception as e:
        ret = e
    
    return f"{tower} {ret}"

def worker(record):
    key, value = record, traffic_data[record]

    print(f"Processing {key}")
    for rec in value:
        res = analyze(rec)
        print(res)
    
    print()

if __name__ == "__main__":
    output = None
    with Pool(3) as pool:
        pool.map(worker, traffic_data)