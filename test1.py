def direction(facing, turn):
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    try:
        return directions[
            (directions.index(facing) + (int(turn) % 360) // 45) % len(directions)
        ]
    except ValueError:
        raise ValueError("Incorrect input")
