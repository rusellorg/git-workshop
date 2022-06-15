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


def calculate_final_notes(notes: list[list[float]]) -> list[float]:
    """
    Calculates the final notes of a list of notes. The final note is calculated by:
    final_note = (note1 + note2) * 0.3 + note3 * 0.6
    """
    final_notes = []
    for note in notes:
        final_note = (note[0] + note[1]) * 0.3 + note[2] * 0.6
        final_notes.append(round(final_note, 1))

    return final_notes
