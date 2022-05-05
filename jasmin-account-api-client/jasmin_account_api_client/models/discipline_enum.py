from enum import Enum


class DisciplineEnum(str, Enum):
    ATMOSPHERIC_PHYSICS = "Atmospheric Physics"
    ATMOSPHERIC_CHEMISTRY = "Atmospheric Chemistry"
    CLIMATE_CHANGE = "Climate Change"
    EARTH_SYSTEM_SCIENCE = "Earth System Science"
    MARINE_SCIENCE = "Marine Science"
    TERRESTRIAL_AND_FRESH_WATER = "Terrestrial and Fresh Water"
    EARTH_OBSERVATION = "Earth Observation"
    POLAR_SCIENCE = "Polar Science"
    GEOGRAPHY = "Geography"
    ENGINEERING = "Engineering"
    MEDICALBIOLOGICAL_SCIENCES = "Medical/Biological Sciences"
    MATHEMATICSCOMPUTER_SCIENCE = "Mathematics/Computer Science"
    ECONOMICS = "Economics"
    OTHER = "Other"

    def __str__(self) -> str:
        return str(self.value)
