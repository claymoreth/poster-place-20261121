import os

_HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    src = os.path.join(_HERE, "image.png")
    with open(src, "rb") as f:
        data = f.read()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.png", "wb") as f:
        f.write(data)
    print("wrote /output/entry.png %d bytes" % len(data))


if __name__ == "__main__":
    main()
