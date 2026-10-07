class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_positions = reversed(sorted(zip(position, speed)))

        num_fleets = 0
        last_fleet_time = 0

        individual_time = ((target - p) / s for p, s in     sorted_positions) 


        for time in individual_time: 
            if time > last_fleet_time: # add a new fleet after this 
                num_fleets += 1
                last_fleet_time = time 

        return num_fleets



        

            
        


        
        
        