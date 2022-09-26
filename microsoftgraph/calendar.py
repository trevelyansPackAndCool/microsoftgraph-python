from datetime import datetime

from microsoftgraph.decorators import token_required
from microsoftgraph.response import Response
from microsoftgraph.utils import format_time


class Calendar(object):
    def __init__(self, client) -> None:
        """Working with Outlook Calendar.

        https://docs.microsoft.com/en-us/graph/api/resources/calendar?view=graph-rest-1.0

        Args:
            client (Client): Library Client.
        """
        self._client = client

    @token_required
    def list_events(self, calendar_id: str = None, params: dict = None) -> Response:
        """Get a list of event objects in the user's mailbox. The list contains single instance meetings and series
        masters.

        https://docs.microsoft.com/en-us/graph/api/user-list-events?view=graph-rest-1.0&tabs=http

        Args:
            calendar_id (str): Calendar ID.
            params (dict, optional): Query. Defaults to None.

        Returns:
            Response: Microsoft Graph Response.
        """
        url = "me/calendars/{}/events".format(calendar_id) if calendar_id else "me/events"
        return self._client._get(self._client.base_url + url, params=params)

    @token_required
    def get_event(self, event_id: str, params: dict = None) -> Response:
        """Get the properties and relationships of the specified event object.

        https://docs.microsoft.com/en-us/graph/api/event-get?view=graph-rest-1.0&tabs=http

        Args:
            event_id (str): Event ID.
            params (dict, optional): Query. Defaults to None.

        Returns:
            Response: Microsoft Graph Response.
        """
        return self._client._get(self._client.base_url + "me/events/{}".format(event_id), params=params)

    @token_required
    def create_event(
        self,
        subject: str,
        content: str,
        start_datetime: datetime,
        start_timezone: str,
        end_datetime: datetime,
        end_timezone: str,
        location: str,
        calendar_id: str = None,
        content_type: str = "HTML",
        attendees: list = None,
        is_online_meeting: bool = False,
        online_meeting_provider: str = 'teamsForBusiness',
        **kwargs,
    ) -> Response:
        """Create an event in the user's default calendar or specified calendar.

        https://docs.microsoft.com/en-us/graph/api/user-post-events?view=graph-rest-1.0&tabs=http

        Additional time zones: https://docs.microsoft.com/en-us/graph/api/resources/datetimetimezone?view=graph-rest-1.0

        Args:
            subject (str): The text of the event's subject line.
            content (str): The body of the message associated with the event.
            start_datetime (datetime): A single point of time in a combined date and time representation ({date}T{time};
            start_timezone (str): Represents a time zone, for example, "Pacific Standard Time".
            end_datetime (datetime): A single point of time in a combined date and time representation ({date}T{time}; for
            end_timezone (str): Represents a time zone, for example, "Pacific Standard Time".
            location (str): The location of the event.
            calendar_id (str, optional): Calendar ID. Defaults to None.
            content_type (str, optional): It can be in HTML or text format. Defaults to HTML.
            attendees (object, optional): list of dicts of the form:
                        [{'email': 'email@example.com', 'name': 'John Doe', 'type': 'required'},...]

        Returns:
            Response: Microsoft Graph Response.
        """
        body = self.build_event_request(
            subject,
            content,
            start_datetime,
            start_timezone,
            end_datetime,
            end_timezone,
            location,
            content_type,
            attendees,
            is_online_meeting,
            online_meeting_provider,
            **kwargs
        )
        url = f"/users/{self.account_id}/calendars/{calendar_id}/events" if calendar_id is not None \
            else f"/users/{self.account_id}/calendar/events"
        return self._client._post(self._client.base_url + url, json=body)

    @token_required
    def update_event(
        self,
        event_id: str,
        subject: str,
        content: str,
        start_datetime: datetime,
        start_timezone: str,
        end_datetime: datetime,
        end_timezone: str,
        location: str,
        calendar_id: str = None,
        content_type: str = "HTML",
        attendees: list = None,
        is_online_meeting: bool = False,
        online_meeting_provider: str = 'teamsForBusiness',
        **kwargs,
    ) -> Response:
        """Create an event in the user's default calendar or specified calendar.

        https://docs.microsoft.com/en-us/graph/api/user-post-events?view=graph-rest-1.0&tabs=http

        Additional time zones: https://docs.microsoft.com/en-us/graph/api/resources/datetimetimezone?view=graph-rest-1.0

        Args:
            event_id (str): id of the calendar event
            subject (str): The text of the event's subject line.
            content (str): The body of the message associated with the event.
            start_datetime (datetime): A single point of time in a combined date and time representation ({date}T{time};
            start_timezone (str): Represents a time zone, for example, "Pacific Standard Time".
            end_datetime (datetime): A single point of time in a combined date and time representation ({date}T{time}; for
            end_timezone (str): Represents a time zone, for example, "Pacific Standard Time".
            location (str): The location of the event.
            calendar_id (str, optional): Calendar ID. Defaults to None.
            content_type (str, optional): It can be in HTML or text format. Defaults to HTML.
            attendees (object, optional): list of dicts of the form:
                        [{'email': 'email@example.com', 'name': 'John Doe', 'type': 'required'},...]

        Returns:
            Response: Microsoft Graph Response.
        """
        body = self.build_event_request(
            subject,
            content,
            start_datetime,
            start_timezone,
            end_datetime,
            end_timezone,
            location,
            content_type,
            attendees,
            is_online_meeting,
            online_meeting_provider,
            **kwargs
        )
        url = f"/users/{self.account_id}/calendars/{calendar_id}/events/{event_id}" if calendar_id is not None \
            else f"/users/{self.account_id}/calendar/events/{event_id}"
        return self._client._patch(self._client.base_url + url, json=body)

    @token_required
    def build_event_request(
        self,
        subject: str,
        content: str,
        start_datetime: datetime,
        start_timezone: str,
        end_datetime: datetime,
        end_timezone: str,
        location: str,
        content_type: str = "HTML",
        attendees: list = None,
        is_online_meeting: bool = False,
        online_meeting_provider: str = 'teamsForBusiness',
        **kwargs,
    ) -> Response:
        """Create an event in the user's default calendar or specified calendar.

        https://docs.microsoft.com/en-us/graph/api/user-post-events?view=graph-rest-1.0&tabs=http

        Additional time zones: https://docs.microsoft.com/en-us/graph/api/resources/datetimetimezone?view=graph-rest-1.0

        Args:
            subject (str): The text of the event's subject line.
            content (str): The body of the message associated with the event.
            start_datetime (datetime): A single point of time in a combined date and time representation ({date}T{time};
            start_timezone (str): Represents a time zone, for example, "Pacific Standard Time".
            end_datetime (datetime): A single point of time in a combined date and time representation ({date}T{time}; for
            end_timezone (str): Represents a time zone, for example, "Pacific Standard Time".
            location (str): The location of the event.
            calendar_id (str, optional): Calendar ID. Defaults to None.
            content_type (str, optional): It can be in HTML or text format. Defaults to HTML.
            attendees (object, optional): list of dicts of the form:
                        [{'email': 'email@example.com', 'name': 'John Doe', 'type': 'required'},...]

        Returns:
            Response: Microsoft Graph Response.
        """
        if isinstance(start_datetime, datetime):
            start_datetime = format_time(start_datetime, is_webhook=True)
        if isinstance(end_datetime, datetime):
            end_datetime = format_time(end_datetime, is_webhook=True)

        attendees_list = [{
            "emailAddress": {
                "address": a["email"],
                "name": a["name"]
            },
            "type": a["type"]
        } for a in attendees]

        body = {
            "subject": subject,
            "body": {
                "contentType": content_type,
                "content": content,
            },
            "start": {
                "dateTime": start_datetime,
                "timeZone": start_timezone,
            },
            "end": {
                "dateTime": end_datetime,
                "timeZone": end_timezone,
            },
            "location": {"displayName": location},
            "isOnlineMeeting": is_online_meeting,
        }

        if is_online_meeting:
            body["onlineMeetingProvider"] = online_meeting_provider

        if attendees:
            body["attendees"] = attendees_list

        body.update(kwargs)
        return body

    @token_required
    def delete_event(self, event_id: str, calendar_id: str=None):
        """
            Delete an existing calendar event.
            Args:
                event_id (str): The id of the calendar event
                calendar_id (str, optional): The id of calendar the event is scheduled on
            Returns:
                Response: Microsoft Graph Response.
            """
        url = f"/users/{self.account_id}/calendars/{calendar_id}/events/{event_id}" if calendar_id is not None \
            else f"/users/{self.account_id}/calendar/events/{event_id}"
        return self._client._delete(self._client.base_url + url)

    @token_required
    def list_calendars(self, params: dict = None) -> Response:
        """Get all the user's calendars (/calendars navigation property), get the calendars from the default calendar
        group or from a specific calendar group.

        https://docs.microsoft.com/en-us/graph/api/user-list-calendars?view=graph-rest-1.0&tabs=http

        Args:
            params (dict, optional): Query. Defaults to None.

        Returns:
            Response: Microsoft Graph Response.
        """
        return self._client._get(self._client.base_url + "me/calendars", params=params)

    @token_required
    def create_calendar(self, name: str) -> Response:
        """Create a new calendar for a user.

        https://docs.microsoft.com/en-us/graph/api/user-post-calendars?view=graph-rest-1.0&tabs=http

        Args:
            name (str): The calendar name.

        Returns:
            Response: Microsoft Graph Response.
        """
        body = {"name": "{}".format(name)}
        return self._client._post(self._client.base_url + "me/calendars", json=body)
