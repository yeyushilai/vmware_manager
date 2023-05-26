# -*- coding: utf-8 -*-

from constants import (
    ACTION_VMWARE_MANAGER_VM_DESCRIBE_VM,
    ACTION_VMWARE_MANAGER_VM_DETAIL_VM,
    ACTION_VMWARE_MANAGER_VM_MONITOR_VM,
    ACTION_VMWARE_MANAGER_VM_OPERATE_VM,
    ACTION_VMWARE_MANAGER_VM_UPDATE_VM,
    ACTION_VMWARE_MANAGER_VM_DETAIL_VM_TICKET
)
from api.constants import (
    CHANNEL_API,
    CHANNEL_SESSION,
    ROLE_GLOBAL_ADMIN,
    ROLE_ZONE_ADMIN,
    ROLE_CONSOLE_ADMIN,
    ROLE_NORMAL_USER,
    ROLE_PARTNER,
    ROLE_AGENT,
)


API_ACL_VMWARE_MANAGER_VM = {
        ACTION_VMWARE_MANAGER_VM_DESCRIBE_VM: {
            CHANNEL_API: [ROLE_GLOBAL_ADMIN, ROLE_NORMAL_USER,
                          ROLE_CONSOLE_ADMIN, ROLE_ZONE_ADMIN,
                          ROLE_PARTNER, ROLE_AGENT],
            CHANNEL_SESSION: [ROLE_GLOBAL_ADMIN, ROLE_NORMAL_USER,
                              ROLE_CONSOLE_ADMIN, ROLE_ZONE_ADMIN,
                              ROLE_PARTNER, ROLE_AGENT],
        },
        ACTION_VMWARE_MANAGER_VM_DETAIL_VM: {
            CHANNEL_API: [ROLE_GLOBAL_ADMIN, ROLE_NORMAL_USER,
                          ROLE_CONSOLE_ADMIN, ROLE_ZONE_ADMIN,
                          ROLE_PARTNER, ROLE_AGENT],
            CHANNEL_SESSION: [ROLE_GLOBAL_ADMIN, ROLE_NORMAL_USER,
                              ROLE_CONSOLE_ADMIN, ROLE_ZONE_ADMIN,
                              ROLE_PARTNER, ROLE_AGENT],
        },
        ACTION_VMWARE_MANAGER_VM_MONITOR_VM: {
            CHANNEL_API: [ROLE_GLOBAL_ADMIN, ROLE_NORMAL_USER,
                          ROLE_CONSOLE_ADMIN, ROLE_ZONE_ADMIN,
                          ROLE_PARTNER, ROLE_AGENT],
            CHANNEL_SESSION: [ROLE_GLOBAL_ADMIN, ROLE_NORMAL_USER,
                              ROLE_CONSOLE_ADMIN, ROLE_ZONE_ADMIN,
                              ROLE_PARTNER, ROLE_AGENT],
        },
        ACTION_VMWARE_MANAGER_VM_OPERATE_VM: {
            CHANNEL_API: [ROLE_GLOBAL_ADMIN, ROLE_NORMAL_USER,
                          ROLE_CONSOLE_ADMIN, ROLE_ZONE_ADMIN,
                          ROLE_PARTNER, ROLE_AGENT],
            CHANNEL_SESSION: [ROLE_GLOBAL_ADMIN, ROLE_NORMAL_USER,
                              ROLE_CONSOLE_ADMIN, ROLE_ZONE_ADMIN,
                              ROLE_PARTNER, ROLE_AGENT],
        },
        ACTION_VMWARE_MANAGER_VM_UPDATE_VM: {
            CHANNEL_API: [ROLE_GLOBAL_ADMIN, ROLE_NORMAL_USER,
                          ROLE_CONSOLE_ADMIN, ROLE_ZONE_ADMIN,
                          ROLE_PARTNER, ROLE_AGENT],
            CHANNEL_SESSION: [ROLE_GLOBAL_ADMIN, ROLE_NORMAL_USER,
                              ROLE_CONSOLE_ADMIN, ROLE_ZONE_ADMIN,
                              ROLE_PARTNER, ROLE_AGENT],
        },
    ACTION_VMWARE_MANAGER_VM_DETAIL_VM_TICKET: {
        CHANNEL_API: [ROLE_GLOBAL_ADMIN, ROLE_NORMAL_USER,
                      ROLE_CONSOLE_ADMIN, ROLE_ZONE_ADMIN,
                      ROLE_PARTNER, ROLE_AGENT],
        CHANNEL_SESSION: [ROLE_GLOBAL_ADMIN, ROLE_NORMAL_USER,
                          ROLE_CONSOLE_ADMIN, ROLE_ZONE_ADMIN,
                          ROLE_PARTNER, ROLE_AGENT],
    }
}
