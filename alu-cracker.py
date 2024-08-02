import zipfile
from tqdm import tqdm

def crack_zip(zip_file, wordlist):
    # Load the wordlist
    with open(wordlist, 'r', encoding='latin-1') as file:
        passwords = file.readlines()

    # Initialize the zip file
    zip_file = zipfile.ZipFile(zip_file)

    # Iterate through the passwords
    for password in tqdm(passwords, "Cracking ZIP file"):
        try:
            zip_file.extractall(pwd=password.strip().encode())
            print(f"\n\033[1;31mPassword found: {password.strip()}\033[0m")
            print("\033[1;31mYES WE DID IT MAN!!!!!!!!!!!!!\033[0m")
            return
        except:
            continue

    print("\033[1;31mPassword not found in the wordlist.\033[0m")

def main():
    print("\033[1;31m---------------------------------------------------------------\033[0m")
    print("\033[1;31m---------------------------------------------------------------\033[0m")
    print("\033[1;31m                     ALU-CRACKER\033[0m")
    print("\033[1;31m---------------------------------------------------------------\033[0m")
    print("\033[1;31m---------------------------------------------------------------\033[0m")
    print('\033[1;31m                        "BY ALVANOSH JOJO"\033[0m')
    print("\033[1;31m---------------------------------------------------------------\033[0m")
    print("\033[1;31m---------------------------------------------------------------\033[0m")

    zip_file = input("\033[1;31mEnter the path to the zip file: \033[0m")
    wordlist = input("\033[1;31mEnter the path to the wordlist (e.g., /usr/share/wordlists/rockyou.txt): \033[0m")
    crack_zip(zip_file, wordlist)

if __name__ == '__main__':
    main()
