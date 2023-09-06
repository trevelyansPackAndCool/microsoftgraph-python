from microsoftgraph.decorators import token_required
from microsoftgraph.response import Response


class SharePoint(object):
    _site = None
    
    def __init__(self, client) -> None:
        """Working with SharePoint in Microsoft Graph.

        https://learn.microsoft.com/en-us/graph/api/resources/site?view=graph-rest-1.0
        https://learn.microsoft.com/en-us/graph/api/resources/driveitem?view=graph-rest-1.0

        Args:
            client (Client): Library Client.
        """
        self._client = client
        
    def set_site(self, site: str) -> None:
        self._site = site
        
    @property
    def base_url(self) -> str:
        assert self._site, 'SharePoint site url is required. Call set_site() first.'
        return f'{self._client.base_url}sites/{self._site}/'

    @token_required
    def get_drives(self, params: dict = None) -> Response:
        """
        Lists all Drives available in the SharePoint site.

        https://learn.microsoft.com/en-us/graph/api/drive-list?view=graph-rest-1.0&tabs=http#list-a-sites-drives
        """
        return self._client._get(f'{self.base_url}drives/', params=params)

    @token_required
    def get_lists(self, params: dict = None) -> Response:
        """
        Gets all lists in the site. Returns a collection of list resources.

        https://learn.microsoft.com/en-us/graph/api/list-list?view=graph-rest-1.0&tabs=http
        """
        return self._client._get(f'{self.base_url}lists', params=params)

    @token_required
    def get_drive_items(self, drive_id: str, item_id: str = None, params: dict = None) -> Response:
        """
        Lists all items in the Drive. Returns a collection of driveItems resources.
        If item_id is provided, lists all items in the folder. Otherwise lists all items in the root folder.

        https://learn.microsoft.com/en-us/graph/api/driveitem-list-children?view=graph-rest-1.0&tabs=http
        """
        return self._client._get(f'{self.base_url}drives/{drive_id}/items/{item_id or "root"}/children', params=params)

    @token_required
    def get_list_items(self, list_id: str, params: dict = None) -> Response:
        """
        Gets all items in the list. Returns a collection of listItem resources.

        https://learn.microsoft.com/en-us/graph/api/listitem-list?view=graph-rest-1.0&tabs=http
        """
        return self._client._get(f'{self.base_url}lists/{list_id}/items/', params=params)

    @token_required
    def get_item_contents(self, drive_id: str, item_id: str, params: dict = None) -> Response:
        """
        Downloads the contents of the specified driveItem. Only driveItems with the file property can be downloaded.

        https://learn.microsoft.com/en-us/graph/api/driveitem-get-content?view=graph-rest-1.0&tabs=http
        """
        return self._client._get(f'{self.base_url}drives/{drive_id}/items/{item_id}/content', params=params)
