## Status

# pyhdpowerview
Python3 interface implementation for Powerview Hub

## Notes
This is for use with [Home-Assistant](http://home-assistant.io)

## Usage
```python
from pyhdpowerview import PowerView

# Connect via IP
pv = PowerView('192.168.1.50')

# Return an array of shade Id objects
shades = pv.get_shades()

# Return shade object
shade = pv.get_shade(shade_id)

# Return attributes of shade
print(shade.id)
print(shade.name)
print(shade.position) # Position represented 0 (close) to 100 (open)
print(shade.battery_level) # Battery level %

# Update shade position

pv.get_status(shade_id)

# Close shade

pv.close_shade(shade_id)

# Open Shade

pv.open_shade(shade_id)

# Stop shade in motion

pv.stop_shade(shade_id)

# Set shade to specific position (0 - 100)

pv.set_shade_position(shade_id, 55)
```
