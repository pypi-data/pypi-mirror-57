from inbetween import inbetween


with open("inputs/sample.txt") as f:
    lines = f.readlines()
lines = inbetween(
    lines, ["^.*sep.*$"], "^.*lin.*$", "writeup", "    hop"
)
print("".join(lines))
