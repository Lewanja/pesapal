# to isntall dependencies run command below
# pip install requests beautifulsoup4
# some functions yet to be implemented

import requests
from bs4 import BeautifulSoup
from collections import Counter


def get_all_words(web_page_link):
    # get web link as html
    response = requests.get(web_page_link)
    # parse html to text
    soup = BeautifulSoup(response.text, "html.parser")
    # clean by removing new lines and spaces
    all_words_combined = soup.get_text()
    all_words_combined = all_words_combined.replace("\n", "")
    all_words = all_words_combined.split(" ")
    all_words = list(map(lambda x: x.replace(" ", ""), all_words))
    all_words = list(filter(lambda x: x != '', all_words))
    return all_words


def find_words_not_in_list(word_dictionary, words_to_compare):
    pass


def main():
    # get all words from web page
    all_words = get_all_words("https://beautiful-soup-4.readthedocs.io/en/latest/#quick-start")
    # count occurrences of each word
    counter = Counter(all_words)
    most_common = counter.most_common(5)
    print(most_common)


if __name__ == '__main__':
    main()
