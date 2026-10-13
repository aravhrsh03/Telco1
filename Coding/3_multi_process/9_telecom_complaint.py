from multiprocessing import Pool

complaints = [
    {
        "complaint_id": "Complaint 1",
        "priority": 5,
        "issue": "No Signal"
    },
    {
        "complaint_id": "Complaint 2",
        "priority": 2,
        "issue": "Recharge"
    },
    {
        "complaint_id": "Complaint 3",
        "priority": 10,
        "issue": "Fiber Cut"
    },
    {
        "complaint_id": "Complaint 4",
        "issue": "Network Slow"
    },
    {
        "complaint_id": "Complaint 5",
        "priority": -3,
        "issue": "Tower Down"
    },
    {
        "complaint_id": "Complaint 6",
        "priority": 7,
        "issue": ""
    },
    {
        "complaint_id": "Complaint 7",
        "priority": 1,
        "issue": "SIM Replacement"
    }
]

def analyze(record):
    try:
        complaint_id = record["complaint_id"]
        priority = record["priority"]
        issue = record["issue"]

        if priority is None:
            raise ValueError("Missing priority")

        if priority < 0:
            raise ValueError("Negative priority")

        if not issue:
            raise ValueError("Invalid issue")

        result = None
        if priority >= 8:
            result = "Critical"

        elif priority >= 4 and priority < 8:
            result = "Medium"
        
        else:
            result = "Low"
        
        return {
            "complaint_id": complaint_id
            "result": result
        }
    
    except ValueError as e:
        return {
            "complaint_id": record["complaint_id"]
            "error": str(e)
        }

    except KeyError as e:
        return {
            "complaint_id": data.get("complaint_id"),
            "error": f"Missing field {e}"
        }
    
    except Exception as e:
        return {
            "complaint_id": data.get("complaint_id"),
            "error": str(e)
        }

def worker(complaints):
    return analyze(complaint)

if __name__ == "__main__":

    output = None
    with Pool(4) as pool:
        output = pool.map(worker, complaints)

    print(output)
