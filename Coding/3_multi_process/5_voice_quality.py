from multiprocessing import Pool

voice_samples = [
    {"id": 1, "file": "sample1.wav", "mos": 4.7},
    {"id": 2, "file": "sample2.wav", "mos": 3.9},
    {"id": 3, "file": "sample3.wav", "mos": 2.5},
    {"id": 4, "file": "sample4.wav", "mos": 4.2},
    {"id": 5, "file": "sample5.wav", "mos": 3.1},
    {"id": 6, "file": "sample6.wav", "mos": 2.8},
    {"id": 7, "file": "sample7.wav", "mos": 4.9},
    {"id": 8, "file": "sample8.wav", "mos": 3.5},
    {"id": 9, "file": "sample9.wav", "mos": 1.9},
    {"id": 10, "file": "sample10.wav", "mos": 4.0},

    # Exception cases
    {"id": 11, "file": "corrupted.wav", "error": "Invalid audio", "mos": 0},
    {"id": 12, "file": "empty.wav", "error": "Empty file", "mos": 0},
    {"id": 13, "file": "sample13.mp3", "error": "Unsupported format", "mos": 0},
]

def analyze(record):
    try:
        record_id = record["id"]
        file = record["file"]
        mos = record["mos"]

        if not isinstance(record_id, int):
            raise TypeError("record_id")
        if not isinstance(file, str):
            raise TypeError("Path File")
        if not isinstance(mos, (int, float)):
            raise TypeError("mos must be numeric")
        
        if "error" in record:
            raise ValueError(record["error"])
        
        ret = None
        if mos > 4:
            ret = "Excellent"
        elif mos < 4 and mos >= 3:
            ret = "Good"
        else:
            ret = "Poor"

    except KeyError as e:
        ret = f"KeyError: {e}"
    except TypeError as e:
        ret = f"TypeError: d_type {e}"
    except ValueError as e:
        ret = f"ValueError: d_type {e}"
    except Exception as e:
        ret = e
    
    return {record_id: ret}

def worker(record):
    output = []
    for rec in record:
        output.append(analyze(rec))
    return output

if __name__ == "__main__":
    chunks = []
    chunk_size = 3
    for i in range(0, len(voice_samples), chunk_size):
        chunks.append(voice_samples[i:i + chunk_size])
    
    output = None
    with Pool(5) as pool:
        output = pool.map(worker, chunks)
    
    for recs in output:
        for r in recs:
            for key, value in r.items():
                print(f"Sample {key} -> {value}")