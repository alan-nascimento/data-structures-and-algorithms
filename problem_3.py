import sys
import heapq
from collections import Counter
from typing import Tuple, Union


class Node:
    def __init__(self, char: Union[str, None], freq: int):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other: "Node") -> bool:
        return self.freq < other.freq


def build_huffman_tree(data: str) -> Node:
    frequency = Counter(data)
    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(priority_queue, merged)

    return priority_queue[0]


def generate_codes(root: Node, current_code: str = "", codes: dict = {}) -> None:
    if root is None:
        return

    if root.char is not None:
        codes[root.char] = current_code

    generate_codes(root.left, current_code + "0", codes)
    generate_codes(root.right, current_code + "1", codes)


def huffman_encoding(data: str) -> Tuple[str, Union[Node, None]]:
    if not data:
        return "", None

    root = build_huffman_tree(data)
    codes = {}
    generate_codes(root, "", codes)

    encoded_data = "".join([codes[char] for char in data])

    return encoded_data, root


def huffman_decoding(data: str, tree: Union[Node, None]) -> str:
    if not data or tree is None:
        return ""

    decoded_data = ""
    current_node = tree

    for bit in data:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_data += current_node.char
            current_node = tree

    return decoded_data


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print(
        "The size of the encoded data is: {}\n".format(
            sys.getsizeof(int(encoded_data, base=2))
        )
    )
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    # Test Case 1: Empty String
    input_string = ""
    encoded_data, tree = huffman_encoding(input_string)
    decoded_data = huffman_decoding(encoded_data, tree)
    assert decoded_data == "", "Test Case 1 Failed: Decoded data doesn't match input string"

    # Test Case 2: Very Large Input
    input_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    encoded_data, tree = huffman_encoding(input_string)
    decoded_data = huffman_decoding(encoded_data, tree)
    assert decoded_data == input_string, "Test Case 2 Failed: Decoded data doesn't match input string"

    # Test Case 3: Null Input
    input_string = None
    encoded_data, tree = huffman_encoding(input_string)
    decoded_data = huffman_decoding(encoded_data, tree)
    assert decoded_data == "", "Test Case 3 Failed: Decoded data doesn't match input string"

    print('All test cases passed successfully!')
