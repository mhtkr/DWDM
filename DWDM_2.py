#Program of Data warehouse cleansing to input names from users (inconsistent) and format them.

def clean_name(name):
    """
    Cleans and formats a name to a consistent format: 'Firstname Lastname'.
    """
    # Remove leading/trailing spaces
    name = name.strip()
    
    # Replace multiple spaces with a single space
    name = " ".join(name.split())
    
    # Split the name into parts
    name_parts = name.split()
    
    # Capitalize each part of the name
    formatted_name = " ".join(part.capitalize() for part in name_parts)
    
    return formatted_name


def main():
    print("Welcome to the Data Warehouse Name Cleansing Program!")
    names = []
    
    # Input names from the user
    while True:
        name = input("Enter a name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        names.append(name)
    
    # Clean and format the names
    cleaned_names = [clean_name(name) for name in names]
    
    # Display the cleaned names
    print("\nFormatted Names:")
    for i, name in enumerate(cleaned_names, 1):
        print(f"{i}. {name}")


if __name__ == "__main__":
    main()
