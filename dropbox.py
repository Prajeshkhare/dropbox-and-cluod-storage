from msilib.schema import File
import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self, file_from , file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from,"rb")
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = "sl.BBJj1OvgnFEhYsuYkYxw0v1thgc9Gwq89c08GkJrBrrBoZ525aXldH4b6mWeKlEvaP8MZa8LmJ62govoWZoNtRKgT5njzdaqwEDuW7GMai3F3MZp4V8XuvkAzRja3gQZhhKQAtE"
    transferData = TransferData(access_token)

    # file_from = input("enter the file path to transfer : ")
    # file_to = input("enter the full path to upload file to dropbox : ")

    file_from = "text.txt"
    file_to = "/test_dropbox1/text.txt"

    transferData.upload_file(file_from,file_to)
    print("file has been moved")

main()

    