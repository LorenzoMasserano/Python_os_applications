from typing import Any

class DiContainer():
    def __init__(self):
        self._service: dict[type, Any] = {}

    def register[T] (self, interface_class: type[T], instance: T) -> None:
        
        if not isinstance(instance, interface_class):
            raise TypeError(f"Instance must be of type {interface_class.__name__}")

        self._service[interface_class] = instance

    def resolve[T] (self, interface_class: type[T]) -> T:

        if interface_class not in self._service:
            raise ValueError(f"Dependency '{interface_class.__name__}' is not registered.")

        return self._service[interface_class]
