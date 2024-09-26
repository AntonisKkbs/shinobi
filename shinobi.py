import subprocess
import time

print(r'  __  __  __ __ __  __   ___   ____  __')
print(r' (( \ ||  || || ||\ ||  // \\  || )) ||')
print(r'  \\  ||==|| || ||\\|| ((   )) ||=)  ||')
print(r' \_)) ||  || || || \||  \\_//  ||_)) ||')
print(r'                                       ')

print("こんにちわ!")
print("I am your shinobi! Please give me your target and let everything on me.\n")

target = input("Target url: ")

print("[+] Exporting informations to urls.txt\n")

time.sleep(3.0)

print("*" * 10, 'Target urls', "*" * 10)

subprocess.call(f'waybackurls {target} | anew urls.txt', shell= True)

time.sleep(2.0)

print("\n[+] Shinobi is crawling into the urls.txt\n")


print("*" * 10, 'Unique paths', "*" * 10)


subprocess.call("cat urls.txt | katana | hakrawler -d 3 | anew shinobi_report.txt", shell= True)

time.sleep(2.0)
    
print("*" * 10, 'Unique paths', "*" * 10)

# Get unique paths only
subprocess.call("cat shinobi_report.txt urls.txt | unfurl format %p | anew unique_paths.txt", shell = True)

time.sleep(2.0)

print("*" * 10, 'Extracted subdomains', "*" * 10)
# Extract the subdomains
subprocess.call("cat shinobi_report.txt urls.txt | unfurl format %d | anew subs.txt", shell= True)
