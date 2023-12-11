# prompt user for file name
prompt = input("File name: ").lower().strip()

# make a dictionnary matching file ext with the MIME 
dic = {
    ".gif": "image/gif",
    ".jpeg": "image/jpeg",
    ".jpg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}

# Develop the logic to handle different cases
if prompt[-5:] in dic:
    print(dic[prompt[-5:]])

elif prompt[-4:] in dic:
    print(dic[prompt[-4:]])
    
else:
    print("application/octet-stream")