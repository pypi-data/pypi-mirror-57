"""
Connection file used to establish connection with Fyle APIs
"""
from fylesdk import FyleSDK


class FyleConnector:
    """The main class which creates a connection with Fyle APIs.
        Parameters:
            client_id (str): Client ID for Fyle API.
            client_secret (str): Client secret for Fyle API.
            refresh_token (str): Refresh token for Fyle API.
            base_url (str) : Base URL.
        """

    def __init__(self, client_id, client_secret, base_url, refresh_token):
        self.__base_url = base_url
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__refresh_token = refresh_token

        self.__connection = FyleSDK(
            base_url=self.__base_url,
            client_id=self.__client_id,
            client_secret=self.__client_secret,
            refresh_token=self.__refresh_token
        )

    def extract_expenses(self, state, approved_at, updated_at):
        """
        Get a list of existing Expenses, that match the parameters
        :param updated_at: Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern.
        :param approved_at: Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern.
        :param state: state of the expense [ 'PAID' , 'DRAFT' , 'APPROVED' , 'APPROVER_PENDING' , 'COMPLETE' ]
        :return: List with dicts in Expenses schema.
        """
        expenses = self.__connection.Expenses.get_all(state=state, approved_at=approved_at, updated_at=updated_at)
        return expenses

    def extract_attachments(self, expense_id):
        """
                Get all the file attachments associated with an Expense.
                :param expense_id: Unique ID to find an Expense. Expense Id is our internal Id, it starts with preifx tx always.
                :return: List with dicts in Attachments schema.
                """
        attachment = self.__connection.Expenses.get_attachments(expense_id)
        return attachment
