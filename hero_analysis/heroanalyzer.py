import json # for work with json_files
import glob # module for finding files by pattern
from pathlib import Path

class HeroAnalyzer:
    """A class to analyze superhero data based on gender and occupation
    """
    
    BASE_DIR = Path(__file__).parent.parent  # lift up by 2 levels
    DEFAULT_DATA_PATH = str(BASE_DIR / 'api' / 'id' / '*.json') #search json files
    
    def __init__(self,gender:str,occupation:bool):
        """Put arguments
        Args:
            gender (str): Heroes gender to filter ('Male'/'Female')
            occupation (bool): Heroes work to filter
        """
        self.gender:str = gender.lower()
        self.occupation:bool = occupation
        self.height_max:int = 0 #stores the maximum height 
        
    def main(self) -> str: 
        """Find the maximum height of superhero
        Work with JSON file in directory and checks each hero:
        - Gender
        - Occupation
        - Height
        
        Returns:
            str: Max height of Hero or "No data!"
        """
        json_files = glob.glob(self.DEFAULT_DATA_PATH)
        if type(self.occupation)!= bool:
            return "Not bool type!"
        for file in json_files:
            try:
                with open(file, 'r', encoding='utf-8') as file:
                    datas = json.load(file)
                    
                    hero_Gender=datas['appearance']['gender'].lower()
                    hero_Occupation = datas['work']['occupation']
                    hero_Height = datas['appearance']['height'][1] # example "180 cm"

                    hero_Height = float(hero_Height.split()[0])   #take str value to flout
                    hero_Height = int(round(hero_Height))       #round float value to int

                    if self._check_string(hero_Occupation) and self._check_gender(hero_Gender) and hero_Height > self.height_max:
                        self.height_max = hero_Height
                        
            except (KeyError, ValueError, IndexError):
                continue
            
        return str(self.height_max) if self.height_max !=0 else "No datas!"
    
    def _check_string(self, hero_Occupation:str) -> bool:
        """Check string hero occupation in str
        Args:
            hero_Occupation (str): Heros occupation
        Returns:
            bool: If len of str occupation has got symbols return True else False
        """

        return bool(len(hero_Occupation)>1) == self.occupation

    def _check_gender(self, hero_Gender: str) -> bool:
        """Check hero gender in str
        Args:
            hero_Gender (str): put gender of hero
        Returns:
            bool: If gender of hero the same what would put return bool True
        """
        return hero_Gender == self.gender
                