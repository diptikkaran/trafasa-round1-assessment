import time

mock_db = {
    "V001": {"name": "Alpha Corp", "rating": 4.5},
    "V002": {"name": "Beta Ltd", "rating": 3.8},
    "V004": {"name": "Delta Inc", "rating": 4.9},
}

def fetch_vendor_data(vendor_ids):
    result = {}

    for vendor_id in vendor_ids:
        time.sleep(0.5)

        if vendor_id in mock_db:
            result[vendor_id] = mock_db[vendor_id]
        else:
            print(f"Vendor {vendor_id} not found.")

    return result


vendors = ["V001", "V002", "V003", "V004"]

data = fetch_vendor_data(vendors)

print(data)