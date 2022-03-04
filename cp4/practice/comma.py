
def separateByComma(arr):
    if len(arr) == 0:
        return 'Empty'

    return ", ".join(arr[:-1]) + f" and {arr[-1]}"

if __name__ == "__main__":
    print("Type a list of items separated by spaces")
    arr = input().split(" ")

    print(separateByComma(arr))
