# 📝 DecodeLabs Project 1: To-Do Engine

## 📌 Overview
This repository contains my first milestone project as a Junior Python Developer at DecodeLabs. The **To-Do Engine** is a command-line interface (CLI) application built to demonstrate core backend engineering principles. It is not just a simple script; it is designed with a decoupled architecture that securely manages data in dynamic memory (the Heap) and ensures permanent storage through JSON serialization.

## 🚀 Features
* **Decoupled Architecture:** Strict separation between the Data Logic (Model) and the User Interface (View).
* **Persistent Storage:** Tasks are automatically serialized and saved to a `tasks.json` file, ensuring data survives process termination.
* **Dynamic File Resolution:** Utilizes the `os` module to dynamically locate the execution path, preventing "read-only" file system errors regardless of the terminal's working directory.
* **Professional Iteration:** Utilizes Python's `enumerate()` function for simultaneous index and value data access.
* **Execution Guard:** Implements `if __name__ == "__main__":` to ensure the program can be run directly or safely imported as a module by other systems.

## 🧠 System Architecture
This engine is built on the foundational **IPO Model**:
1. **Input (Data Entry):** The user interface securely captures human input.
2. **Process (Logic/Modification):** The API boundary routes commands to the core data functions.
3. **Output (Display/View):** The system dynamically formats the backend data into a human-readable layout.

## 💻 Installation & Usage

**1. Clone the repository**
```bash
git clone [https://github.com/mohitkumarjha1257-pixel/Task-1-MohitKumarJha.git](https://github.com/mohitkumarjha1257-pixel/Task-1-MohitKumarJha.git)
cd Task-1-MohitKumarJha
