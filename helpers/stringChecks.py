import re


def isUrlContainedInString(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)
    return bool(url)

def isSubstackContainedInString(string):
    if "substack" in string:
        return True
    else:
        return False

def isNftContainedInString(string):  # true if there is nft word, false if not
    str1 = "nfts"
    str2 = "nft"
    str3 = "NFT"
    str4 = "NFTs"

    if str1 in string or str2 in string or str3 in string or str4 in string:
        return True
    else:
        return False
