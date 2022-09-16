import json

from CoolProp.CoolProp import PropsSI


def _get_basic_properties(fluid_name, fluid_temperature, fluid_pressure):
    c_p = PropsSI("C", "P", fluid_pressure, "T", fluid_temperature, fluid_name)
    rho = PropsSI("D", "T", fluid_temperature, "P", fluid_pressure, fluid_name)
    return {
        "fluid": fluid_name,
        "c_p": {"value": c_p, "unit": "J/kg/K"},
        "rho": {"value": rho, "unit": "kg/m3"},
    }

def lambda_handler(event, context):
    fluid_name = event["fluid_name"]
    fluid_temperature = event["fluid_temperature"]
    fluid_pressure = event["fluid_pressure"]
    calculated_properties = _get_basic_properties(
        fluid_name, fluid_temperature, fluid_pressure
    )
    return json.dumps({"status_code": 200, "body": {"results": calculated_properties}})
