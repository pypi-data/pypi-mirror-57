# beSMArt

![](https://i.imgflip.com/1jqcf8.jpg)

Python connector for SMA solar panel

## Usage

```py
from beSMArt import get_data, get_attribute

data = get_data("192.168.1.100") # IP of your SMA device
total_yield = get_attribute(data, "total_yield") # You can check available fields in table underneath
```

## Fields

I got this from https://github.com/kellerza/pysma thanks to @kellerza

| API_ID          | Field               | Unit |
| --------------- | ------------------- | ---- |
| `6100_40263F00` | grid_power          | W    |
| `6100_00465700` | frequency           | Hz   |
| `6100_00464800` | voltage_l1          | V    |
| `6100_00464900` | voltage_l2          | V    |
| `6100_00464A00` | voltage_l3          | V    |
| `6100_40465300` | current_l1          | A    |
| `6100_40465400` | current_l2          | A    |
| `6100_40465500` | current_l3          | A    |
| `6100_0046C200` | pv_power            | W    |
| `6380_40451F00` | pv_voltage          | V    |
| `6380_40452100` | pv_current          | A    |
| `6400_0046C300` | pv_gen_meter        | kWh  |
| `6400_00260100` | total_yield         | kWh  |
| `6400_00262200` | daily_yield         | Wh   |
| `6100_40463600` | grid_power_supplied | W    |
| `6100_40463700` | grid_power_absorbed | W    |
| `6400_00462400` | grid_total_yield    | kWh  |
| `6400_00462500` | grid_total_absorbed | kWh  |
| `6100_00543100` | current_consumption | W    |
| `6400_00543A00` | total_consumption   | kWh  |
