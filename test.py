import requests
import json

if __name__ == "__main__":
    # Create three volunteers
    forenames = ["Stanislas", "Antoine", "Gilles"]
    surnames = ["Bruhiere", "Deleuze", "Vaucher"]
    ids = [0, 1, 2]

    for fn, sn, id in zip(forenames, surnames, ids):
        requests.put(
            f"http://127.0.0.1:5000/volunteer/{id}",
            {
                "forename": fn,
                "surname": sn,
            }
        )

        res = requests.get(
            f"http://127.0.0.1:5000/volunteer/{id}"
        )
        print(res.json())

    # Create two maraudes
    requests.put(
        "http://127.0.0.1:5000/maraude/0",
        {
            "volunteer_0": 0,
            "volunteer_1": 1,
        }
    )

    requests.put(
        "http://127.0.0.1:5000/maraude/1",
        {
            "volunteer_0": 0,
            "volunteer_1": 1,
            "volunteer_2": 2,
        }
    )

    # Get maraude 1
    res = requests.get(
        "http://127.0.0.1:5000/maraude/1",
    )

    print(json.dumps(res.json(), indent=4))

# curl http://127.0.0.1:5000/maraude_path/pcps17_2020_11_23 -d "data_path=example_data" -X GET
