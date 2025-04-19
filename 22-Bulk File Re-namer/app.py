import os
from typing import Optional

def bulk_rename_files(
    directory: str,
    prefix: str = "",
    suffix: str = "",
    replace_text: Optional[str] = None,
    new_text: Optional[str] = None,
    to_lowercase: bool = False,
    to_uppercase: bool = False
) -> None:
    """
    Renames all files in the specified directory based on the given rules.

    :param directory: Path to the directory containing the files.
    :param prefix: Text to add at the beginning of each filename.
    :param suffix: Text to add at the end of each filename (before the extension).
    :param replace_text: Text to replace in the filename.
    :param new_text: New text to replace the `replace_text`.
    :param to_lowercase: Convert filename to lowercase.
    :param to_uppercase: Convert filename to uppercase.
    """
    if not os.path.isdir(directory):
        print(f"Error: Directory '{directory}' does not exist or is not a directory.")
        return

    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    if not files:
        print("No files found in the directory.")
        return

    print(f"Found {len(files)} files in '{directory}'.")

    for filename in files:
        name, ext = os.path.splitext(filename)

        if replace_text and new_text:
            name = name.replace(replace_text, new_text)

        if to_lowercase:
            name = name.lower()
        elif to_uppercase:
            name = name.upper()

        new_name = f"{prefix}{name}{suffix}{ext}"
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)

        if old_path != new_path:  # Avoid renaming if the name is unchanged
            if not os.path.exists(new_path):
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} -> {new_name}")
            else:
                print(f"Skipped: {filename} (File with new name already exists)")

    print("Renaming completed!")

if __name__ == "__main__":
    directory = input("Enter the directory path: ").strip()
    prefix = input("Enter prefix (leave blank for none): ").strip()
    suffix = input("Enter suffix (leave blank for none): ").strip()
    replace_text = input("Enter text to replace (leave blank for none): ").strip() or None
    new_text = input("Enter new text (leave blank for none): ").strip() or None
    to_lowercase = input("Convert filenames to lowercase? (y/n): ").strip().lower() == "y"
    to_uppercase = input("Convert filenames to uppercase? (y/n): ").strip().lower() == "y"

    bulk_rename_files(
        directory=directory,
        prefix=prefix,
        suffix=suffix,
        replace_text=replace_text,
        new_text=new_text,
        to_lowercase=to_lowercase,
        to_uppercase=to_uppercase
    )
