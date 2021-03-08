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
        "http://127.0.0.1:5000/maraude/0"
    )

    requests.put(
        "http://127.0.0.1:5000/maraude/1"
    )

    # Create two participations for maraude 1
    requests.put(
        "http://127.0.0.1:5000/participation/0",
        {
            "volunteer_id": 0,
            "maraude_id": 1
        }
    )

    requests.put(
        "http://127.0.0.1:5000/participation/1",
        {
            "volunteer_id": 1,
            "maraude_id": 1
        }
    )

    # Get maraude 1
    res = requests.get(
        "http://127.0.0.1:5000/maraude/1",
    )

    # Create two homeless people
    requests.put(
        "http://127.0.0.1:5000/homeless/0",
        {
            "forename": "Jeff"
        }
    )

    requests.put(
        "http://127.0.0.1:5000/homeless/1",
        {
            "forename": "Bobby"
        }
    )

    # Create one encounter for maraude 1
    requests.put(
        "http://127.0.0.1:5000/encounter/0",
        {
            "maraude_id": 1,
            "homeless_id": 0,
            "latitude": 18.,
            "longitude": 19.,
            "comment": "Bon contact, cherche des chaussettes",
        }
    )

    print(json.dumps(res.json(), indent=4))

# curl http://127.0.0.1:5000/maraude_path/pcps17_2020_11_23 -d "data_path=example_data" -X GET
