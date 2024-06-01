import os
import json


def directory_structure_to_dict(directory, current_id=[0]):
    """
    Creates a dictionary representing the directory structure with unique id-numbers for subdirectories.
    """
    directory_dict = {}
    for root, dirs, files in os.walk(directory):
        path = root.split(os.sep)
        if root == directory:
            for subdir in dirs:
                if subdir == '__pycache__':
                    continue
                subdir_path = os.path.join(root, subdir)
                subdir_id = current_id[0]
                current_id[0] += 1
                directory_dict[subdir] = directory_structure_to_dict(subdir_path, current_id)
                directory_dict[subdir]['id-number'] = subdir_id
                directory_dict[subdir]['__files__'] = [os.path.join(subdir_path, file).replace('/', '\\') for file in
                                                       os.listdir(subdir_path) if
                                                       os.path.isfile(os.path.join(subdir_path, file))]
        else:
            for subdir in dirs:
                if subdir == '__pycache__':
                    continue
                subdir_path = os.path.join(root, subdir)
                subdir_id = current_id[0]
                current_id[0] += 1
                directory_dict[subdir] = directory_structure_to_dict(subdir_path, current_id)
                directory_dict[subdir]['id-number'] = subdir_id
                directory_dict[subdir]['__files__'] = [os.path.join(subdir_path, file).replace('/', '\\') for file in
                                                       os.listdir(subdir_path) if
                                                       os.path.isfile(os.path.join(subdir_path, file))]
            break
    return directory_dict


def save_directory_structure_to_json(directory, output_file):
    """
    Saves the directory structure to a JSON file with unique id-numbers for subdirectories.
    """
    structure_dict = {'modules': directory_structure_to_dict(directory)}
    with open(output_file, 'w') as json_file:
        json.dump(structure_dict, json_file, indent=4)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Save the subdirectories and files in those subdirectories in a JSON file with unique id-numbers for subdirectories.")
    parser.add_argument("directory", help="The directory to scan")
    parser.add_argument("output_file", help="The output JSON file")

    args = parser.parse_args()

    save_directory_structure_to_json(args.directory, args.output_file)

