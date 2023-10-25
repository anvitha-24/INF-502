import sys


def calculate_number_of_matches(sequence1, sequence2):
    if len(sequence1) != len(sequence2):
        raise ValueError("Sequences must have the same length for matching.")

    match_count = 0
    for char1, char2 in zip(sequence1, sequence2):
        if char1 == char2:
            match_count += 1
    return match_count


def shift_and_calculate_score(sequence, shift, target_sequence):
    if shift < 0:
        raise ValueError("Shift value must be non-negative.")

    shifted_sequence = sequence[-shift:] + sequence[:-shift]
    return calculate_number_of_matches(shifted_sequence, target_sequence)


def find_maximum_contiguous_chain(sequence1, sequence2):
    max_chain = 0
    current_chain = 0
    for nucleotide1, nucleotide2 in zip(sequence1, sequence2):
        if nucleotide1 == nucleotide2:
            current_chain += 1
            if current_chain > max_chain:
                max_chain = current_chain
        else:
            current_chain = 0
    return max_chain


def main():
    max_shift = None
    sequence1 = None
    sequence2 = None

    try:
        while True:
            print("DNA Similarity Program")
            print("1. Set maximum shift")
            print("2. Input DNA sequences")
            print("3. Calculate number of matches (No shifts)")
            print("4. Calculate chain after shifts (Maximum score)")
            print("5. Calculate maximum contiguous chain")
            print("6. Exit")

            option = input("Select an option: ")

            if option == "1":
                max_shift = int(input("Enter the maximum shift value: "))
            elif option == "2":
                sequence1 = input("Enter the first DNA sequence: ").upper()
                sequence2 = input("Enter the second DNA sequence: ").upper()
            elif option == "3":
                if sequence1 and sequence2:
                    matches = calculate_number_of_matches(sequence1, sequence2)
                    print(f"Number of matches: {matches} (No shifts)")
                else:
                    print("DNA sequences not provided.")
            elif option == "4":
                if sequence1 and sequence2 and max_shift is not None:
                    max_score = 0
                    for shift in range(max_shift + 1):
                        score = shift_and_calculate_score(sequence1, shift, sequence2)
                        if score > max_score:
                            max_score = score
                            best_shift = shift
                    print(
                        f"Best score after shifting by {best_shift} cells: {max_score}"
                    )
                else:
                    print("DNA sequences or maximum shift not provided.")
            elif option == "5":
                if sequence1:
                    max_chain = find_maximum_contiguous_chain(sequence1, sequence2)
                    print(f"Maximum contiguous chain: {max_chain}")
                else:
                    print("DNA sequence not provided.")
            elif option == "6":
                print("Exiting the program.")
                sys.exit()
            else:
                print("Invalid option. Please select a valid option.")

    except Exception as e:
        print(f"An error occurred: {e}")


if _name_ == "_main_":
    main()
