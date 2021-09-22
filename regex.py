
import re


def split_path_list(path):
    """
    split url path at '/' & put into list for router trie
    :param path:
    :return: list of path splits
    """
    pattern = re.compile(r'/\w*')
    matches = pattern.findall(path)
    return matches


def split_path_dict(path):
    """
    split url path at '/' & put into dictionary where key is path part and value is tuple of start & end indices
    :param path:
    :return: dictionary of path matches & index spans
    """
    pattern = re.compile(r'/\w*')
    matches = pattern.finditer(path)
    split_idx_dict = {}
    for m in matches:
        # split_idx_dict[m.group()] = (m.start(), m.end())
        split_idx_dict[m.group()] = m.span()
        print(m.end())
    return split_idx_dict


def search_email(text):
    """
    search text for all phone numbers
    :param text:
    :return: email match
    """
    pattern = re.compile(r'\(?\d{3}.\d{3}.\d{4}')
    matches = pattern.findall(text)
    return matches


def search_phones(text):
    """
    search text for an email address
    :param text:
    :return: email match
    """
    pattern = re.compile(r'[a-zA-Z1-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
    match = pattern.search(text)
    return match.group()


url_path = '/home/about/me'
some_text = 'hi hello here is text ' \
       'this is new line 123 ' \
       'here\'s a phone number: (775)336-8345 ' \
       'hi again eddie-bow@red-co.com ' \
       'and a last line for fun agent_hell@cox.net ' \
       'this is actually 702.334.5556 the last line.'

print(split_path_list(url_path))
print(split_path_dict(url_path))
print(search_phones(some_text))
print(search_email(some_text))
