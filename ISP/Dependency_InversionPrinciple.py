class SwitchableDevice:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

class Light(SwitchableDevice):
    def turn_on(self):
        pass
        # Logic to turn on the light

    def turn_off(self):
        # Logic to turn off the light
        pass
class Fan(SwitchableDevice):
    def turn_on(self):
        # Logic to turn on the fan
        pass
    def turn_off(self):
        # Logic to turn off the fan
        pass
class HomeAutomationController:
    def __init__(self, devices):
        self.devices = devices

    def activate(self):
        for device in self.devices:
            device.turn_on()

    def deactivate(self):
        for device in self.devices:
            device.turn_off()
            
            
             


# We introduce the SwitchableDevice abstraction that defines the behavior for turning devices on and off.
# Both Light and Fan implement the SwitchableDevice interface, providing the specific behavior.
# The HomeAutomationController now depends on the abstraction (SwitchableDevice) instead of concrete implementations. You can add or change devices without modifying the high-level module.
# By adhering to the Dependency Inversion Principle, we invert the dependency direction. 
# High-level modules now depend on abstractions, which leads to more flexible, maintainable, and extensible code. 
# This principle helps avoid tightly coupled code and enables easier changes and additions to the system without 
# affecting existing functionality.
