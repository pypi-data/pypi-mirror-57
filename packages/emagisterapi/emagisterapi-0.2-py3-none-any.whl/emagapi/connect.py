import requests
from urllib.parse import urlencode
from http import HTTPStatus
import json


class Api:
    DOMAINS = {'es': 'www.emagister.com',
               'uk': 'www.emagister.co.uk',
               'fr': 'www.emagister.fr'}

    BASE_API_URL = 'https://{}/api/'
    MAX_NUM_OF_CONSECUTIVE_ERRORS = 5

    def __init__(self, country='es', version='1.0', encoding='utf-8', page_size=25, silent=False):
        self.country = country
        self.version = version
        self.encoding = encoding
        self.page_size = page_size
        self.records = []
        self.silent = silent
        self.errors = 0


    def __record_data__(self, record, subset=None):
        if not subset:
            return record
            
        data = {}

        if isinstance(subset, list):
            for key in subset:
                data[key] = record[key]

            return data
        
        if isinstance(subset, dict):
            for key, value in subset.items():
                data[key] = record[value]

            return data

        raise Exception('subset must be of type Dictionary or List')

    def __build_url__(self, resource, filters=None, page=1):
        base_api_url = self.BASE_API_URL.format(self.DOMAINS[self.country])

        parameters = 'page={}&size={}'.format(page, self.page_size)

        if filters:
            parameters = '{}&{}'.format(parameters, urlencode(filters))
        
        return '{}{}/{}?{}'.format(base_api_url, self.version, resource, parameters)
    

    def __read__(self, url):
        response = requests.get(url)

        if response.status_code == HTTPStatus.OK:
            if not self.silent:
                print('GET: {} [{}]'.format(url, response.status_code))

            self.errors = 0

            return json.loads(response.content.decode(self.encoding))
        
        if not self.silent:
            print('GET: {} [{}]'.format(url, response.status_code))
        
        self.errors += 1
        if self.errors == self.MAX_NUM_OF_CONSECUTIVE_ERRORS:
            raise Exception('Maximum number of consecutive errors reached')

    def __add_record__(self, record):
        self.records.append(record)

    def __get_records__(self):
        records = self.records
        self.records = []

        return records


class Courses(Api):
    def get(self, subset=None, filters=None, max_records=None, url=None):
        ''' Get courses collection from API
        Parameters: 
        subset (list|dict): Subset of fields to retrieve. If None, all fields will be retrieved.
        filters (dict): Dictionary of filtres to apply. See https://www.emagister.com/api/doc#get--api-{version}-courses
        max_records (int): Maximum number of records to retrieve. If None, all records will be retrieved.
        url (str): Api endpoint
    
        Returns: 
        list: A list of dictionaries representing records
        '''
        if not url:
            url = self.__build_url__('courses', filters=filters)

        courses = self.__read__(url)
        total_records = max_records if max_records else courses['total_count']

        next_url = courses['_links']['next']['href']
        
        for course in courses['courses']:
            course_data = self.__record_data__(course, subset)

            self.__add_record__(course_data)
            
            if max_records and len(self.records) >= max_records:
                return self.__get_records__()

        if not self.silent:
            print('Records: {}/{}'.format(len(self.records), total_records))

        if next_url:
            return self.get(subset, max_records=max_records, url=next_url)

        return self.__get_records__()
