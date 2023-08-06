import requests
from remediation.utils import Singleton
from typing import List
from random import randint


class CM11Generator(Singleton):
    """
    Generates CM11 mock data
    """

    words = []

    def __init__(self, n_tuples=10):
        Singleton.__init__(self)
        # populate random words db
        # load only the first time a new object is created from the singleton
        if not self.words:
            self.words = self.__load_words()
            # create a generator providing lower case words already converted
            # to string
            self.generate_word = \
                (str(x.decode('utf-8')).lower() for x in self.words)
        self.n_tuples = n_tuples
#        print(self.words[0:10])

    def __str__(self):
        return f'{self.name}'

    def get_generated_data_as_list_of_dict(self):
        data = self.get_generated_data()
        th = ['aa_code', 'ak_code', 'url']
        return [dict(zip(th, t)) for t in data]

    def get_generated_data(self):
        """
        :param num_tuples: number of tuples to generate
        :return: a generator of tuples with (AA, AK, url)
        """

        def make_url():
            base = '/'.join([next(self.generate_word) for k in range(2)])
            return f'https://{base}.git'

        # fill out as separate lists
        _aa = []
        _ak = []
        _url = []
        # _type = []

        # merge all together in a list of tuples (via list(zip(..)) ) )
        for i in range(self.n_tuples):
            _aa.append(f'AA{randint(10000, 99999)}')
            _ak.append(f'AK{randint(10000, 99999)}')
            _url.append(f'{make_url()}')

        return zip(_aa, _ak, _url)

        # [dict(zip(th, t)) for t in c.get_generated_data()]
        # --> per convertire in formato db per insert

    def __load_words(self) -> List:
        """
        :return: a list of words in binary code
        """
        word_site = \
            "http://svnweb.freebsd.org/csrg/share/dict/\
                words?view=co&content-type=text/plain"
        response = requests.get(word_site)
        return response.content.splitlines()
