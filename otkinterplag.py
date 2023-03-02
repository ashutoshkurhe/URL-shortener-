import difflib
import tkinter as tk
import difflib
import requests
from functools import *
from bs4 import BeautifulSoup
from googlesearch import search

def check_plagiarism():

    query = entry1.get("1.0", tk.END)
    text = entry2.get("1.0", tk.END)
    print(query)
    print(text)


    # Get the search results from Google
    urls = search(query, num_results=10)
   
    
    # Check each URL for plagiarism

    for url in urls:

        # Get the web page content using requests
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        # Extract the text content from the web page
        page_text = soup.get_text()
        # Compare the text content with the given text
        s = difflib.SequenceMatcher(None, text, page_text)
        plagiarism = s.ratio() * 100
        
        if plagiarism >= 0: # If the plagiarism percentage is above 80%
            result_label.config(text="Plagiarism Percentage: {:.2f}%".format(plagiarism))
            return "Plagiarism detected: {}% similar content found at {}".format(plagiarism, url)
    return "No plagiarism detected"


root = tk.Tk()
root.title("Plagiarism Checker")


label1 = tk.Label(root, text="Enter search hint:")
label1.grid(row=0, column=0, padx=5, pady=5)

entry1 = tk.Text(root, height=10, width=50)
entry1.grid(row=1, column=0, padx=5, pady=5)

label2 = tk.Label(root, text="Enter Text For Check Plagarism")
label2.grid(row=2, column=0, padx=5, pady=5)

entry2 = tk.Text(root, height=10, width=50)
entry2.grid(row=3, column=0, padx=5, pady=5)


# check_plagiarism = partial(check_plagiarism, entry1,entry2)
check_button = tk.Button(root, text="Check Plagiarism", command=check_plagiarism)
check_button.grid(row=4, column=0, padx=5, pady=5)
# check_button.pack()





result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, padx=5, pady=5)

root.mainloop()
