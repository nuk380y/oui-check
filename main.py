import os
import urllib.error
import urllib.request

def main():
    # Declare dictionary of database type (key) and URL (value).
    link_dict = {
        "ma-l": "http://standards-oui.ieee.org/oui/oui.csv",
        "ma-m": "http://standards-oui.ieee.org/oui28/mam.csv",
        "ma-s": "http://standards-oui.ieee.org/oui36/oui36.csv",
        "iab": "http://standards-oui.ieee.org/iab/iab.csv",
        "cid": "http://standards-oui.ieee.org/cid/cid.csv",
        "ethertype": "http://standards-oui.ieee.org/ethertype/eth.csv",
        "manid": "http://standards-oui.ieee.org/manid/manid.csv",
        "opid": "http://standards-oui.ieee.org/bopid/opid.csv",
    }
    # Define filepath for local temporary directory.
    temp_dir = "temp"
    try:
        os.mkdir(f"./{temp_dir}")
        print(f"Directory '{temp_dir}' created!")
    except FileExistsError:
        pass
    
    for key in link_dict:
        print(f"Downloading {key} database from IEEE...")
        # Rename file to be readily understood when looking at file artifacts.
        file_name = f"{key}.csv"
        file_path = f"{temp_dir}/{file_name}"
        # Request the file from the remote server.
        try:
            urllib.request.urlretrieve(link_dict[key], file_path)
        except urllib.error.HTTPError as e:
            print(f"HTTP Error: {e.code} - {e.reason}")
            print(f"Error URL: {e.url}")
        except urllib.error.URLError as e:
            print(f"URL Error: {e.reason}")


if __name__ == "__main__":
    main()
