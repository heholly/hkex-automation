# File Name: Helper
# Author: Karthick Dhakshinamoorthy
# Python Version: 3.5.4

import random
import re
import datetime


def select_random_participant_id():
    participants = ['1', '2']
    secure_random = random.SystemRandom()
    p_id = secure_random.choice(participants)
    return p_id


def get_current_date():
    today = datetime.datetime.today().strftime('%bX%d,%Y').replace('X0', 'X').replace('X', '')
    return today


def trim_white_space(value):
    trim_space = re.sub(' ', '', value)
    return trim_space
