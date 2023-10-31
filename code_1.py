# Function to read DNA sequences from a file
def read_sequences_from_file(filename):
    sequences = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                sequences.append(line.strip())
    except FileNotFoundError:
        print("File not found.")
    return sequences


# Function to calculate the number of matches between two DNA sequences
def calculate_matches(sequence1, sequence2):
    match_count = sum(char1 == char2 and char1 != '-' for char1, char2 in zip(sequence1, sequence2))
    return match_count


# Function to calculate the maximum contiguous chain between two DNA sequences
def calculate_max_contiguous_chain(sequence1, sequence2):
    max_contiguous_chain = 0
    current_contiguous_chain = 0

    for char1, char2 in zip(sequence1, sequence2):
        if char1 == char2 and char1 != '-':
            current_contiguous_chain += 1
            max_contiguous_chain = max(max_contiguous_chain, current_contiguous_chain)
        else:
            current_contiguous_chain = 0

    return max_contiguous_chain


# Function to set the maximum shift based on user input
def set_max_shift():
    max_shift = int(input("Enter the maximum shift: "))
    return max_shift


# Function to calculate the number of matches with shifts iterating through the maximum shift
def calculate_matches_with_shifts(sequence1, sequence2, max_shift):
    max_match_count = 0
    best_shift = 0

    for shift in range(0, max_shift + 1):
        #shifted_sequence1 = sequence1[-shift:] + sequence1[:-shift]
        tmp_sequence1 = ("-" * shift) + sequence1
        tmp_sequence2 = sequence2 + ("-" * shift)
        tmp_sequence2 += (len(tmp_sequence1) - len(tmp_sequence2)) * "-"
        tmp_sequence1 += (len(tmp_sequence2) - len(tmp_sequence1)) * "-"
        print("-------------------------", shift)
        print("SEQ 1:", tmp_sequence1)
        print("SEQ 2:", tmp_sequence2)
        match_count = calculate_matches(tmp_sequence1, tmp_sequence2)
        print('Match Count:', match_count)

        if match_count > max_match_count:
            max_match_count = match_count
            best_shift = shift
    
    for shift in range(0, max_shift + 1):
        tmp_sequence2 = ("-" * shift) + sequence2
        tmp_sequence1 = sequence1 + ("-" * shift)
        tmp_sequence1 += (len(tmp_sequence2) - len(tmp_sequence1)) * "-"
        tmp_sequence2 += (len(tmp_sequence1) - len(tmp_sequence2)) * "-"
        print("-------------------------", shift)
        print("SEQ 1:", tmp_sequence1)
        print("SEQ 2:", tmp_sequence2)
        match_count = calculate_matches(tmp_sequence1, tmp_sequence2)
        print('Match Count:', match_count)

        if match_count > max_match_count:
            max_match_count = match_count
            best_shift = shift

    return max_match_count, best_shift


# Function to calculate the maximum contiguous chain with shifts iterating through the maximum shift
def calculate_max_contiguous_chain_with_shifts(sequence1, sequence2, max_shift):
    max_contiguous_chain = 0
    best_shift = 0

    for shift in range(0, max_shift + 1):
        #shifted_sequence1 = sequence1[-shift:] + sequence1[:-shift]
        tmp_sequence1 = ("-" * shift) + sequence1
        tmp_sequence2 = sequence2 + ("-" * shift)
        tmp_sequence2 += (len(tmp_sequence1) - len(tmp_sequence2)) * "-"
        tmp_sequence2 += (len(tmp_sequence2) - len(tmp_sequence1)) * "-"
        print("-------------------------", shift)
        print("SEQ 1:", tmp_sequence1)
        print("SEQ 2:", tmp_sequence2)
        match_count = calculate_max_contiguous_chain(tmp_sequence1, tmp_sequence2)
        print('Match Chain:', match_count)

        if match_count > max_contiguous_chain:
            max_contiguous_chain = match_count
            best_shift = shift
    
    for shift in range(0, max_shift + 1):
        tmp_sequence2 = ("-" * shift) + sequence2
        tmp_sequence1 = sequence1 + ("-" * shift)
        tmp_sequence2 += (len(tmp_sequence2) - len(tmp_sequence1)) * "-"
        tmp_sequence2 += (len(tmp_sequence1) - len(tmp_sequence2)) * "-"
        print("-------------------------", shift)
        print("SEQ 1:", tmp_sequence1)
        print("SEQ 2:", tmp_sequence2)
        match_count = calculate_max_contiguous_chain(tmp_sequence1, tmp_sequence2)
        print('Match Chain:', match_count)

        if match_count > max_contiguous_chain:
            max_contiguous_chain = match_count
            best_shift = shift

    return max_contiguous_chain, best_shift


