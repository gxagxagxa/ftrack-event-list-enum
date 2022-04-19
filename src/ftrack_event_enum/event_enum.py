from base import NestEnumBase


class FtrackEventActionEnum(NestEnumBase):
    __event_name__ = 'action'
    DISCOVER = 'discover'
    LAUNCH = 'launch'
    TRIGGER_USER_INTERFACE = 'trigger-user-interface'


class FtrackEventLocationEnum(NestEnumBase):
    __event_name__ = 'location'
    COMPONENT_ADDED = 'component-added'
    COMPONENT_REMOVED = 'component-removed'


class FtrackEventConnectEnum(NestEnumBase):
    __event_name__ = 'connect'


class FtrackEventDynamicEnumeratorEnum(NestEnumBase):
    __event_name__ = 'dynamic-enumerator'


class FtrackEventUpdateEnum(NestEnumBase):
    __event_name__ = 'update'


class FtrackEventAPISessionEnum(NestEnumBase):
    __event_name__ = 'session'
    GET_FILE_TYPE_FROM_STRING = 'get-file-type-from-string'
    CONSTRUCT_ENTITY_TYPE = 'construct-entity-type'
    CONFIGURE_LOCATION = 'configure-location'
    COMPONENT_ADDED = 'component-added'
    COMPONENT_REMOVED = 'component-removed'
    READY = 'ready'
    RESET = 'reset'


class FtrackEventAPIEnum(NestEnumBase):
    __event_name__ = 'api'
    SESSION = FtrackEventAPISessionEnum()


class FtrackEventEnum(NestEnumBase):
    __event_name__ = 'ftrack'
    ACTION = FtrackEventActionEnum()
    CONNECT = FtrackEventConnectEnum()
    DYNAMIC_ENUMERATOR = FtrackEventDynamicEnumeratorEnum()
    LOCATION = FtrackEventLocationEnum()
    UPDATE = FtrackEventUpdateEnum()
    API = FtrackEventAPIEnum()
