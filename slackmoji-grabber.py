import sys
from bs4 import BeautifulSoup
import requests
import os


def show_arg():

    req = requests.get(sys.argv[1])
    soup_response = BeautifulSoup(req.text, 'html.parser')
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dest_dir = os.path.join(script_dir, 'slackmojis')

    try:
        os.makedirs(dest_dir)

    except OSError:
        pass  # already exists

    for img in soup_response.find_all('img'):
        src_attr = img.get('src')

        if src_attr.find('/'):
            filename = src_attr.rsplit('/', 1)[1].split('?', 1)[0]

        with open(os.path.join(dest_dir, filename), 'wb') as file:
            print("Downloading %s" % filename)
            response = requests.get(src_attr, stream=True)
            file_size = response.headers.get('content-length')

            if file_size is None:  # no content length header
                file.write(response.content)
            else:
                dl = 0
                file_size = int(file_size)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    file.write(data)
                    done = int(50 * dl / file_size)
                    sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50 - done)))
                    sys.stdout.flush()


show_arg()
