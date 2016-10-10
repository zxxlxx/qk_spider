# -*- coding: utf-8 -*-

class Permission:
    GUEST = 0x00
    EDIT = 0x01
    ADMINISTRATOR = 0xFF
    PERMISSION_MAP = {
        GUEST: ('guest', 'guest'),
        EDIT: ('edit', 'edit'),
        ADMINISTRATOR: ('administrator', 'administrator')
    }