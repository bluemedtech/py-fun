import csv

def count_data_lines(file_path):
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            # Skip the header if there is one
            next(reader, None)
            
            data_line_count = 0
            for row in reader:
                data_line_count += 1
                # Print progress every 100,000 lines
                if data_line_count % 1000000 == 0:
                    print(f"Lines read so far: {data_line_count}")
            
            print(f"Total number of data lines: {data_line_count}")
            return data_line_count
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Example usage
file_path = r"C:\med\dev\py-upload\rawdata\raw\update-patches\25-01\pp-monthly-update-new-version.csv"
num_lines = count_data_lines(file_path)
if num_lines is not None:
    print(f"The number of data lines in the CSV file is: {num_lines}")