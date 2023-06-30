"""Sensor platform for yaml_helper."""
from __future__ import annotations

import logging

# from homeassistant.components.sensor import SensorEntity, SensorEntityDescription
from homeassistant.components.sensor import SensorEntity, SensorStateClass
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_NAME, CONF_UNIQUE_ID
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.reload import async_setup_reload_service
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from . import PLATFORMS
from .const import DOMAIN, ICON, KEY_NAME, KEY_VALUE

_LOGGER = logging.getLogger(__name__)

# ENTITY_DESCRIPTIONS = (
#     SensorEntityDescription(
#         key="yaml_helper",
#         name="Integration Sensor",
#         icon="mdi:format-quote-close",
#     ),
# )


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Initialize Yaml Helper config entry."""
    _LOGGER.debug("--> async_setup_entry")
    key_name = config_entry.options[KEY_NAME]
    key_value = config_entry.options[KEY_VALUE]
    async_add_entities(
        [
            YamlHelperSensor(
                config_entry.title, key_name, key_value, config_entry.entry_id
            )
        ]
    )


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Setup Yaml Helper sensor"""
    _LOGGER.debug("--> async_setup_platform")
    name: str | None = config.get(CONF_NAME)
    key_name: str = config[KEY_NAME]
    key_value: str = config[KEY_VALUE]
    unique_id = config.get(CONF_UNIQUE_ID)
    await async_setup_reload_service(hass, DOMAIN, PLATFORMS)
    async_add_entities([YamlHelperSensor(name, key_name, key_value, unique_id)])


class YamlHelperSensor(SensorEntity):
    """Yaml Helper Sensor class."""

    _attr_icon = ICON
    _attr_should_poll = False
    _attr_state_class = SensorStateClass.MEASUREMENT

    def __init__(
        self, name: str | None, key_name: str, key_value: str, unique_id: str | None
    ) -> None:
        """Initialize the sensor class."""
        _LOGGER.debug("--> __init__")
        self._attr_unique_id = unique_id
        self._key_name = key_name
        self._key_value = key_value
        if name:
            self._attr_name = name
        else:
            self._attr_name = "Yaml Helper Sensor"
