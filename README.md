# DirMap: Directory Structure Visualizer

A powerful command-line tool that generates beautiful, customizable directory tree visualizations with smart file filtering and annotation capabilities.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

DirMap is a lightweight Python utility that helps you visualize directory structures with customizable depth and file limits. Perfect for documentation, project overviews, or understanding complex codebases at a glance.

## Features

- 🌲 Generate tree-like visualizations of directory structures
- 📊 Set maximum depth for large directory trees
- 🔍 Limit the number of files displayed per directory to avoid clutter
- 🚫 Ignore specific patterns or directories
- 🏷️ Automatic file type annotations for 25+ common extensions
- 📄 Export to file or print to console
- ⏱️ Performance metrics for large directories
- 💻 Simple command-line interface

## Installation

### Download the Script

```bash
# Clone the repository
git clone https://github.com/SakibAhmedShuva/DirMap-Folder-Directory-Structure-Visualizer.git

# Navigate to the directory
cd DirMap-Folder-Directory-Structure-Visualizer
```

No additional installation required! Just run the script directly with Python.

## Usage

### Basic Usage

```bash
python dirmap.py /path/to/your/directory
```

### Advanced Options

```bash
# Limit directory traversal depth
python dirmap.py /path/to/your/directory --max-depth 3

# Limit files shown per directory
python dirmap.py /path/to/your/directory --max-files 5

# Ignore specific patterns
python dirmap.py /path/to/your/directory --ignore __pycache__ .git node_modules

# Save output to a file
python dirmap.py /path/to/your/directory --output project_structure.txt

# Combine multiple options
python dirmap.py /path/to/your/directory --max-depth 3 --max-files 10 --ignore .git venv --output structure.txt
```

### Windows Path Example

```bash
python dirmap.py "D:\Projects\MyWebsite" --max-files 5
```

## Example Output

```
D:\Projects\MyWebsite
├── index.html  # HTML template
├── assets/
│   ├── css/
│   │   ├── main.css  # CSS styles
│   │   ├── normalize.css  # CSS styles
│   │   └── ... 3 more file(s) not shown  # Use --max-files option to change limit
│   ├── js/
│   │   ├── app.js  # JavaScript code
│   │   ├── utils.js  # JavaScript code
│   │   └── vendor/
│   └── images/
│       ├── logo.png
│       ├── banner.jpg
│       └── ... 8 more file(s) not shown  # Use --max-files option to change limit
└── README.md  # Markdown documentation

Generated in 0.03 seconds
```

## File Type Annotations

DirMap automatically adds helpful annotations for common file types:

| Extension | Annotation |
|-----------|------------|
| .py | Python script |
| .js | JavaScript code |
| .jsx, .tsx | React component |
| .ts | TypeScript code |
| .html | HTML template |
| .css | CSS styles |
| .json | JSON data |
| .md | Markdown documentation |
| .yml, .yaml | YAML configuration |
| .txt | Text file |
| .csv | CSV data |
| .sh | Shell script |
| .java | Java source code |
| .cpp, .cc | C++ source code |
| .c | C source code |
| .h, .hpp | Header file |
| .go | Go source code |
| .rs | Rust source code |
| .php | PHP script |
| .rb | Ruby script |
| .sql | SQL query |
| .xml | XML data |
| .env | Environment variables |
| .gitignore | Git ignore rules |
| .dockerignore | Docker ignore rules |
| Dockerfile | Docker build instructions |

## Use Cases

- **Project Documentation**: Include a directory structure in your README.md
- **Codebase Exploration**: Quickly understand the structure of a new project
- **Teaching**: Show students the organization of a project
- **Presentations**: Include directory structures in slides or documents
- **Repository Overview**: Provide a high-level view of your GitHub repository

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Comparison with Similar Tools

| Feature | DirMap | Unix `tree` | Windows `dir /s` |
|---------|--------|-------------|------------------|
| Cross-platform | ✅ | ❌ (Unix only) | ❌ (Windows only) |
| File type annotations | ✅ | ❌ | ❌ |
| File limiting | ✅ | ❌ | ❌ |
| Pattern ignoring | ✅ | Limited | ❌ |
| Output to file | ✅ | ✅ | ✅ |

## Customization

You can easily extend the file type annotations by modifying the script. Look for the section with file extensions and add your own mappings:

```python
# Add your custom extensions here
elif extension == ".your_extension":
    comment = "# Your custom comment"
```

## Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Ideas for Contributions

- Add colorized output
- Implement interactive mode
- Add size information for files
- Create file type statistics
- Add sorting options (by name, size, type)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by the Unix `tree` command
- Created to simplify project documentation

---

## Repository Structure

```
DirMap-Folder-Directory-Structure-Visualizer/
├── dirmap.py         # Main script
├── LICENSE           # MIT License
└── README.md         # This file
```
