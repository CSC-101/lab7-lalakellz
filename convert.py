from typing import Optional

#task 1
def str_to_float(value: str) -> Optional[float]:
    try:
        return float(value)
    except ValueError:
        return None

#task 2
