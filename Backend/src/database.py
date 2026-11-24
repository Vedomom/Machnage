import os

name_databases = []

for file in os.scandir("src/DB"):
    if file.is_file():
        if file.name.split(".")[-1] == "db":
            name_databases.append(file.name)