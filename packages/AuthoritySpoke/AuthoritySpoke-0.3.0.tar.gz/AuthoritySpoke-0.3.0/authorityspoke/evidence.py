r""":class:`.Factor`\s used to support :class:`.Fact` findings."""
from dataclasses import dataclass

from typing import ClassVar, Iterator, Optional

from authorityspoke.entities import Entity
from authorityspoke.factors import ContextRegister, Factor
from authorityspoke.facts import Fact
from authorityspoke.formatting import indented, wrapped


@dataclass(frozen=True)
class Exhibit(Factor):
    """
    A source of information for use in litigation.

    .. note
        "Derived_from" and "offered_by" parameters were removed
        because the former is probably better represented as a :class:`Fact`,
        and the latter as a :class:`Motion`.

    TODO: Allowed inputs for ``form`` will need to be limited.
    """

    form: Optional[str] = None
    statement: Optional[Fact] = None
    stated_by: Optional[Entity] = None
    name: Optional[str] = None
    absent: bool = False
    generic: bool = False
    context_factor_names: ClassVar = ("statement", "stated_by")

    def _means_if_concrete(
        self, other: Factor, context: Optional[ContextRegister] = None
    ) -> Iterator[ContextRegister]:
        if isinstance(other, self.__class__) and self.form == other.form:
            yield from super()._means_if_concrete(other, context)

    def _implies_if_concrete(
        self, other: Factor, context: Optional[ContextRegister] = None
    ) -> Iterator[ContextRegister]:
        if isinstance(other, self.__class__) and (
            self.form == other.form or other.form is None
        ):
            yield from super()._implies_if_concrete(other, context)

    @property
    def short_string(self):
        """
        Return string representation of the object without line breaks.
        """
        string = (
            f'{("by " + self.stated_by.short_string + ", ") if self.stated_by else ""}'
            + f'{("asserting " + self.statement.short_string) if self.statement else ""}'
        )
        string = super().__str__().format(string)
        return string.replace("Exhibit", self.form or "exhibit").strip()

    def __str__(self):
        text = ""
        if self.form:
            text += f"in the FORM of {self.form}"
        if self.stated_by:
            text += f"\n" + indented(f"STATED BY {str(self.stated_by)}")
        if self.statement:
            text += f"\n" + indented(f"ASSERTING:")
            factor_text = indented(str(self.statement), tabs=2)
            text += f"\n{str(factor_text)}"
        return super().__str__().format(text)


@dataclass(frozen=True)
class Evidence(Factor):
    """An :class:`Exhibit` admitted by a court to aid a factual determination."""

    exhibit: Optional[Exhibit] = None
    to_effect: Optional[Fact] = None
    name: Optional[str] = None
    absent: bool = False
    generic: bool = False
    context_factor_names: ClassVar = ("exhibit", "to_effect")

    def __str__(self):
        text = ""
        if self.exhibit:
            text += f"\n" + indented("OF:")
            factor_text = indented(str(self.exhibit), tabs=2)
            text += f"\n{str(factor_text)}"
        if self.to_effect:
            text += f"\n" + indented("INDICATING:")
            factor_text = indented(str(self.to_effect), tabs=2)
            text += f"\n{str(factor_text)}"
        return super().__str__().format(text).strip()

    @property
    def short_string(self):
        string = (
            f'{("of " + self.exhibit.short_string + ", ") if self.exhibit else ""}'
            + f'{("which supports " + self.to_effect.short_string) if self.to_effect else ""}'
        )
        return super().__str__().format(string).strip().replace("Evidence", "evidence")
