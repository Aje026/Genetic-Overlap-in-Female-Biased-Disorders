import os

# Specify the directory where your log files are located
log_files_directory = os.getcwd()  # Use the current working directory

# Loop through log files from 2.log to 36.log
for i in range(2, 38):
    log_file_path = f'{i}.log'
    
    # Read the contents of the log file
    with open(log_file_path, 'r') as file:
        log_contents = file.readlines()

    # Find the line number where the table starts
    start_line = None

    for j, line in enumerate(log_contents):
        if line.startswith('Summary of Genetic Correlation Results'):
            start_line = j 
            break

    # Extract the table lines
    if start_line is not None:
        table_lines = log_contents[start_line:]

        # Save the extracted table to a new file
        output_file_path = f'{i}_extracted_table.txt'
        with open(output_file_path, 'w') as output_file:
            output_file.writelines(table_lines)
    else:
        print(f"Table not found in {log_file_path}")
