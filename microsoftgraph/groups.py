from datetime import datetime

from microsoftgraph.decorators import token_required
from microsoftgraph.response import Response
from microsoftgraph.utils import format_time


class Groups(object):
    def __init__(self, client) -> None:
        """Working with Microsoft 365 Groups.

        https://learn.microsoft.com/en-us/graph/api/resources/group?view=graph-rest-1.0

        Args:
            client (Client): Library Client.
        """
        self._client = client

    @token_required
    def list_groups(self, params: dict = None) -> Response:
        """Get a list of groups. The list contains a collection of group objects in the response body. The response
        includes only the default properties of each group.

        https://learn.microsoft.com/en-us/graph/api/group-list?view=graph-rest-1.0&tabs=http

        Args:
            params (dict, optional): Query. Defaults to None.

        Returns:
            Response: Microsoft Graph Response.
        """
        headers = {'ConsistencyLevel': 'eventual'}  # Enable advanced filtering
        return self._client._get(self._client.base_url + "groups", params=params, headers=headers)

    @token_required
    def list_group_members(self, group_id: str, params: dict = None) -> Response:
        """Get a list of members in a group. The list contains a collection of directoryObject objects in the response
        body.

        Pagination is handled by the Client class.

        https://learn.microsoft.com/en-us/graph/api/group-list-members?view=graph-rest-1.0&tabs=http

        https://learn.microsoft.com/en-us/graph/api/resources/directoryobject?view=graph-rest-1.0

        Args:
            group_id (str): Group ID.
            params (dict, optional): Query. Defaults to None.

        Returns:
            Response: Microsoft Graph Response.
        """
        return self._client._get(self._client.base_url + "groups/{}/members".format(group_id), params=params)
