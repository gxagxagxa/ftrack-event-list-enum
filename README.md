# ftrack-event-list-enum

A enumerator for ftrack events.

- support Ftrack Event List.
- support IDE code completion, prevent from typo errors.
- behave like enum.Enum, also support Nested.
- support chainable call, with any attributes.
- support strict mode, only get defined attributes.
- support customized Enum class, by inheriting NestEnumBase class.
- easy declaration, all by class attributes.

# How to Use?

## generate ftrack defined event string

```python
from ftrack_event_enum.event_enum import FtrackEventEnum

event = FtrackEventEnum().ACTION.DISCOVER
print(event.value)  # ftrack.action.dicover
```

## generate ftrack custom event string

```python
from ftrack_event_enum.event_enum import FtrackEventEnum

event = FtrackEventEnum().ACTION.customized
print(event.value)  # ftrack.action.customized

event = FtrackEventEnum().xxx.yyy.zzz
print(event.value)  # ftrack.xxx.yyy.zzz

event = FtrackEventEnum().ACTION['*']
print(event.value)  # ftrack.action.*
```

## customized nested enum class

```python
from ftrack_event_enum.base import NestEnumBase


class World(NestEnumBase):
    __event_name__ = 'world'


class Hello(NestEnumBase):
    __event_name__ = 'hello'
    WORLD = World()
    OTHER = 'other'


print(Hello().WORLD.value)  # hello.world
print(Hello().OTHER.value)  # hello.other
```
