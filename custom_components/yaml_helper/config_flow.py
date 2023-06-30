"""Adds config flow for Blueprint."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, cast

import voluptuous as vol

from homeassistant.helpers import selector
from homeassistant.helpers.schema_config_entry_flow import (
    SchemaConfigFlowHandler,
    SchemaFlowFormStep,
)

from .const import DOMAIN, KEY_NAME, KEY_VALUE

OPTIONS_SCHEMA = vol.Schema(
    {
        vol.Required(KEY_NAME): selector.TextSelector(),
        vol.Required(KEY_VALUE): selector.TextSelector(),
    }
)

CONFIG_SCHEMA = vol.Schema({vol.Required("name"): selector.TextSelector()}).extend(
    OPTIONS_SCHEMA.schema
)

CONFIG_FLOW = {"user": SchemaFlowFormStep(CONFIG_SCHEMA)}

OPTIONS_FLOW = {"init": SchemaFlowFormStep(OPTIONS_SCHEMA)}


class YamlHelperFlowHandler(SchemaConfigFlowHandler, domain=DOMAIN):
    """Config flow for Yaml helper."""

    config_flow = CONFIG_FLOW
    options_flow = OPTIONS_FLOW

    def async_config_entry_title(self, options: Mapping[str, Any]) -> str:
        """Return config entry title"""
        return cast(str, options["name"]) if "name" in options else ""
