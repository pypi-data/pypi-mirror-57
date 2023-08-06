"""
Dumper file used to dump data to CSV or JSON format
"""
import base64
import csv
import json
import os
import shutil
from datetime import datetime
from logger import logger


class Dumper:
    """
    Used to Dump the expenses data into a CSV or JSON file
    """

    def __init__(self, fyle_connection):
        self.__fyle_connection = fyle_connection

    @staticmethod
    def dump_csv(data, path):
        """
        :param data: Takes existing Expenses Data, that match the parameters
        :param path: Takes the path of the file
        :return: CSV file with the list of existing Expenses, that match the parameters
        """

        filename = path + '/{0}--Date--{1}.csv'
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename.format(data[0]['org_name'], datetime.now()), 'w') as export_file:
            keys = data[0].keys()
            dict_writer = csv.DictWriter(export_file, fieldnames=keys, delimiter=',')
            dict_writer.writeheader()
            dict_writer.writerows(data)

    @staticmethod
    def dump_json(data, path):
        """
        :param data: Takes existing Expenses Data, that match the parameters
        :param path: Takes the path of the file
        :return:  JSON file with the list of existing Expenses, that match the parameters
        """

        filename = path + '/{0}--Date--{1}.json'
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename.format(data[0]['org_name'], datetime.now()), 'w') as export_file:
            json.dump(data, export_file, indent=4, sort_keys=True)

    def dump_attachments(self, data, path):
        """
        :param data: Takes existing Expenses Data, that match the parameters
        :param path: Takes the path of the file
        :return:  Expenses Attachments
        """

        fyle_connection = self.__fyle_connection

        expense_ids = [(i.get('id')) for i in data]
        if not expense_ids:
            logger.error('No attachments found.')

        if expense_ids:
            dir_name = path + '/attachments-Date--{}'.format(datetime.now())
            os.mkdir(dir_name)
            logger.info('{} Expense(s) have attachment(s)'.format(len(expense_ids)))
            logger.info('Downloading now')

            for expense_id in expense_ids:
                attachment = fyle_connection.extract_attachments(expense_id)
                attachment_data = attachment['data']
                attachment_content = [item.get('content') for item in attachment_data]

                if attachment['data']:
                    attachment = attachment['data'][0]
                    attachment['expense_id'] = expense_id
                    attachment_names = [item.get('filename') for item in attachment_data]

                    for index, img_data in enumerate(attachment_content):
                        img_data = (attachment_content[index])
                        with open(dir_name + '/' + expense_id + '_' + attachment_names[index], "wb") as fh:
                            logger.info(' Downloading {}_{}'.format(expense_id, attachment_names[index]))
                            fh.write(base64.b64decode(img_data))
                            logger.info('{}_{} Download completed'.format(expense_id, attachment_names[index]))

            shutil.make_archive(dir_name, 'zip', dir_name)
            logger.info('Archive file created at {}'.format(dir_name))
