import csv


def load_notes(filename: str) -> list[list[float]]:
    """
    Loads notes from a file.
    """
    notes = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            notes.append(row)

    return list(map(lambda x: list(map(float, x)), notes))
