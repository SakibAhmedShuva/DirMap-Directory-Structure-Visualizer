#!/usr/bin/env python3

import os
import argparse
from pathlib import Path
import sys
import time

def generate_folder_structure(directory_path, indent="", is_last=True, max_depth=None, 
                             current_depth=0, ignore_patterns=None, max_files=None, 
                             output_file=None):
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
        output_file: File object to write output to (None for stdout)
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
    line = f"{indent}{connector}{basename}"
    
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
        elif extension == ".md":
            comment = "# Markdown documentation"
        elif extension == ".yml" or extension == ".yaml":
            comment = "# YAML configuration"
        elif extension == ".txt":
            comment = "# Text file"
        elif extension == ".csv":
            comment = "# CSV data"
        elif extension == ".sh":
            comment = "# Shell script"
        elif extension == ".java":
            comment = "# Java source code"
        elif extension == ".cpp" or extension == ".cc":
            comment = "# C++ source code"
        elif extension == ".c":
            comment = "# C source code"
        elif extension == ".h" or extension == ".hpp":
            comment = "# Header file"
        elif extension == ".go":
            comment = "# Go source code"
        elif extension == ".rs":
            comment = "# Rust source code"
        elif extension == ".php":
            comment = "# PHP script"
        elif extension == ".rb":
            comment = "# Ruby script"
        elif extension == ".ts":
            comment = "# TypeScript code"
        elif extension == ".jsx" or extension == ".tsx":
            comment = "# React component"
        elif extension == ".sql":
            comment = "# SQL query"
        elif extension == ".xml":
            comment = "# XML data"
        elif extension == ".env":
            comment = "# Environment variables"
        elif extension == ".gitignore":
            comment = "# Git ignore rules"
        elif extension == ".dockerignore":
            comment = "# Docker ignore rules"
        elif extension == ".dockerfile" or basename.lower() == "dockerfile":
            comment = "# Docker build instructions"
        
        if comment:
            line += f"  {comment}"
    
    # Print the line
    if output_file:
        print(line, file=output_file)
    else:
        print(line)
    
    # If it's a directory, process its contents
    if path.is_dir():
        try:
            # Get all items and sort them (directories first, then files)
            items = list(path.iterdir())
            dirs = [item for item in items if item.is_dir()]
            files = [item for item in items if item.is_file()]
            
            # Sort directories and files alphabetically
            dirs.sort()
            files.sort()
            
            # Apply file limit if specified
            hidden_file_count = 0
            if max_files is not None and len(files) > max_files:
                hidden_file_count = len(files) - max_files
                files = files[:max_files]
                has_hidden_files = True
            else:
                has_hidden_files = False
            
            # Combine sorted directories and files
            sorted_items = dirs + files
            
            # Process each item
            for i, item in enumerate(sorted_items):
                # Check if this is the last item (considering we might add a hidden files indicator)
                is_item_last = (i == len(sorted_items) - 1) and not has_hidden_files
                
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
                    max_files,
                    output_file
                )
            
            # Add indicator for hidden files if needed
            if has_hidden_files:
                if is_last:
                    new_indent = indent + "    "
                else:
                    new_indent = indent + "│   "
                hidden_line = f"{new_indent}└── ... {hidden_file_count} more file(s) not shown  # Use --max-files option to change limit"
                if output_file:
                    print(hidden_line, file=output_file)
                else:
                    print(hidden_line)
        except PermissionError:
            error_line = f"{indent}    └── [Permission denied]"
            if output_file:
                print(error_line, file=output_file)
            else:
                print(error_line)

def main():
    parser = argparse.ArgumentParser(description="Generate a folder structure visualization")
    parser.add_argument("path", nargs="?", default=".", help="Path to the directory to analyze")
    parser.add_argument("--max-depth", type=int, help="Maximum depth to traverse")
    parser.add_argument("--max-files", type=int, default=None, help="Maximum number of files to show per directory")
    parser.add_argument("--ignore", nargs="+", help="Patterns to ignore (e.g., __pycache__ .git)")
    parser.add_argument("--output", "-o", help="Output file path (default: print to console)")
    parser.add_argument("--version", "-v", action="version", version="DirMap v1.0.0")
    
    args = parser.parse_args()
    
    try:
        directory_path = os.path.abspath(args.path)
        if not os.path.exists(directory_path):
            print(f"Error: Path '{args.path}' does not exist", file=sys.stderr)
            return 1
        
        output_file = None
        try:
            if args.output:
                output_file = open(args.output, 'w', encoding='utf-8')
            
            # Print the root directory
            if output_file:
                print(directory_path, file=output_file)
            else:
                print(directory_path)
            
            start_time = time.time()
            
            # Generate the structure
            generate_folder_structure(
                directory_path, 
                max_depth=args.max_depth,
                ignore_patterns=args.ignore,
                max_files=args.max_files,
                output_file=output_file
            )
            
            elapsed_time = time.time() - start_time
            
            # Print summary
            summary = f"\nGenerated in {elapsed_time:.2f} seconds"
            if output_file:
                print(summary, file=output_file)
            else:
                print(summary)
                
            return 0
            
        finally:
            if output_file:
                output_file.close()
                print(f"Output written to {args.output}")
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
