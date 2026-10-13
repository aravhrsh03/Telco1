from multiprocessing import Pool

customer_records = [
    {
        "customer_id": 1001,
        "usage": 35,
        "complaints": 5
    },
    {
        "customer_id": 1002,
        "usage": 120,
        "complaints": 1
    },
    {
        "customer_id": 1003,
        "usage": 45,
        "complaints": 4
    },
    {
        "customer_id": 1004,
        "usage": 200,
        "complaints": 0
    },
    {
        "customer_id": 1005,
        "usage": None,
        "complaints": 3
    },
    {
        "customer_id": 1006,
        "usage": 40,
        "complaints": "many"
    },
    {
        "customer_id": None,
        "usage": 30,
        "complaints": 5
    },
    {
        "customer_id": 1008,
        "usage": 60,
        "complaints": 6
    },
    {
        "customer_id": 1009,
        "usage": 20,
        "complaints": 10
    },
    {
        "customer_id": 1010,
        "usage": 75,
        "complaints": 2
    }
]


def analyze(record):
    try:
        customer_id = record["customer_id"]
        usage = record["usage"]
        complaints = record["complaints"]

        if customer_id is None:
            raise ValueError("Customer ID cannot be null")

        if usage is None:
            raise ValueError("Missing usage")

        if not isinstance(complaints, int):
            raise TypeError("Invalid complaint count")

        if usage < 50 and complaints > 3:
            result = "Churn"
        else:
            result = "No Churn"

        return f"Customer {customer_id} -> {result}"

    except KeyError as e:
        return f"Missing key: {e}"

    except Exception as e:
        return f"Customer {record.get('customer_id')} -> Error: {e}"


def worker(record):
    return analyze(record)


if __name__ == "__main__":

    with Pool(4) as pool:
        output = pool.map(worker, customer_records)

    for result in output:
        print(result)