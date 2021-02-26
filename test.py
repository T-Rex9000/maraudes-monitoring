import requests
import json

if __name__ == "__main__":
    res = requests.get(
        "http://127.0.0.1:5000/maraude_path/pcps17_2020_11_23",
        {
            "data_path": "example_data"
        }
    )

    print(json.dumps(res.json(), indent=4))

# curl http://127.0.0.1:5000/maraude_path/pcps17_2020_11_23 -d "data_path=example_data" -X GET
