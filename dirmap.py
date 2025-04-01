#!/usr/bin/env python3

import os
import argparse
from pathlib import Path
import sys

def generate_folder_structure(directory_path, indent="", is_last=True, max_depth=None, 
                             current_depth=0, ignore_patterns=None, max_files=None):
    """
    Recursively generate a tree-like folder structure visualization.
    
    Args:
        directory_path: Path to the directory to analyze
        indent: Current indentation string
        is_last: Whether this is the last item in the current level
        max_depth: Maximum depth to traverse (None for unlimited)
        current_depth: Current traversal depth
        ignore_patterns: List of patterns to ignore
        max_files: Maximum number of files to show per directory
    """
    if max_depth is not None and current_depth > max_depth:
        return
    
    path = Path(directory_path)
    basename = path.name
    
    # Skip if matches ignore pattern
    if ignore_patterns and any(pattern in str(path) for pattern in ignore_patterns):
        return
    
    # Print the current directory/file
    connector = "└── " if is_last else "├── "
    print(f"{indent}{connector}{basename}", end="")
    
    # Add comment for file types if needed
    if path.is_file():
        extension = path.suffix.lower()
        comment = ""
        if extension == ".py":
            comment = "# Python script"
        elif extension == ".css":
            comment = "# CSS styles"
        elif extension == ".js":
            comment = "# JavaScript code"
        elif extension == ".html":
            comment = "# HTML template"
        elif extension == ".json":
            comment = "# JSON data"
        
        if comment:
            print(f"  {comment}")
        else:
            print()
    else:
        print()  # Just a newline for directories
    
    # If it's a directory, process its contents
    if path.is_dir():
        # Get all items and sort them (directories first, then files)
        items = list(path.iterdir())
        dirs = [item for item in items if item.is_dir()]
        files = [item for item in items if item.is_file()]
        
        # Sort directories and files alphabetically
        dirs.sort()
        files.sort()
        
        # Apply file limit if specified
        if max_files is not None and len(files) > max_files:
            files = files[:max_files]
            # We'll add an indicator for hidden files later
            has_hidden_files = True
        else:
            has_hidden_files = False
        
        # Combine sorted directories and files
        sorted_items = dirs + files
        
        # Process each item
        for i, item in enumerate(sorted_items):
            # Check if this is the last item (considering we might add a hidden files indicator)
            is_item_last = (i == len(sorted_items) - 1) and not (has_hidden_files and i == len(sorted_items) - 1)
            
            # Determine the new indent for the next level
            if is_last:
                new_indent = indent + "    "
            else:
                new_indent = indent + "│   "
            
            # Recursively process this item
            generate_folder_structure(
                item, 
                new_indent, 
                is_item_last, 
                max_depth, 
                current_depth + 1,
                ignore_patterns,
                max_files
            )
        
        # Add indicator for hidden files if needed
        if has_hidden_files:
            hidden_count = len(list(path.iterdir())) - len(sorted_items)
            if is_last:
                new_indent = indent + "    "
            else:
                new_indent = indent + "│   "
            print(f"{new_indent}└── ... {hidden_count} more file(s) not shown  # Use --max-files option to change limit")

def main():
    parser = argparse.ArgumentParser(description="Generate a folder structure visualization")
    parser.add_argument("path", nargs="?", default=".", help="Path to the directory to analyze")
    parser.add_argument("--max-depth", type=int, help="Maximum depth to traverse")
    parser.add_argument("--max-files", type=int, help="Maximum number of files to show per directory")
    parser.add_argument("--ignore", nargs="+", help="Patterns to ignore (e.g., __pycache__ .git)")
    
    args = parser.parse_args()
    
    try:
        directory_path = os.path.abspath(args.path)
        if not os.path.exists(directory_path):
            print(f"Error: Path '{args.path}' does not exist", file=sys.stderr)
            return 1
        
        # Print the root directory
        print(directory_path)
        
        # Generate the structure
        generate_folder_structure(
            directory_path, 
            max_depth=args.max_depth,
            ignore_patterns=args.ignore,
            max_files=args.max_files
        )
        return 0
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
