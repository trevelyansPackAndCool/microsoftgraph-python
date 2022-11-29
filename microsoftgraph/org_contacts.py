from microsoftgraph.decorators import token_required
from microsoftgraph.response import Response


class OrgContacts(object):
    def __init__(self, client) -> None:
        """Working with organizational contacts in Microsoft Graph.

        https://learn.microsoft.com/en-us/graph/api/resources/orgcontact?view=graph-rest-1.0

        Args:
            client (Client): Library Client.
        """
        self._client = client

    @token_required
    def get_all_org_contacts(self, params: dict = None) -> Response:
        """Retrieve a list of all organizational contacts

        Users
        https://learn.microsoft.com/en-us/graph/api/user-list?view=graph-rest-1.0&tabs=http

        Args:
            params (dict, optional): Query. Defaults to None.

        Returns:
            Response: Microsoft Graph Response.
        """
        return self._client._get(self._client.base_url + "/contacts", params=params, advanced_filtering=True)
