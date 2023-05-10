from enum import Enum


class DisciplineEnum(str, Enum):
    ATMOSPHERIC_CHEMISTRY = "Atmospheric Chemistry"
    ATMOSPHERIC_PHYSICS = "Atmospheric Physics"
    CLIMATE_CHANGE = "Climate Change"
    EARTH_OBSERVATION = "Earth Observation"
    EARTH_SYSTEM_SCIENCE = "Earth System Science"
    ECONOMICS = "Economics"
    ENGINEERING = "Engineering"
    GEOGRAPHY = "Geography"
    MARINE_SCIENCE = "Marine Science"
    MATHEMATICSCOMPUTER_SCIENCE = "Mathematics/Computer Science"
    MEDICALBIOLOGICAL_SCIENCES = "Medical/Biological Sciences"
    OTHER = "Other"
    POLAR_SCIENCE = "Polar Science"
    TERRESTRIAL_AND_FRESH_WATER = "Terrestrial and Fresh Water"

    def __str__(self) -> str:
        return str(self.value)
