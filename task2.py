import time

def generate_variants(text, allow_repeats=True):
    """Generate all possible permutations of a string using a recursive approach."""
    if not text:
        return []

    characters = list(text)
    unique_variants = set()

    def permute_recursive(index):
        if index == len(characters) - 1:
            variant = ''.join(characters)
            if allow_repeats or variant not in unique_variants:
                unique_variants.add(variant)
        else:
            for j in range(index, len(characters)):
                # Swap characters to form a new arrangement
                characters[index], characters[j] = characters[j], characters[index]
                permute_recursive(index + 1)
                # Revert the change to backtrack
                characters[index], characters[j] = characters[j], characters[index]

    permute_recursive(0)
    return list(unique_variants) if not allow_repeats else list(unique_variants)


def get_permutations_iteratively(word, allow_repeats=True):
    """Generate all permutations of a string in an iterative manner."""
    if not word:
        return []

    word = ''.join(sorted(word))
    length = len(word)
    permuted_set = set()

    while True:
        if allow_repeats or word not in permuted_set:
            permuted_set.add(word)
            print(word)  # Display each permutation as it is generated

        # Step 1: Find the highest index i where word[i-1] < word[i]
        i = length - 1
        while i > 0 and word[i - 1] >= word[i]:
            i -= 1

        # End loop if no such index is found
        if i == 0:
            break

        # Step 2: Find the largest j such that word[j] > word[i-1]
        j = length - 1
        while word[j] <= word[i - 1]:
            j -= 1

        # Step 3: Swap characters at the pivot point
        word_list = list(word)
        word_list[i - 1], word_list[j] = word_list[j], word_list[i - 1]
        word = ''.join(word_list)

        # Step 4: Reverse the sequence from i to the end
        word = word[:i] + word[i:][::-1]

    return list(permuted_set) if not allow_repeats else list(permuted_set)


if __name__ == "__main__":
    try:
        input_string = input("Provide a string to generate permutations: ")
        if not input_string.strip():
            raise ValueError("Input cannot be blank.")

        repeats_allowed = input("Allow duplicate results? (yes/no): ").strip().lower()
        if repeats_allowed not in ["yes", "no"]:
            raise ValueError("Answer must be 'yes' or 'no'.")

        repeats_allowed = repeats_allowed == "yes"

        # Measure the execution time of the recursive method
        start = time.time()
        recursive_variants = generate_variants(input_string, repeats_allowed)
        recursive_duration = time.time() - start

        print(f"Recursive permutations ({len(recursive_variants)}): {recursive_variants}")
        print(f"Time taken for recursion: {recursive_duration:.6f} seconds")

        # Uncomment below to test the iterative method
        # start = time.time()
        # iterative_variants = get_permutations_iteratively(input_string, repeats_allowed)
        # iterative_duration = time.time() - start

        # print(f"Iterative permutations ({len(iterative_variants)}): {iterative_variants}")
        # print(f"Time taken iteratively: {iterative_duration:.6f} seconds")

    except Exception as error:
        print(f"Encountered an error: {error}")
