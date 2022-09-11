import json

from src.app.main import lambda_handler


def test_water():
    test_event = {"fluid_name": "Water"}

    test_event["fluid_temperature"] = 300
    test_event["fluid_pressure"] = 101325

    response = json.loads(lambda_handler(test_event, {}))

    assert response["status_code"] == 200
    assert response["body"]["results"]["fluid"] == test_event["fluid_name"]
    assert response["body"]["results"]["c_p"]["value"] == 4180.6357765560715
    assert response["body"]["results"]["c_p"]["unit"] == "J/kg/K"
    assert response["body"]["results"]["rho"]["value"] == 996.5569352652021
    assert response["body"]["results"]["rho"]["unit"] == "kg/m3"
