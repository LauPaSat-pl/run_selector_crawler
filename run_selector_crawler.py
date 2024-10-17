import requests


def load_data() -> set:
    """
    This function loads the data from the sample_list.txt file and returns a set of the lines.
    """
    with open('sample_list.txt', 'r') as file:
        lines = set((x.strip() for x in file.readlines()))
    return lines


def main():
    """
    This is the main function that will be executed when the script is run.
    """
    lines: set = load_data()
    for line in lines:
        response = requests.get(f"https://www.ncbi.xyz/Traces/study/?acc={line.strip()}")
        if "Hi-C" in response.text:
            print(f"Found Hi-C in {line}")
        else:
            print(f"Did not find Hi-C in {line}")


if __name__ == '__main__':
    main()
