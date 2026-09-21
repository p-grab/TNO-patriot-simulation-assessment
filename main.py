from patriot import Patriot
from radar import Radar
from iff import IFF
from firing_unit import FiringUnit


def run_simulation(file_path="radar-output.csv", simulation_duration=20):
    print("Patriot Air Defence System simulation")
    
    radar = Radar(file_path)
    iff = IFF()
    firing_unit = FiringUnit()
    patriot = Patriot(radar, iff, firing_unit)

    for timestep in range(simulation_duration):
        sequence = patriot.radar.scan()
        if sequence is None:
            break
        
        print(f"\nTime step {timestep + 1}s")
        hostile_detected = patriot.iff.is_hostile_entity_detected(sequence)

        if hostile_detected:
            print("Hostile entity detected.")
            shot_successful = patriot.firing_unit.fire()

            print("Missile launched.")
            if shot_successful:
                print("Target neutralized.")
            else:
                print("Target was not neutralized.")
        else:
            print("No hostile entity detected.")
            print("No missile launched.")
            print("Target neutralized: N/A")

    patriot.radar.close_file()
            
          
if __name__ == "__main__":
    run_simulation()
