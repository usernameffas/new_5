import numpy as np
import os

def design_dome():
    """
    Analyzes Mars base parts data to find and save weak parts.
    """
    # Define the file paths
    files = ['mars_base_main_parts-001.csv', 'mars_base_main_parts-002.csv', 'mars_base_main_parts-003.csv']
    arr_list = []

    # Load the three CSV files into numpy arrays
    try:
        for file in files:
            # Check if the file exists before loading
            if not os.path.exists(file):
                print(f"Error: The file '{file}' was not found.")
                return
            arr_list.append(np.loadtxt(file, delimiter=','))
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        return

    # Merge the three arrays into one
    parts = np.concatenate(arr_list, axis=0)

    # Calculate the average value
    average_value = np.mean(parts)
    print(f"The average value of all parts is: {average_value}")

    # Find values less than 50
    parts_to_work_on = parts[parts < 50]

    # Save the filtered values to a new CSV file
    output_filename = 'parts_to_work_on.csv'
    try:
        np.savetxt(output_filename, parts_to_work_on, fmt='%d', delimiter=',')
        print(f"Successfully saved '{output_filename}'.")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")

if __name__ == '__main__':
    design_dome()
