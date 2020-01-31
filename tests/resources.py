import json


with open("samples/charizard.json") as f:
    DUMMY_CHARIZARD_JSON = json.loads(str(f.read()))

DUMMY_SHAKESPEARE_DESC = (
    "Charizard flies 'round the sky in search of powerful opponents. 't "
    "breathes fire of such most wondrous heat yond 't melts aught. However, "
    "'t nev'r turns its fiery breath on any opponent weaker than itself."
)
DUMMY_SHAKESPEARE_JSON = {
    "success": {"total": 1},
    "contents": {"translated": DUMMY_SHAKESPEARE_DESC, "translation": "shakespeare"},
}
