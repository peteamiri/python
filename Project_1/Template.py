import argparse

def process_arguments():
    parser = argparse.ArgumentParser(description="Process some arguments.")
    parser.add_argument('-i', '--input_file', required=True, help='Path to the input file')
    parser.add_argument('-o', '--output_file', required=True, help='Path to the output file')
    parser.add_argument('-s', '--substitutions_file', help='Path to the substitutions file')

    return parser.parse_args()

def substitute_variables(template_file, output_file, substitutions_file=None):
    # Read template file
    with open(template_file, 'r') as file:
        template_content = file.read()

    # Read substitutions from file if provided
    substitutions = {}
    if substitutions_file:
        with open(substitutions_file, 'r') as file:
            substitutions = json.load(file)

    # Substitute variables in the template content
    substituted_content = template_content.format(**substitutions)

    # Write the substituted content into the output file
    with open(output_file, 'w') as file:
        file.write(substituted_content)

if __name__ == "__main__":
    args = process_arguments()
    template_file = args.input_file
    output_file = args.output_file
    substitutions_file = args.substitutions_file

    substitute_variables(template_file, output_file, substitutions_file)

