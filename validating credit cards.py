import sys,re,itertools
r = sys.stdin.read().split("\n")[1:]
for card in r:
    if not card or card[0] not in ("4","5","6"):
        print("Invalid")
        continue
    if len(re.findall(r"\d",card)) !=  16:
        print("Invalid")
        continue
    if re.findall(r"[^\d\-]",card):
        print("Invalid")
        continue
    if "-" in card:
        card = card.split("-")
        if any( len(p) != 4 for p in card ):
            print("Invalid")
            continue
        card = "".join(card)
    if any( len(list(b)) >= 4 for a,b in itertools.groupby(card)):
        print("Invalid")
        continue
    print("Valid")

