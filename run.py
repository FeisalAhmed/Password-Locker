#!/usr/bin/env python3.6

import random
from user import User
from credential import Credentials

# Functions to add credentials


def create_new_credential(account_name, account_password):
    """Function to create a new account and its credentials"""
    new_credential = Credentials(account_name, account_password)
    return new_credential


def save_new_credential(credentials):
    """Function to save the newly created account and password"""
    credentials.save_credentials()

