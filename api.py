import enum 
from typing import Annotated

from livekit.agents import llm
import logging


logger = logging.getLogger("temperature_control")
logger.setLevel(logging.INFO)

class Zone(enum.Enum):
    LIVING_ROOM = "living_room"
    BEDROOM = "bedroom"
    KITCHEN = "kitchen"
    BATHROOM = "bathroom"
    OFFICE = "office"

class AssistantFunction(llm.FunctionContext):
    def __init__(self) -> None:
        super().__init__()

        self._temperature = {
            Zone.LIVING_ROOM: 22,
            Zone.BEDROOM: 23,
            Zone.KITCHEN: 27,
            Zone.BATHROOM: 20,
            Zone.OFFICE: 21,
        }

    @llm.ai_callable(name="get_temperature", description="Get the temperature in a specific zone")
    def get_temperature(self, zone: Annotated[Zone, llm.TypeInfo(description="The zone to get the temperature of")]) -> int:
        logger.info(f"Getting temperature for {zone}")
        temp = self._temperature[Zone(zone)]
        return f"The temperature in the {zone} is {temp}C"
    
    @llm.ai_callable(name="set_temperature", description="Set the temperature in a specific zone")
    def set_temperature(self, zone: Annotated[Zone, llm.TypeInfo(description="The zone to set the temperature of")], temperature: Annotated[int, llm.TypeInfo(description="The temperature to set the zone to")]) -> None:
        logger.info(f"Setting temperature for {zone} to {temperature}")
        self._temperature[Zone[zone]] = temperature
        return f"The temperature in the {zone} has been set to {temperature}C"