# Main menu for user interaction
def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Calculate Number of Matches (Console Input)")
        print("2. Calculate Maximum Contiguous Chain (Console Input)")
        print("3. Calculate Number of Matches with Maximum Shift (Console Input)")
        print("4. Calculate Maximum Contiguous Chain with Maximum Shift (Console Input)")
        print("5. Calculate Number of Matches (File Input)")
        print("6. Calculate Maximum Contiguous Chain (File Input)")
        print("7. Calculate Number of Matches with Maximum Shift (File Input)")
        print("8. Calculate Maximum Contiguous Chain with Maximum Shift (File Input)")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            sequence1 = input("Enter the first DNA sequence: ").upper()
            sequence2 = input("Enter the second DNA sequence: ").upper()
            match_count = calculate_matches(sequence1, sequence2)
            print(f"Number of Matches without Shifts: {match_count}")
        elif choice == '2':
            sequence1 = input("Enter the first DNA sequence: ").upper()
            sequence2 = input("Enter the second DNA sequence: ").upper()
            max_contiguous_chain = calculate_max_contiguous_chain(sequence1, sequence2)
            print(f"Maximum Contiguous Chain without Shifts: {max_contiguous_chain}")
        elif choice == '3':
            sequence1 = input("Enter the first DNA sequence: ").upper()
            sequence2 = input("Enter the second DNA sequence: ").upper()
            max_shift = set_max_shift()
            max_match_count, best_shift = calculate_matches_with_shifts(sequence1, sequence2, max_shift)
            print(f"Number of Matches with Maximum Shift ({best_shift}): {max_match_count}")
        elif choice == '4':
            sequence1 = input("Enter the first DNA sequence: ").upper()
            sequence2 = input("Enter the second DNA sequence: ").upper()
            max_shift = set_max_shift()
            max_contiguous_chain, best_shift = calculate_max_contiguous_chain_with_shifts(sequence1, sequence2, max_shift)
            print(f"Maximum Contiguous Chain with Maximum Shift ({best_shift}): {max_contiguous_chain}")
        elif choice == '5':
            filename = input("Enter the filename: ")
            sequences = read_sequences_from_file(filename)
            if len(sequences) >= 2:
                match_count = calculate_matches(sequences[0], sequences[1])
                print(f"Number of Matches without Shifts: {match_count}")
            else:
                print("File must contain at least two sequences.")
        elif choice == '6':
            filename = input("Enter the filename: ")
            sequences = read_sequences_from_file(filename)
            if len(sequences) >= 2:
                max_contiguous_chain = calculate_max_contiguous_chain(sequences[0], sequences[1])
                print(f"Maximum Contiguous Chain without Shifts: {max_contiguous_chain}")
            else:
                print("File must contain at least two sequences.")
        elif choice == '7':
            filename = input("Enter the filename: ")
            sequences = read_sequences_from_file(filename)
            if len(sequences) >= 2:
                max_shift = set_max_shift()
                max_match_count, best_shift = calculate_matches_with_shifts(sequences[0], sequences[1], max_shift)
                print(f"Number of Matches with Maximum Shift ({best_shift}): {max_match_count}")
            else:
                print("File must contain at least two sequences.")
        elif choice == '8':
            filename = input("Enter the filename: ")
            sequences = read_sequences_from_file(filename)
            if len(sequences) >= 2:
                max_shift = set_max_shift()
                max_contiguous_chain, best_shift = calculate_max_contiguous_chain_with_shifts(sequences[0], sequences[1], max_shift)
                print(f"Maximum Contiguous Chain with Maximum Shift ({best_shift}): {max_contiguous_chain}")
            else:
                print("File must contain at least two sequences.")
        elif choice == '9':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main_menu()
