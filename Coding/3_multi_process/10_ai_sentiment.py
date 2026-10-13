from multiprocessing import Pool


transcripts = [
    {
        "id": "Transcript 1",
        "text": "Thank you so much, your service was excellent and very helpful"
    },
    {
        "id": "Transcript 2",
        "text": "I have received the information. I will check and update later"
    },
    {
        "id": "Transcript 3",
        "text": "Your service is terrible. I am angry and disappointed"
    },
    {
        "id": "Transcript 4"
    },
    {
        "id": "Transcript 5",
        "text": ""
    },
    {
        "id": "Transcript 6",
        "text": b"\xff\xfe"
    },
    {
        "id": "Transcript 7",
        "text": "The agent solved my problem quickly and I am happy"
    },
    {
        "id": "Transcript 8",
        "text": "I do not like this experience and want a complaint raised"
    }
]


def sentiment_analysis(data):

    try:
        transcript_id = data["id"]
        text = data["text"]

        if isinstance(text, bytes):
            text = text.decode("utf-8")

        if not text.strip():
            raise ValueError("Empty text")


        text = text.lower()


        if "excellent" in text or "happy" in text or "thank" in text or "solved" in text:
            result = "Happy"

        elif "angry" in text or "terrible" in text or "complaint" in text or "disappointed" in text:
            result = "Angry"

        else:
            result = "Neutral"


        return {
            "transcript_id": transcript_id,
            "sentiment": result
        }


    except KeyError:
        return {
            "transcript_id": data.get("id"),
            "error": "Missing transcript"
        }


    except UnicodeDecodeError:
        return {
            "transcript_id": data.get("id"),
            "error": "Unicode decode error"
        }


    except ValueError as e:
        return {
            "transcript_id": data.get("id"),
            "error": str(e)
        }


    except Exception as e:
        return {
            "transcript_id": data.get("id"),
            "error": str(e)
        }

def worker(record):
    return sentiment_analysis(record)

if __name__ == "__main__":

    with Pool(4) as pool:
        results = pool.map(worker, transcripts)


    for result in results:
        print(result)