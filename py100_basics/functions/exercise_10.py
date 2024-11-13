def extract_region(locale):
    return locale.split(".")[0].split("_")[1]

print(extract_region('en_US.UTF-8'))      # en
print(extract_region('en_GB.UTF-8'))      # en
print(extract_region('ko_KR.UTF-16'))     # ko