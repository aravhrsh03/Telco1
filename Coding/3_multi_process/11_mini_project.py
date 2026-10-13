import random
from multiprocessing import Pool
import multiprocessing
import time
from enum import Enum

class Predict(Enum):
    SKIPPED = "Skipped"
    NORMAL = "Normal"
    HIGH_RISK = "High Risk"

class Status(Enum):
    OK = "ok"
    ERROR = "error"


def generate_data(count):
    random.seed(42)
    records = []

    for i in range(count):

        record = {
            "customer_id": i + 1,
            "usage": random.randint(1, 500),
            "complaints": random.randint(0, 10),
            "signal": random.randint(-120, -50)
        }

        records.append(record)


    records.extend([
        {
            "usage": 200,
            "complaints": 1,
            "signal": -70
        },
        {
            "customer_id": 500002,
            "complaints": 5,
            "signal": -90
        },
        {
            "customer_id": 500003,
            "usage": "high",
            "complaints": 2,
            "signal": -80
        },
        {
            "customer_id": 500004,
            "usage": 100,
            "complaints": None,
            "signal": -90
        },
        {
            "customer_id": 500005,
            "usage": 20,
            "complaints": 1,
            "signal": -150
        }
    ])

    return records



customer_records = generate_data(500000)

def analyze(record):
    try:
        customer_id = record["customer_id"]
        usage = record["usage"]
        complaints = record["complaints"]
        signal = record["signal"]

        if not customer_id:
            raise ValueError("Missing Customer_id")
        
        if not usage:
            raise ValueError("Missing Usage")
        
        if not complaints:
            raise ValueError("Missing Complaints")
        
        if not signal:
            raise ValueError("Missing Signal")
        
        if not isinstance(usage, int):
            raise TypeError("Invalid typeid : usage")
        
        if not isinstance(complaints, int):
            raise TypeError("Invalid typeid : complaints")
        
        if not isinstance(customer_id, int):
            raise TypeError("Invalid typeid : customer_id")
        
        status = None
        ret = None
        if usage < 50 or complaints > 3 or signal < -100:
            ret = Predict.HIGH_RISK.name
        else:
            ret = Predict.NORMAL.name
        status = Status.OK.name

    except KeyError as e:
        ret = Predict.SKIPPED.name
        status = Status.ERROR.name
    except TypeError as e:
        ret = Predict.SKIPPED.name
        status = Status.ERROR.name
    except ValueError as e:
        ret = Predict.SKIPPED.name
        status = Status.ERROR.name
    except Exception as e:
        ret = Predict.SKIPPED.name
        status = Status.ERROR.name
    
    return {
        "status" : status,
        "prediction" : ret
    }

def worker(records):
    output = []
    for rec in records:
        output.append(analyze(rec))
    return output

if __name__ == "__main__":
    workers = multiprocessing.cpu_count()
    chunks = []
    chunk_size = int(len(customer_records)/workers)

    for i in range(0, len(customer_records), chunk_size):
        chunks.append(customer_records[i:i + chunk_size])
    
    start = time.time()
    output = None
    with Pool(workers) as pool:
        output = pool.map(worker, chunks)
    end = time.time()
    
    Total_Records = len(customer_records)
    Processed = 0
    Skipped = 0
    High_risk = 0
    Normal = 0
    Time_taken = end - start

    for rec in output:
        for dic in rec:
            status = dic["status"]
            ret = dic["prediction"]

            if ret == Predict.SKIPPED.name:
                Skipped += 1
                continue
            elif ret == Predict.NORMAL.name:
                Normal += 1
            elif ret == Predict.HIGH_RISK.name:
                High_risk += 1
            
            Processed += 1
    
    print("========= SUMMARY ==========")
    print(f"""
    Total Records: {Total_Records}
    Processed: {Processed}
    Skipped: {Skipped}
    High Risk: {High_risk}
    Normal: {Normal}
        
    Time Taken: {Time_taken}
    """)
