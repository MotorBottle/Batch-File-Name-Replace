import os

def batch_rename(fileType, directory, find, replace):
    for filename in os.listdir(directory):
        if filename.endswith(fileType):
            new_filename = filename.replace(find, replace)
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

# Provide the directory path, find, and replace values
fileType = ".mp4"
directory = "D:\纸牌屋\纸牌屋S2"
find = "纸牌屋第02季第"
replace = "House.of.Cards.S02E"

batch_rename(fileType, directory, find, replace)

