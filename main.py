from hashmap import HashMap


def main():
    map = HashMap(capacity=4, load_factor=0.75)

    # Add entries to trigger resize
    keys = ["apple", "banana", "carrot", "dog", "elephant", "frog", "grape"]
    colors = ["red", "yellow", "orange", "brown", "gray", "green", "purple"]

    for k, v in zip(keys, colors):
        map.set(k, v)
        print(f"Added ({k}: {v}), size: {map.size}, capacity: {map.capacity}")

    print("Final capacity after inserts:", map.capacity)
    print("Entries:", map.entries())

    # Check retrieval after resize
    print("Get 'elephant':", map.get("elephant"))
    print("Get 'frog':", map.get("frog"))


if __name__ == "__main__":
    main()
