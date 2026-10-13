from multiprocessing import Pool


images = [
    {"image_id": "Image 1", "file_name": "tower_001.jpg", "format": "JPG", "status": "valid"},
    {"image_id": "Image 2", "file_name": "tower_002.jpg", "format": "JPG", "status": "valid"},
    {"image_id": "Image 3", "file_name": "tower_003.png", "format": "PNG", "status": "valid"},
    {"image_id": "Image 4", "file_name": "tower_004.jpg", "format": "JPG", "status": "valid"},
    {"image_id": "Image 5", "file_name": "tower_005.jpeg", "format": "JPEG", "status": "valid"},
    {"image_id": "Image 6", "file_name": "tower_006.png", "format": "PNG", "status": "valid"},
    {"image_id": "Image 7", "file_name": "tower_007.jpg", "format": "JPG", "status": "valid"},
    {"image_id": "Image 8", "file_name": "tower_008.webp", "format": "WEBP", "status": "valid"},
    {"image_id": "Image 9", "file_name": "tower_009.jpg", "format": "JPG", "status": "corrupted"},
    {"image_id": "Image 10", "file_name": "tower_010.jpg", "format": "JPG", "status": "missing"}
]


def predict(file_name):

    if "001" in file_name:
        return "Healthy Tower"

    elif "002" in file_name:
        return "Cable Fault"

    elif "003" in file_name:
        return "Damaged Tower"

    elif "004" in file_name:
        return "Healthy Tower"

    elif "005" in file_name:
        return "Cable Fault"

    elif "006" in file_name:
        return "Damaged Tower"

    elif "007" in file_name:
        return "Healthy Tower"

    elif "008" in file_name:
        return "Cable Fault"

    else:
        return "Unknown"


def analyze(record):

    try:
        image_id = record["image_id"]
        file_name = record["file_name"]
        image_format = record["format"]
        status = record["status"]


        if status == "missing":
            raise FileNotFoundError("File not found")

        if status == "corrupted":
            raise ValueError("Corrupted image")


        if image_format not in ["JPG", "PNG", "WEBP"]:
            raise ValueError("Unsupported format")


        if not isinstance(image_id, str):
            raise TypeError("Invalid image ID")


        result = predict(file_name)


        return {
            "image_id": image_id,
            "prediction": result
        }


    except FileNotFoundError as e:
        return {
            "image_id": record["image_id"],
            "error": str(e)
        }


    except ValueError as e:
        return {
            "image_id": record["image_id"],
            "error": str(e)
        }


    except Exception as e:
        return {
            "image_id": record["image_id"],
            "error": str(e)
        }



if __name__ == "__main__":

    with Pool(4) as pool:
        output = pool.map(analyze, images)


    for item in output:
        print(item)