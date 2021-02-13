import requests
from bs4 import BeautifulSoup
import tldextract
list_of_references = []
# main_url = 'https://www.apple.com/'
# main_url= 'http://www.carameltechstudios.com/'
main_url = 'http://learnyouahaskell.com/'
# main_url = 'https://www.syedfaaizhussain.com/'
global count
count = 1
Domain_of_main_url = tldextract.extract(main_url)
list_of_references.append(main_url)
source_code_of_main_url = requests.get(main_url)
print(count)
print(main_url)
with open(str(count) + '.html', 'wb') as f:
    f.write(source_code_of_main_url.content)
    f.close()
global index
index=0
while True:
    # print("hello")
    length = len(list_of_references)
    # print(length)
    if index < length:
        url = list_of_references[index]
        # print(url)
        source_code = requests.get(url)
        web_content = source_code.text
        soup = BeautifulSoup(web_content, "html.parser")
        # print("hello")
        for link in soup.findAll('a', href = True):
            # print("hello")
            reference_link = link.get('href')
            reference_link = str(reference_link)
            domain_of_reference_link = tldextract.extract(reference_link)
            if domain_of_reference_link.domain == Domain_of_main_url.domain:
                source_code_of_reference_link = requests.get(reference_link)
                # web_content_of_reference_link = source_code_of_reference_link.text
                # soup2 = BeautifulSoup(web_content_of_reference_link, "html.parser")
                # if soup2.title.string is not '':
                # if '404' not in soup2.title.string or '400' not in soup2.title.string:
                if reference_link in list_of_references or "javascript" in reference_link or "#" in reference_link or "mailto" in reference_link or "cache" in reference_link or "None" in reference_link:
                    continue
                else:
                    list_of_references.append(reference_link)
                    count += 1
                    print(count)
                    print(reference_link)
                    with open(str(count) + '.html', 'wb') as f:
                        f.write(source_code_of_reference_link.content)
                        f.close()
            else:
                if 'https://' in reference_link or 'http://' in reference_link or 'www' in reference_link or 'irc://' in reference_link:
                    continue
                else:
                    reference_link = main_url + reference_link
                    # print (reference_link)
                    source_code_of_reference_link = requests.get(reference_link)
                    # web_content_of_reference_link = source_code_of_reference_link.text
                    # soup2 = BeautifulSoup(web_content_of_reference_link, features= "html.parser")
                    # if soup2.title.string is not '':
                    # if '404' not in soup2.title.string or '400' not in soup2.title.string:
                    if reference_link in list_of_references or "javascript" in reference_link or "#" in reference_link or "mailto" in reference_link or "cache" in reference_link or "None" in reference_link:
                        # print(reference_link)
                        continue
                    else:
                        list_of_references.append(reference_link)
                        count += 1
                        print (count)
                        print (reference_link)
                        with open(str(count) + '.html', 'wb') as f:
                            f.write(source_code_of_reference_link.content)
                            f.close()
        index += 1
    else:
        print("Done crawling this url")
        break
