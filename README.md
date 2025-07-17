# 📦 GitHub File Splitter & Merger Tool

Many developers struggle with GitHub’s file size limits. This tool solves that.

## 🚀 Features

- 🔹 Split large files (>100MB) into GitHub-safe 40MB chunks
- 🔹 Reconstruct files back to original
- 🔹 Optional zip/unzip utility for directories
- 🔒 Binary-safe and works cross-platform

---

## 📁 Usage

### 1. Split a file into 40MB chunks
```bash
python file_split_merge.py split my_data.zip --size 40
```

### 2. Merge chunks back into one file
```bash
python file_split_merge.py merge my_data.zip --output restored.zip
```

### 3. Zip a folder 
```bash
python zip_unzip_tool.py zip my_folder/ --output my_data.zip
```

### 4. Unzip a file
```bash
python zip_unzip_tool.py unzip my_data.zip --output ./restored_folder/
```

## 📂 Example Workflow
```bash
zip -r my_data.zip my_folder/
python file_split_merge.py split my_data.zip
# Upload to GitHub

# Later...
python file_split_merge.py merge my_data.zip --output my_data_restored.zip
unzip my_data_restored.zip
```

## 😉 Author
[Kumar Anurag](https://kmranrg.com)
