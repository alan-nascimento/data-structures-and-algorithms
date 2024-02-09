# Explanation for find_files Function

## Reasoning Behind Decisions:

### Data Structure:

I chose to use a list to store the paths of files with the specified suffix. A list provides a simple and efficient way to collect the paths as we traverse the directory structure recursively. Each file path found is appended to this list, ensuring easy retrieval and manipulation of the results.

### Recursion:

I opted for a recursive approach to traverse the directory structure. Recursion simplifies the logic by handling the exploration of subdirectories automatically. This approach helps in achieving a concise and readable implementation.

## Time Efficiency:

The time complexity of the find_files function primarily depends on the number of files and directories in the given directory structure. In the worst-case scenario, where all files in the directory tree end with the specified suffix, the function will have to traverse through all files and directories once, resulting in a time complexity of O(N), where N is the total number of files and directories.

## Space Efficiency:

In terms of space complexity, the function utilizes a list (files_with_suffix) to store the paths of files with the specified suffix. The space complexity depends on the number of files matching the suffix. If there are M files with the specified suffix, the space complexity would be O(M), as the list will contain M elements representing these file paths.
