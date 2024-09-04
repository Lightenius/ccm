

def capitalize_words(String: str) -> str:
    cap = String
    listo: list = []
    for item in cap.split(" "):
        listo.append(item.capitalize())
    string = listo[0]
    if len(listo) > 1:
        i = 1
        while i < len(listo):
            string = string + " " + listo[i]
            i += 1

    return string

