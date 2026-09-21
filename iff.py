class IFF:
    """Represents the Identification Friend or Foe
    that identifies hostile entities from radar data"""

    def __init__(self):
        pass
    
    def is_hostile_entity_detected(self, sequence):
        odd_count = 0
        even_count = 0
        
        for element in sequence:
            decimal_nr = int(element, 2)
            if decimal_nr % 2 == 1:
                odd_count +=1
            else:
                even_count +=1
        
        return odd_count > even_count
