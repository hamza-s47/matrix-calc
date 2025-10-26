import os
import numpy as np

class FileSystem:
    # Load .npy file
    def load_npy(self, file):
        try:
            data = np.load(file, allow_pickle=True)
            return data
        except FileNotFoundError:
            return f"Error: File '{file}' not found."
        except Exception as e:
            return f"Error while loading '{file}': {e}"
    
    # Save .npy file
    def save_npy(self, file, arr):
        try:
            os.makedirs("./outputs", exist_ok=True)
            np.save(f"./outputs/{file}", arr)
            return f"File saved successfully as './outputs/{file}.npy'"
        except Exception as e:
            return f"Error while saving file: {e}"

    # Load .txt file
    def load_txt(self, file, delimiter=None):
        try:
            return np.loadtxt(file, delimiter=delimiter)
        except FileNotFoundError:
            return f"Error: File '{file}' not found."
        except Exception as e:
            return f"Error while loading text file '{file}': {e}"

    # Save .txt file
    def save_txt(self, file, arr, delimiter=" "):
        try:
            os.makedirs("./outputs", exist_ok=True)
            if not file.endswith(".txt"):
                file+=".txt"
            np.savetxt(f"./outputs/{file}", arr, delimiter=delimiter, fmt="%s")
            return f"File saved successfully as './outputs/{file}'"
        except Exception as e:
            return f"Error while saving text file: {e}"

