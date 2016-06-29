"""This module contains the general information for StorageLocalDisk ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class StorageLocalDiskConsts:
    ADMIN_ACTION_DISABLE_SED_FOREIGN_DRIVES = "disable-sed-foreign-drives"
    ADMIN_ACTION_DISABLE_SELF_ENCRYPT = "disable-self-encrypt"
    ADMIN_ACTION_ENABLE_SELF_ENCRYPT = "enable-self-encrypt"
    ADMIN_ACTION_LOCATOR_LED_OFF = "locator-led-off"
    ADMIN_ACTION_LOCATOR_LED_ON = "locator-led-on"
    ADMIN_ACTION_MAKE_DEDICATED_HOT_SPARE = "make-dedicated-hot-spare"
    ADMIN_ACTION_MAKE_GLOBAL_HOT_SPARE = "make-global-hot-spare"
    ADMIN_ACTION_MAKE_JBOD = "make-jbod"
    ADMIN_ACTION_MAKE_UNCONFIGURED_GOOD = "make-unconfigured-good"
    ADMIN_ACTION_PREPARE_FOR_REMOVAL = "prepare-for-removal"
    ADMIN_ACTION_REMOVE_HOT_SPARE = "remove-hot-spare"
    ADMIN_ACTION_SET_BOOT_DRIVE = "set-boot-drive"
    ADMIN_ACTION_UNDO_PREPARE_FOR_REMOVAL = "undo-prepare-for-removal"
    DEDICATED_HOT_SPARE_FOR_VDID_ = ""
    LOCATOR_LEDSTATUS_OFF = "off"
    LOCATOR_LEDSTATUS_ON = "on"


class StorageLocalDisk(ManagedObject):
    """This is StorageLocalDisk class."""

    consts = StorageLocalDiskConsts()
    naming_props = set([u'id'])

    mo_meta = MoMeta("StorageLocalDisk", "storageLocalDisk", "pd-[id]", VersionMeta.Version151f, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], [u'storageController'], [u'faultInst', u'storageLocalDiskProps', u'storageOperation'], ["Get", "Set"])

    prop_meta = {
        "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["disable-sed-foreign-drives", "disable-self-encrypt", "enable-self-encrypt", "locator-led-off", "locator-led-on", "make-dedicated-hot-spare", "make-global-hot-spare", "make-jbod", "make-unconfigured-good", "prepare-for-removal", "remove-hot-spare", "set-boot-drive", "undo-prepare-for-removal"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "coerced_size": MoPropertyMeta("coerced_size", "coercedSize", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "dedicated_hot_spare_for_vd_id": MoPropertyMeta("dedicated_hot_spare_for_vd_id", "dedicatedHotSpareForVDId", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [""], ["0-4294967295"]), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []), 
        "drive_firmware": MoPropertyMeta("drive_firmware", "driveFirmware", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "drive_serial_number": MoPropertyMeta("drive_serial_number", "driveSerialNumber", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "drive_state": MoPropertyMeta("drive_state", "driveState", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "fde_capable": MoPropertyMeta("fde_capable", "fdeCapable", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []), 
        "fde_enabled": MoPropertyMeta("fde_enabled", "fdeEnabled", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []), 
        "foreign_locked": MoPropertyMeta("foreign_locked", "foreignLocked", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []), 
        "health": MoPropertyMeta("health", "health", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version151f, MoPropertyMeta.NAMING, 0x10, 0, 510, None, [], ["0-256"]), 
        "interface_type": MoPropertyMeta("interface_type", "interfaceType", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "link_speed": MoPropertyMeta("link_speed", "linkSpeed", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "locator_led_status": MoPropertyMeta("locator_led_status", "locatorLEDStatus", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["off", "on"], []), 
        "locked": MoPropertyMeta("locked", "locked", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []), 
        "media_type": MoPropertyMeta("media_type", "mediaType", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "online": MoPropertyMeta("online", "online", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "pd_status": MoPropertyMeta("pd_status", "pdStatus", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "predictive_failure_count": MoPropertyMeta("predictive_failure_count", "predictiveFailureCount", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "product_id": MoPropertyMeta("product_id", "productId", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, 0, 255, None, [], []), 
        "secured": MoPropertyMeta("secured", "secured", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "adminAction": "admin_action", 
        "childAction": "child_action", 
        "coercedSize": "coerced_size", 
        "dedicatedHotSpareForVDId": "dedicated_hot_spare_for_vd_id", 
        "dn": "dn", 
        "driveFirmware": "drive_firmware", 
        "driveSerialNumber": "drive_serial_number", 
        "driveState": "drive_state", 
        "fdeCapable": "fde_capable", 
        "fdeEnabled": "fde_enabled", 
        "foreignLocked": "foreign_locked", 
        "health": "health", 
        "id": "id", 
        "interfaceType": "interface_type", 
        "linkSpeed": "link_speed", 
        "locatorLEDStatus": "locator_led_status", 
        "locked": "locked", 
        "mediaType": "media_type", 
        "online": "online", 
        "pdStatus": "pd_status", 
        "predictiveFailureCount": "predictive_failure_count", 
        "productId": "product_id", 
        "rn": "rn", 
        "secured": "secured", 
        "status": "status", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.admin_action = None
        self.child_action = None
        self.coerced_size = None
        self.dedicated_hot_spare_for_vd_id = None
        self.drive_firmware = None
        self.drive_serial_number = None
        self.drive_state = None
        self.fde_capable = None
        self.fde_enabled = None
        self.foreign_locked = None
        self.health = None
        self.interface_type = None
        self.link_speed = None
        self.locator_led_status = None
        self.locked = None
        self.media_type = None
        self.online = None
        self.pd_status = None
        self.predictive_failure_count = None
        self.product_id = None
        self.secured = None
        self.status = None
        self.vendor = None

        ManagedObject.__init__(self, "StorageLocalDisk", parent_mo_or_dn, **kwargs)

