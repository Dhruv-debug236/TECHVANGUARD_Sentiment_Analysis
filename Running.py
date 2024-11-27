import pickle

# Read the code from the Python file
with open("Sentiment_dashboard.py", "r") as code_file:
    code_content = code_file.read()

# Save the code content as a .pkl file
with open("my_script.pkl", "wb") as pkl_file:
    pickle.dump(code_content, pkl_file)

print("Python code saved as a .pkl file.")
