"""
Enterprise-grade OOP module demonstrating best practices.
"""

import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Optional, List
from functools import lru_cache
from contextlib import contextmanager

logger = logging.getLogger(__name__)


class PersonType(Enum):
    """Enumeration of person types."""
    DEVELOPER = "developer"
    MANAGER = "manager"
    ARCHITECT = "architect"


@dataclass(frozen=True)
class PersonInfo:
    """Immutable person information object."""
    first_name: str
    last_name: str
    person_type: PersonType

    def __post_init__(self):
        if not self.first_name or not self.last_name:
            raise ValueError("Names cannot be empty")

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Communicator(ABC):
    """Abstract base class for communication patterns."""

    @abstractmethod
    def send_message(self, message: str) -> None:
        """Send a message using the communicator."""
        pass

    @abstractmethod
    def receive_message(self) -> Optional[str]:
        """Receive a message from the communicator."""
        pass


class ConsoleCommunicator(Communicator):
    """Console-based implementation of Communicator."""

    def __init__(self):
        self._message_queue: List[str] = []
        logger.info("Initialized ConsoleCommunicator")

    def send_message(self, message: str) -> None:
        """Print message to console and log."""
        if not message:
            raise ValueError("Message cannot be empty")
        print(f"[{self.__class__.__name__}] {message}")
        logger.debug(f"Message sent: {message}")

    def receive_message(self) -> Optional[str]:
        """Retrieve last message from queue."""
        return self._message_queue.pop() if self._message_queue else None

    def queue_message(self, message: str) -> None:
        """Queue a message for later retrieval."""
        self._message_queue.append(message)


class Person:
    """Enterprise Person class with full lifecycle management."""

    _instances: List['Person'] = []
    _message_count: int = 0

    def __init__(
        self,
        info: PersonInfo,
        communicator: Optional[Communicator] = None
    ):
        """
        Initialize a Person instance.

        Args:
            info: PersonInfo dataclass containing name and type
            communicator: Optional communicator instance (defaults to ConsoleCommunicator)

        Raises:
            TypeError: If info is not a PersonInfo instance
        """
        if not isinstance(info, PersonInfo):
            raise TypeError("info must be a PersonInfo instance")

        self._info = info
        self._communicator = communicator or ConsoleCommunicator()
        self._is_active = True
        Person._instances.append(self)
        logger.info(f"Created Person: {self._info.full_name}")

    @property
    def info(self) -> PersonInfo:
        """Get person information (read-only)."""
        return self._info

    @property
    def communicator(self) -> Communicator:
        """Get the communicator instance."""
        return self._communicator

    @contextmanager
    def active_session(self):
        """Context manager for managing active sessions."""
        try:
            self._is_active = True
            logger.info(f"Session started for {self._info.full_name}")
            yield self
        finally:
            self._is_active = False
            logger.info(f"Session ended for {self._info.full_name}")

    def say_greeting(self, greeting: str = "Hello World") -> None:
        """
        Send a greeting message.

        Args:
            greeting: The greeting message to send
        """
        if not self._is_active:
            logger.warning(f"{self._info.full_name} is not in an active session")
            return

        self._communicator.send_message(greeting)
        Person._message_count += 1

    @lru_cache(maxsize=128)
    def get_introduction(self) -> str:
        """
        Get a cached introduction string.

        Returns:
            A formatted introduction
        """
        return (
            f"Hello, I'm {self._info.full_name}, "
            f"a {self._info.person_type.value}"
        )

    def __repr__(self) -> str:
        """Return developer-friendly representation."""
        return (
            f"Person(name={self._info.full_name!r}, "
            f"type={self._info.person_type.value!r})"
        )

    def __str__(self) -> str:
        """Return user-friendly representation."""
        return self._info.full_name

    @classmethod
    def get_all_instances(cls) -> List['Person']:
        """Get all created Person instances."""
        return cls._instances.copy()

    @classmethod
    def get_message_count(cls) -> int:
        """Get total message count across all instances."""
        return cls._message_count

    def __enter__(self):
        """Context manager entry."""
        self._is_active = True
        return self

    def __exit__(self, _exc_type, _exc_val, _exc_tb):
        """Context manager exit."""
        self._is_active = False


class PersonFactory:
    """Factory for creating Person instances with preset configurations."""

    _templates = {
        "developer": PersonInfo(
            first_name="Darpan",
            last_name="Jiyani",
            person_type=PersonType.DEVELOPER
        ),
        "manager": PersonInfo(
            first_name="Project",
            last_name="Manager",
            person_type=PersonType.MANAGER
        ),
    }

    @staticmethod
    def create_person(
        template_key: str,
        communicator: Optional[Communicator] = None
    ) -> Person:
        """
        Create a Person from a template.

        Args:
            template_key: Key of the template to use
            communicator: Optional custom communicator

        Returns:
            New Person instance

        Raises:
            KeyError: If template_key is not found
        """
        if template_key not in PersonFactory._templates:
            raise KeyError(f"Template '{template_key}' not found")

        info = PersonFactory._templates[template_key]
        return Person(info, communicator)


# === Configuration & Logging Setup ===
def setup_logging(level: int = logging.INFO) -> None:
    """Configure logging for the module."""
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


# === Example Usage ===
if __name__ == "__main__":
    setup_logging()

    # Using PersonFactory
    person1 = PersonFactory.create_person("developer")
    person2 = PersonFactory.create_person("manager")

    # Using context manager
    with person1.active_session():
        person1.say_greeting("Hello World")
        person1.say_greeting(person1.get_introduction())

    with person2.active_session():
        person2.say_greeting("Hello Globe")

    # Demonstrate properties and introspection
    print(f"\n{person1}")
    print(f"Representation: {repr(person1)}")
    print(f"Total messages sent: {Person.get_message_count()}")
    print(f"All instances: {Person.get_all_instances()}")