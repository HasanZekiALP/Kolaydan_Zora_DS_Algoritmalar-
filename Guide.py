# Guide for Python 

import os

repo = "HasanZekiALP/Kolaydan_Zora_DS_Algoritmalar-"
base_url = "https://colab.research.google.com/github"

for file in os.listdir("."):
    if file.endswith(".ipynb"):
        print(f"- [{file}]({base_url}/{repo}/blob/main/{file})")
