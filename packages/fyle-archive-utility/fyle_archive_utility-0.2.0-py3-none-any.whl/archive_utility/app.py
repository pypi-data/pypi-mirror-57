"""
Fyle-Archive-Utility
"""
import logging
import os
import json
import click
from archive_utility.dumper import Dumper
from archive_utility.fyle_connection import FyleConnector

logger = logging.getLogger('FyleArchiveUtility')

SUPPORTED_EXTENSIONS = ('csv', 'json')

try:
    path_to_json = os.path.expanduser('~/.config.json')
    with open(path_to_json, 'r') as config_file:
        credentials = json.load(config_file)
        config_file.close()
    CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN, BASE_URL = credentials['client_id'], credentials['client_secret'], \
                                                        credentials['refresh_token'], credentials['base_url']
    # Make connection with FYLE using the above credentials
    fyle_connection = FyleConnector(
        CLIENT_ID, CLIENT_SECRET, BASE_URL, REFRESH_TOKEN)

    dumper = Dumper(fyle_connection)
except:
    click.echo(click.style('Please make connection with FYLE', fg='red', blink=True))


@click.group()
@click.version_option(version='0.01', prog_name='Fyle-Archive-Utility')
def main():
    """  Fyle Archive Utility """

# Using this command to get FYLE credentials and store them in a json file
@main.command()
@click.option('--client_id', prompt='client_id', help='Enter Your CLIENT_ID')
@click.option('--client_secret', prompt='client_secret', help='Enter Your CLIENT_SECRET')
@click.option('--refresh_token', prompt='refresh_token', help='Enter Your REFRESH_TOKEN')
@click.option('--base_url', prompt='base_url', help='Enter Your BASE_URL')
def connect(client_id, client_secret, refresh_token, base_url):
    """
    :param client_id: Client ID for Fyle API.
    :param client_secret: Client secret for Fyle API.
    :param refresh_token: Refresh Token for Fyle API.
    :param base_url: BaseURL.
    """
    cred_file = os.path.expanduser('~/.fyleconfig.json')
    with open(cred_file, 'w') as handler:
        json.dump({'client_id': client_id, 'client_secret': client_secret, 'refresh_token': refresh_token,
                   'base_url': base_url}, handler, sort_keys=True, indent=4)
        handler.close()
        logger.info('Your FYLE credentials are saved.')


@main.command()
@click.option('--file_format', help="Enter the format of the file 'csv' or 'json' ", default='csv')
@click.option('--state', help="Enter the state of Expenses [ 'PAID' , 'APPROVED' ]")
@click.option('--path', help='Enter the directory where you want to save your file', required=True)
@click.option('--approved_at_gte', help='Enter approved date', default=None)
@click.option('--approved_at_lte', help='Enter approved date', default=None)
@click.option('--updated_at_gte', help='Enter updated date', default=None)
@click.option('--updated_at_lte', help='Enter updated date', default=None)
@click.option('--download_attachments', help='If set to True, all attachments will be downloaded', default=None)
def expenses(file_format, state, path, approved_at_gte, approved_at_lte, updated_at_gte, updated_at_lte, download_attachments):
    """
    :param file_format: format of the file to be generated 'CSV' or 'JSON'
    :param state:  state of the Expense [ 'PAID' , 'DRAFT' , 'APPROVED' , 'APPROVER_PENDING' , 'COMPLETE' ]
    :param path:   Takes the path of the file to save the data.
    :param approved_at_gte:  Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format
    :param approved_at_lte:  Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format.
    :param updated_at_gte: Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format.
    :param updated_at_lte: Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format.
    :param download_attachments: (bool) - If set to 'True', all attachments will be downloaded.

    """
    if file_format in SUPPORTED_EXTENSIONS:
        logger.info('Downloading data from Fyle')
        
        approved_at = []
        if approved_at_gte:
            approved_at.append('gte:{0}'.format(approved_at_gte))
        if approved_at_lte:
            approved_at.append('lte:{0}'.format(approved_at_lte))

        updated_at = []
        if updated_at_gte:
            updated_at.append('gte:{0}'.format(updated_at_gte))
        if updated_at_lte:
            updated_at.append('lte:{0}'.format(updated_at_lte))

        response_data = fyle_connection.extract_expenses(state=state, approved_at=approved_at, updated_at=updated_at)
        data = [i for i in response_data if i['has_attachments'] is True]

        if not response_data:
            logger.info('No Expenses found')
        elif file_format == 'csv':
            dumper.dump_csv(response_data, path)
            logger.info('Download Successful !')
        else:
            dumper.dump_json(response_data, path)
            logger.info('Download Successful !')
        if download_attachments == 'True':
            dumper.dump_attachments(data, path)
    else:
        logger.error('%s format not supported', file_format)
