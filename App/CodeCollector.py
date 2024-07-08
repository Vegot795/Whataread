import os


def collect_code(modules, main_file, output_file):
    collected_code = []

    # Add main.py to the list of files to collect code from
    modules.append(main_file)

    for module_name in modules:
        try:
            with open(module_name + '.py', 'r') as file:
                collected_code.append(f"# Code from module: {module_name}\n")
                collected_code.extend(file.readlines())
                collected_code.append("\n\n")
        except FileNotFoundError:
            print(f"Module '{module_name}' not found.")

    # Write collected code to output file (overwriting existing content)
    with open(output_file, 'w') as outfile:
        outfile.writelines(collected_code)


if __name__ == "__main__":
    # List of module names to collect code from
    modules_to_collect = ['AddBookMod', 'AppMod', 'BookMod',  'EditBookMod', 'MoveButtonsMod']  # Adjust as per your actual module names

    # Main file (assuming it's named 'main.py')
    main_file = 'main'

    # Output file to save the collected code
    output_file = 'collected_code.txt'

    # Collect code from modules and main file, and save to file
    collect_code(modules_to_collect, main_file, output_file)
    print(f"Collected code from modules {modules_to_collect} and main file '{main_file}.py' saved to {output_file}")
