import json

class HuckelInputError(Exception):
    pass

def load_input(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        raise HuckelInputError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise HuckelInputError(f"File is not valid JSON: {file_path}")
    
    validate_input(data)
    return data

def validate_input(data):
    required_keys = ["atoms", "bonds", "electrons", "alpha", "beta"]
    for key in required_keys:
        if key not in data:
            raise HuckelInputError(f"Missing required key: {key}")
    
    if not isinstance(data["atoms"], list) or len(data["atoms"]) == 0:
        raise HuckelInputError("Atoms must be a non-empty list")
    
    if not isinstance(data["bonds"], list):
        raise HuckelInputError("Bonds must be a list of index pairs")
    for bond in data["bonds"]:
        if not (isinstance(bond, list) or isinstance(bond, tuple)) or len(bond) != 2:
            raise HuckelInputError(f"Each bond must be a pair of indices: {bond}")
        if not all(isinstance(idx, int) for idx in bond):
            raise HuckelInputError(f"Bond indices must be integers: {bond}")
        if any(idx < 0 or idx >= len(data["atoms"]) for idx in bond):
            raise HuckelInputError(f"Bond index out of range: {bond}")
    
    if not isinstance(data["electrons"], int) or data["electrons"] < 0:
        raise HuckelInputError("Electrons must be a non-negative integer")
    
    for param in ["alpha", "beta"]:
        if not isinstance(data[param], (int, float)):
            raise HuckelInputError(f"Parameter {param} must be a number")