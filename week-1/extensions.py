#.gif   .jpg   .jpeg   .png   .pdf   .txt   .zip

file = input("File name:" ).strip().lower()
if "." in file:
    first, last = file.rsplit(".",1)

    match last:
        case "gif":
            print(f"image/{last}")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "png":
            print(f"image/{last}")
        case "pdf":
            print(f"application/{last}")
        case "txt":
            print(f"text/{last}")
        case "zip":
            print(f"application/{last}")
        case _:
            print("application/octet-stream")
else:
    print("application/octet-stream")
