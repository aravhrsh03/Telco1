from multiprocessing import Pool

def analyze(record):
    try:
        signal = record["signal"]
        latency = record["latency"]

        if isinstance(signal, (int, float)) == False:
            raise TypeError("Signal must be numeric")
        
        if isinstance(latency, (int, float)) == False:
            raise TypeError("Latency must be numeric")
        
        if signal < -100 or latency > 300:
            return "Drop"
        
        return "Stable"

    except KeyError as e:
        print("Key is not found : ", e)
    
    except Exception as e:
        print(e)

def worker(chunk):
    return analyze(chunk[0])

if __name__ == "__main__":
    call_records = [
        {"signal": -95, "latency": 250},
        {"signal": -70, "latency": 50},
        {"signal": -120, "latency": 500},
    ]

    chunks = []
    chunk_size = 1

    for i in range(0, len(call_records), chunk_size):
        chunks.append(call_records[i:i + chunk_size])
    
    with Pool(4) as pool:
        output = pool.map(worker, chunks)
    
    for i, value in enumerate(output):
        print(f"Record {i + 1} -> {value}")