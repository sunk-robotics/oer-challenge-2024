import requests
from bs4 import BeautifulSoup
import os
import urllib.request

folder_path = "images/"

print("imported")

used_urls = []


# Function to create a directory for saving images
def create_image_directory(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)


# Function to download images
def download_image(url, folder_path, image_name):
    full_path = os.path.join(folder_path, image_name)
    try:
        urllib.request.urlretrieve(url, full_path)
        used_urls.append(url)
    except:
        pass
    print(f"Downloaded {image_name}")


# Function to search and download chicken images
def search_images():
    print("searching...")
    url = "https://duckduckgo.com/?t=ffab&q=serpent+stars&iax=images&ia=images"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    print("received data")

    soup = BeautifulSoup(response.text, "html.parser")

    print("parsed!")

    image_tags = soup.find_all("img")

    print("Search Done!")

    create_image_directory(folder_path)

    for i, img_tag in enumerate(image_tags):
        img_url = img_tag.get("src")
        if img_url and img_url.startswith("http") and img_url not in used_urls:
            image_name = f"chicken_{i}.jpg"
            download_image(img_url, folder_path, image_name)


def clean_up():
    files = os.listdir(folder_path)
    for i, file in enumerate(files):
        os.rename(file, folder_path + "/" + str(i + 1) + ".jpg")


if __name__ == "__main__":
    search_images()
    input("Finished! Press enter when finalizing shall be executed... ")
    clean_up()
