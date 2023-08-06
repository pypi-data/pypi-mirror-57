"""API Wrapper for Eloqua Contacts"""

from collections import namedtuple

ContactFields = namedtuple("ContactFields", ["first_name", "last_name", "email_address"])


class Contact:
    """Abstracts API operations for Eloqua contacts"""
    def __init__(self, session,
                 contact_fields=None,
                 contact_id=None):
        self.session = session
        self.contact_fields = ContactFields(*contact_fields)
        self.contact_id = contact_id

    def make_json_body(self):
        """
        Maps dictionary values to the field names that the Eloqua API expects.
        The request body defines the details of the contact to be created.
        emailAddress is the only required field.
        """
        return {
            "firstName": self.contact_fields.first_name,
            "lastName": self.contact_fields.last_name,
            "emailAddress": self.contact_fields.email_address
        }

    def sync_id_from_eloqua(self, response):
        """
        Updates the contact_id value based on a response from the Eloqua API.
        :param response: HTTP response from Eloqua API
        :type response: requests.Response
        """
        self.contact_id = response.json()["id"]

    def create(self):
        """
        Creates a contact that matches the criteria specified by the request body.
        If the contact was created successfully, proceeds to update the contact_id value in the
        Contact object based on the response from the Eloqua API.
        """
        response = self.session.post(url="/api/REST/1.0/data/contact", json=self.make_json_body())
        response.raise_for_status()
        self.sync_id_from_eloqua(response)

    def delete(self):
        """Deletes a contact specified by the id parameter."""
        response = self.session.delete(url=f"/api/REST/1.0/data/contact/{self.contact_id}")
        response.raise_for_status()
