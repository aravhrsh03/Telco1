from multiprocessing import Pool

messages = [
    # Spam Messages
    "Congratulations! Win ₹500000",
    "Limited offer! Buy now",
    "Claim your free gift today",
    "You have won an iPhone",
    "Exclusive deal! Click here",
    "Get 90% discount today",
    "Urgent! Claim your reward",
    "Earn money from home",
    "Win cash instantly",
    "Lottery winner! Contact us",
    "Lowest prices guaranteed",
    "Free vacation package",
    "Congratulations! You've been selected",
    "Special offer expires tonight",
    "Click here to receive your prize",
    "Get free recharge now",
    "You are our lucky winner",
    "Claim cashback immediately",
    "Limited time sale",
    "You've won ₹1000000",

    # Not Spam Messages
    "Your OTP is 234567",
    "Meeting starts at 10 AM",
    "Happy Birthday! Have a great day",
    "Your electricity bill is due tomorrow",
    "Package delivered successfully",
    "Dinner at 8 PM?",
    "Your order has been shipped",
    "Class is cancelled today",
    "Doctor appointment confirmed",
    "Please call me when free",
    "Your bank balance is updated",
    "Train departs at 6:30 PM",
    "Project deadline is Friday",
    "Welcome to our service",
    "Your subscription has been renewed",
    "Exam results are available",
    "Invoice generated successfully",
    "See you tomorrow",
    "Thanks for your payment",
    "Your cab has arrived",

    # Exception Cases
    "",                          # Empty message
    None,                        # None
    b"\xff\xfe\x00\x80",         # Invalid encoding (bytes)
    "",                          # Empty message
    None,                        # None
    b"\x80\x81\x82",             # Invalid encoding
    "",                          # Empty message
    None,                        # None
    b"\xff\xff",                 # Invalid encoding
    "",                          # Empty message
]

spam_keywords = [
    "win", "won", "offer", "free", "prize", "claim",
    "cash", "lottery", "reward", "discount",
    "buy now", "click here", "gift", "earn", "Congratulations"
]

def classify_message(message):
    try:
        if message is None:
            raise ValueError("Message is None")

        if isinstance(message, bytes):
            raise UnicodeDecodeError("utf-8", b"", 0, 1, "Invalid encoding")

        if message.strip() == "":
            raise ValueError("Empty message")

        ret = None
        message = message.lower()

        for keyword in spam_keywords:
            if keyword in message:
                ret = "Spam"

        ret = "Not Spam"
    
    except ValueError as e:
        ret = e
    except UnicodeDecodeError as e:
        ret = e
    except Exception as e:
        ret = e
    
    return ret

def worker(msgs):
    output = []
    for message in msgs:
        output.append(classify_message(message))
    return output

if __name__ == "__main__":
    chunks = []
    chunk_size = 4
    for i in range(0, len(messages), chunk_size):
        chunks.append(messages[i:i + chunk_size])
    
    output = None
    with Pool(4) as pool:
        output = pool.map(worker, chunks)
    
    iterator = 1
    for i in output:
        for j in i:
            print(f"Message {iterator} {j}")
            iterator += 1