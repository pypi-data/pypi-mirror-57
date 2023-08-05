import enum


class LanguageEnumMeta(enum.EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())


class Language(enum.Enum, metaclass=LanguageEnumMeta):
    C = ("c",)
    CPP = ("cpp",)
    JAVA = ('java',)
    PYTHON = ('python',)

    def __init__(self, canonical_name: str) -> None:
        self.__canonical_name = canonical_name

    @property
    def canonical_name(self) -> str:
        """The canonical name of this language."""
        return self.__canonical_name

    def __str__(self) -> str:
        return self.__canonical_name
