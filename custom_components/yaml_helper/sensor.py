"""Sensor platform for yaml_helper."""
from __future__ import annotations

import logging
from typing import Any, final

# from homeassistant.components.sensor import SensorEntity, SensorEntityDescription
from homeassistant.components.sensor import SensorEntity, SensorStateClass
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_NAME, CONF_UNIQUE_ID
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.reload import async_setup_reload_service
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from . import PLATFORMS
from .const import DOMAIN, ICON, VALUES

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
    values = config_entry.options[VALUES]
    async_add_entities(
        [YamlHelperSensor(config_entry.title, values, config_entry.entry_id)]
    )


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Setup Yaml Helper sensor"""
    name: str | None = config.get(CONF_NAME)
    values: str = config[VALUES]
    unique_id = config.get(CONF_UNIQUE_ID)
    await async_setup_reload_service(hass, DOMAIN, PLATFORMS)
    async_add_entities([YamlHelperSensor(name, values, unique_id)])


class YamlHelperSensor(SensorEntity):
    """Yaml Helper Sensor class."""

    _attr_icon = ICON
    _attr_should_poll = False
    _attr_state_class = SensorStateClass.MEASUREMENT

    def __init__(
        self, name: str | None, config: ConfigType, unique_id: str | None
    ) -> None:
        """Initialize the sensor class."""
        _LOGGER.debug("--> YamlHelperSensor#__init__")
        _LOGGER.debug("name: %s", name)
        _LOGGER.debug("config: %s", config)
        _LOGGER.debug("unique_id: %s", unique_id)
        self._attr_unique_id = unique_id
        self._config = config
        if name:
            self._attr_name = name
        else:
            self._attr_name = "Yaml Helper Sensor"

    @final
    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        _LOGGER.debug("--> YamlHelperSensor#state_attributes")
        _LOGGER.debug("config: %s", self._config)
        data: dict[str, Any] = {}
        data["values"] = self._config
        _LOGGER.debug("data: %s", data)
        return data
