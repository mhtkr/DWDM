#Program of Data warehouse cleansing to remove redundancy in data.

def remove_redundancy(data):
    """
    Removes redundant entries from the dataset and returns the cleaned data.
    """
    # Use a set to automatically remove duplicates
    cleaned_data = list(set(data))
    return cleaned_data


def main():
    print("Welcome to the Data Warehouse Redundancy Removal Program!")
    data = []
    
    # Input data from the user
    print("Enter data entries (type 'done' to finish):")
    while True:
        entry = input("> ").strip()
        if entry.lower() == 'done':
            break
        data.append(entry)
    
    # Remove redundancy
    cleaned_data = remove_redundancy(data)
    
    # Display results
    print("\nOriginal Data:")
    print(data)
    print("\nCleaned Data (Duplicates Removed):")
    print(cleaned_data)


if __name__ == "__main__":
    main()
