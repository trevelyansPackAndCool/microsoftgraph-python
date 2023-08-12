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
        return self._client._get(f'{self.base_url}drives/', params=params)

    @token_required
    def get_drive_items(self, drive_id: str, params: dict = None) -> Response:
        return self._client._get(f'{self.base_url}drives/{drive_id}/items/root/children', params=params)

    @token_required
    def get_item_children(self, item_id: str, params: dict = None) -> Response:
        return self._client._get(f'{self.base_url}drive/items/{item_id}/children', params=params)

    @token_required
    def get_item_contents(self, item_id: str, params: dict = None) -> Response:
        return self._client._get(f'{self.base_url}drive/items/{item_id}/content', params=params)
