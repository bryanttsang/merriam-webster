from selenium import webdriver

# only lowercase letters allowed
def isalphabetical(word):
    for letter in list(word):
        if (letter < 'a' or letter > 'z'):
            return False
    return True

driver = webdriver.PhantomJS()

dictionary = []
for letter in range(ord('a'), ord('z')+1):
    driver.get("https://www.merriam-webster.com/browse/dictionary/%c/1" %chr(letter))
    
    mp = driver.find_element_by_class_name("counters").text
    maxpage = int(mp[mp.rindex(" ")+1:])
    print("\n%c: MAX PAGE = %d" %(chr(letter-32), maxpage))

    for page in range(1, maxpage+1):
        driver.get("https://www.merriam-webster.com/browse/dictionary/%c/%d" %(chr(letter), page))
        words = driver.find_element_by_class_name("entries").text.split("\n")
        dictionary = dictionary + list(filter(lambda word: isalphabetical(word) and len(set(word)) >= 2, words))
        print("%c: PAGE %d" %(chr(letter-32), page))

driver.quit()

f = open("dict.txt", "w")
for word in dictionary:
    f.write("%s\n" %word)
f.close()
