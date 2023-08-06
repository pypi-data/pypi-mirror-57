# -*- coding: utf-8 -*-
"""Dialpad class file."""

import csv
import json
import time
import requests

from bits.dialpad.reports import Reports


class Dialpad(object):
    """Dialpad class."""

    def __init__(self, token, verbose=False):
        """Initialize a class instance."""
        self.token = token
        self.verbose = verbose

        # set the API base url
        self.base_url = "https://dialpad.com/api/v2"

        # set the headers
        self.headers = {"Authorization": "Bearer {}".format(self.token)}

        # set list of valid number statuses
        self.number_statuses = [
            "available",
            "pending",
            "office",
            "department",
            "call_center",
            "user",
            "room",
            "porting",
            "call_router",
        ]

    #
    # Classes
    #
    def reports(self, auth):
        """Return a Reports instance."""
        return Reports(auth, self)

    #
    # Helpers
    #
    def get_list(self, url, params):
        """Return a list of paginated items."""
        # get first page of results
        response = requests.get(url, headers=self.headers, params=params)

        # get json data
        try:
            data = json.loads(response.text)
        except Exception as e:
            print("ERROR: Failed to parse json response: {}".format(e))
            return

        cursor = data.get("cursor")
        items = data.get("items", [])

        while cursor:
            params["cursor"] = cursor

            # get next page of results
            response = requests.get(url, headers=self.headers, params=params)

            # get json data
            try:
                data = json.loads(response.text)
            except Exception as e:
                print("ERROR: Failed to parse json response: {}".format(e))
                print(response.text)
                return

            cursor = data.get("cursor")
            items.extend(data.get("items", []))

        return items

    #
    # Departments: /api/v2/departments
    #
    def get_all_departments(self):
        """Return a list of all numbers."""
        departments = []
        for office in self.get_offices():
            departments.extend(self.get_office_departments(office["id"]))
        return departments

    def get_department(self, department_id):
        """Return a list of departments."""
        url = "{}/departments/{}".format(self.base_url, department_id)
        return self.get_list(url, params={})

    #
    # Numbers: /api/v2/numbers
    #
    def get_all_numbers(self):
        """Return a list of all numbers."""
        numbers = []
        for status in self.number_statuses:
            numbers.extend(self.get_numbers(status=status))
        return numbers

    def get_numbers(self, status=None):
        """Return a list of numbers."""
        url = "{}/numbers".format(self.base_url)
        params = {
            # 'limit': '40',
            "status": status
        }
        return self.get_list(url, params=params)

    #
    # Offices: /api/v2/offices
    #
    def get_offices(self):
        """Return a list of offices."""
        url = "{}/offices".format(self.base_url)
        return self.get_list(url, params={})

    def get_office_by_id(self, id):
        """Returns details of an office"""
        url = "{}/offices/{}".format(self.base_url, id)
        r = requests.get(url, headers=self.headers)
        return r.json()

    def get_office_departments(self, office_id):
        """Return a list of departments for an office."""
        url = "{}/offices/{}/departments".format(self.base_url, office_id)
        return self.get_list(url, params={})

    #
    # Rooms: /api/v2/rooms
    #
    def create_room(self, body):
        """Create a room in Dialpad."""
        url = "{}/rooms".format(self.base_url)
        response = requests.post(url, headers=self.headers, json=body)
        return response.json()

    def delete_room(self, room_id):
        """Delete a room from Dialpad."""
        url = "{}/rooms/{}".format(self.base_url, room_id)
        r = requests.delete(url, headers=self.headers)
        if r.status_code == 200:
            return True
        else:
            return False

    def assign_room_number(self, room_id, number, area_code=None):
        """Return confirmation json if success or None."""
        url = "{}/rooms/{}/assign_number".format(self.base_url, room_id)
        data = {"area_code": area_code, "number": number}
        r = requests.post(url, headers=self.headers, json=data)
        if r.status_code == 200:
            return r.json()
        else:
            return None

    def get_rooms(self):
        """Return a list of rooms."""
        url = "{}/rooms".format(self.base_url)
        return self.get_list(url, params={})

    #
    # Rooms Desk Phones: /api/v2/rooms/{room_id}/deskphones
    #
    def get_room_desk_phones(self, room_id):
        """Return a list of phones under a room."""
        url = "{}/rooms/{}/deskphones".format(self.base_url, room_id)
        return self.get_list(url, params={})

    def get_rooms_desk_phones(self):
        """Return a dict of desk phones for all rooms."""
        rooms = self.get_rooms()
        desk_phones = {}
        for r in rooms:
            if r["state"] == "deleted":
                continue
            room_id = r["id"]
            phones = self.get_room_desk_phones(room_id)
            if not phones:
                continue
            r["desk_phones"] = phones
            desk_phones[room_id] = r
        return desk_phones

    def set_room_desk_phone(self, user_id, name, mac_address, phone_type="polycom"):
        """Set a room desk phone."""
        url = "{}/rooms/{}/deskphones".format(self.base_url, user_id)
        data = {"type": phone_type, "name": name, "mac_address": mac_address}
        response = requests.post(url, headers=self.headers, json=data)
        if response.status_code == 200:
            return True
        return False

    def set_office_desk_phone(self, user_id, name, mac_address, phone_type="polycom"):
        """Set a room desk phone - alias for set_room_desk_phone."""
        return self.set_room_desk_phone(user_id, name, mac_address, phone_type)

    #
    # Statistics: /api/v2/stats
    #
    def get_stats(self, days_ago_end=30):
        """Return statistics data."""
        # process statistics
        request = self.process_statistics(days_ago_end=days_ago_end)

        # get progress
        request_id = request["request_id"]
        progress = self.get_statistics(request_id)
        while "download_url" not in progress:
            time.sleep(1)
            progress = self.get_statistics(request_id)

        # get data
        url = progress["download_url"]
        return self.get_statistics_data(url)

    def get_statistics(self, request_id):
        """Return a the progress of a stastics request."""
        url = "{}/stats/{}".format(self.base_url, request_id)
        return requests.get(url, headers=self.headers).json()

    def get_statistics_data(self, url):
        """Return a the data of a stats request."""
        return list(
            csv.DictReader(requests.get(url, headers=self.headers).text.splitlines())
        )

    def process_statistics(
        self,
        coaching_group=False,
        days_ago_start=1,
        days_ago_end=30,
        export_type="stats",
        is_today=False,
        office_id=None,
        stat_type="calls",
        target_id=None,
        target_type="user",
        timezone="US/Eastern",
    ):
        """Process statistics in Dialpad."""
        url = "{}/stats".format(self.base_url)
        body = {
            "coaching_group": coaching_group,
            "days_ago_start": days_ago_start,
            "days_ago_end": days_ago_end,
            "export_type": export_type,
            "is_today": is_today,
            "stat_type": stat_type,
            "timezone": timezone,
        }
        if target_id:
            body["target_id"] = target_id
            body["taget_type"] = target_type
        elif office_id:
            body["office_id"] = office_id

        return requests.post(url, headers=self.headers, json=body).json()

    #
    # Users: /api/v2/users
    #
    def assign_user_number(self, user_id, area_code=None, number=None):
        """Assign a number to a user."""
        url = "{}/users/{}/assign_number".format(self.base_url, user_id)
        body = {"area_code": area_code, "number": number}
        response = requests.post(url, headers=self.headers, json=body)
        return response.json()

    def create_user(self, body):
        """Create a user in Dialpad."""
        url = "{}/users".format(self.base_url)
        response = requests.post(url, headers=self.headers, json=body)
        return response.json()

    def delete_user(self, user_id):
        """Delete a Dialpad user."""
        url = "{}/users/{}".format(self.base_url, user_id)
        response = requests.delete(url, headers=self.headers)
        return response.json()

    def get_user(self, user_id):
        """Return a user from dialpad."""
        url = "{}/users/{}".format(self.base_url, user_id)
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_users(self, email=None, state=None, limit=1000, cursor=None):
        """Return a list of users."""
        params = {"email": email, "state": state, "limit": limit, "cursor": cursor}
        url = "{}/users".format(self.base_url)

        # get first page of results
        response = requests.get(url, headers=self.headers, params=params)

        # raise for status
        response.raise_for_status()

        # get json data
        # try:
        #     data = json.loads(response.text)
        # except Exception as e:
        #     print("ERROR: Failed to parse json response: {}".format(e))
        #     return

        data = response.json()
        cursor = data.get("cursor")
        items = data.get("items", [])

        while cursor:
            # set the next page cursor
            params["cursor"] = cursor

            # get next page of results
            response = requests.get(url, headers=self.headers, params=params)

            # get json data
            # try:
            #     data = json.loads(response.text)
            # except Exception as e:
            #     print("ERROR: Failed to parse json response: {}".format(e))
            #     return

            # raise for status
            response.raise_for_status()

            data = response.json()
            cursor = data.get("cursor")
            items.extend(data.get("items", []))

        return items

    def patch_user(self, user_id, body):
        """Patch a Dialpad user."""
        url = "{}/users/{}".format(self.base_url, user_id)
        return requests.patch(url, headers=self.headers, json=body)

    #
    # Users Desk Phones: /api/v2/users/{user_id}/deskphones
    #
    def get_user_desk_phones(self, user_id):
        """Return a list of phones under a user."""
        url = "{}/users/{}/deskphones".format(self.base_url, user_id)
        return self.get_list(url, params={})

    def get_users_desk_phones(self):
        """Return a dict of desk phones for all users."""
        users = self.get_users()
        desk_phones = {}
        for u in users:
            if u["state"] == "deleted":
                continue
            user_id = u["id"]
            phones = self.get_user_desk_phones(user_id)
            if not phones:
                continue
            u["desk_phones"] = phones
            desk_phones[user_id] = u
        return desk_phones

    def set_user_desk_phone(self, user_id, name, mac_address, phone_type="polycom"):
        """Set a user desk phone."""
        url = "{}/users/{}/deskphones".format(self.base_url, user_id)
        params = {"type": phone_type, "name": name, "mac_address": mac_address}

        r = requests.post(url, headers=self.headers, params=params)

        if r.status_code == 200:
            return True
        return False
