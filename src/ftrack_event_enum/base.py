from typing import Any, Optional


class NestEnumBase(object):
    __event_name__: Optional[str] = None
    __event_list__: list = []
    __strict_enum__: bool = False

    def __getitem__(self, item):
        return getattr(self, item)

    def __getattribute__(self, name: str) -> Any:
        event_list = object.__getattribute__(self, '__event_list__')
        if not event_list:
            event_list.append(self)

        if name == 'value':
            return object.__getattribute__(self, 'value')

        last_event = event_list[-1]
        if isinstance(last_event, NestEnumBase):
            try:
                event_list.append(object.__getattribute__(last_event, name))
            except AttributeError as e:
                if object.__getattribute__(last_event, '__strict_enum__'):
                    raise e
                event_list.append(name)

        else:
            event_list.append(name)

        return self

    @property
    def value(self) -> str:

        def resovlve_event_topic(event):
            if isinstance(event, NestEnumBase):
                return object.__getattribute__(event, '__event_name__')
            else:
                return event

        result_list = list(map(resovlve_event_topic, object.__getattribute__(self, '__event_list__')))
        object.__getattribute__(self, '__event_list__').clear()
        return '.'.join(result_list)
