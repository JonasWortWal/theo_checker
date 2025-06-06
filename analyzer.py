TRIGGER = {
    "Gesetzlichkeit": [
        "wenn du treu bist", 
        "Gott wird segnen, wenn", 
        "du musst gehorchen, damit"
    ],
    "Bundesvermischung": [
        "wir müssen das Gesetz halten",
        "die zehn Gebote gelten für Christen"
    ]
}

def analyze_transcript(text):
    findings = []
    for kategorie, muster in TRIGGER.items():
        for satz in muster:
            if satz.lower() in text.lower():
                findings.append(f"Irrtum erkannt ({kategorie}): '{satz}'")
    return findings