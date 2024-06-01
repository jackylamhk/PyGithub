############################ Copyrights and license ############################
#                                                                              #
# Copyright 2024 Jacky Lam <jacky.lam@r2studiohk.com>                          #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
################################################################################

from __future__ import annotations

from typing import Any

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet, Opt


class OrganizationCustomProperty(NonCompletableGithubObject):
    """
    This class represents a CustomProperty for an Organization.

    The reference can be found here
    https://docs.github.com/en/rest/orgs/custom-properties

    """

    @property
    def property_name(self) -> str:
        return self._property_name.value

    @property
    def value_type(self) -> str:
        return self._value_type.value

    @property
    def required(self) -> Opt[bool | None]:
        return self._required.value

    @property
    def default_value(self) -> Opt[str | list[str] | None]:
        return self._default_value.value

    @property
    def description(self) -> Opt[str | None]:
        return self._description.value

    @property
    def allowed_values(self) -> Opt[list[str] | None]:
        return self._allowed_values.value

    @property
    def values_editable_by(self) -> Opt[str | None]:
        return self._values_editable_by.value

    def _initAttributes(self) -> None:
        self._property_name: Attribute[str] = NotSet
        self._value_type: Attribute[str] = NotSet
        self._required: Attribute[bool] = NotSet
        self._default_value: Attribute[str | list[str]] = NotSet
        self._description: Attribute[str] = NotSet
        self._allowed_values: Attribute[list[str]] = NotSet
        self._values_editable_by: Attribute[str] = NotSet

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        self._property_name = self._makeStringAttribute(attributes["property_name"])
        self._value_type = self._makeStringAttribute(attributes["value_type"])
        if "required" in attributes:
            self._required = self._makeBoolAttribute(attributes["required"])
        if "default_value" in attributes:
            self._default_value = self._makeStringAttribute(attributes["default_value"])
        if "description" in attributes:
            self._description = self._makeStringAttribute(attributes["description"])
        if "allowed_values" in attributes:
            self._allowed_values = self._makeListOfStringsAttribute(attributes["allowed_values"])
        if "values_editable_by" in attributes:
            self._values_editable_by = self._makeStringAttribute(attributes["values_editable_by"])


class RepositoryCustomPropertyValues(NonCompletableGithubObject):
    """
    This class represents CustomPropertyValues for a Repository.

    The reference can be found here
    https://docs.github.com/en/rest/orgs/custom-properties#list-custom-property-values-for-organization-repositories

    """

    @property
    def respository_id(self) -> int:
        return self._repository_id.value

    @property
    def repository_name(self) -> str:
        return self._repository_name.value

    @property
    def repository_full_name(self) -> str:
        return self._repository_full_name.value

    @property
    def properties(self) -> dict[str, str]:
        return self._properties.value

    def _initAttributes(self) -> None:
        self._repository_id: Attribute[str] = NotSet
        self._repository_name: Attribute[str] = NotSet
        self._repository_full_name: Attribute[str] = NotSet
        self._properties: Attribute[dict[str, str]] = NotSet

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        self._repository_id = self._makeIntAttribute(attributes["repository_id"])
        self._repository_name = self._makeStringAttribute(attributes["repository_name"])
        self._repository_full_name = self._makeStringAttribute(attributes["repository_full_name"])
        properties = {p["property_name"]: p["value"] for p in attributes["properties"]}
        self._properties = self._makeDictAttribute(properties)
