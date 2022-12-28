# CE_Calc

Carbon (CO2) Emission Footprint Calculator

### Commands

After **Downloading/cloning** the Project i.e **CE_Calc**

Make sure You have Python install, then
Open *terminal* **(recommanded "GIT Bash")** in the *root directory* of the project and **_RUN_**

if it is your first time

* ```bash
  sh setup
  ```

else

* ```python
  python manage.py runserver
  ```

##### JSON data at *api/get_br_data*

```json
[
    {
        "uid": "kabir-swift",
        "date": "2022-07-05",
        "time": "11:44:04",
        "state": "connected standby",
        "ru": {
            "source": "ac",
            "capacity_percent": 5,
            "capacity": 1528
        },
        "bu": {
            "duration": "00:00:00",
            "energy_percent": 0,
            "energy": 0
        }
    },

    {
        "uid": "xe-ggn-it-02893",
        "date": "2022-07-05",
        "time": "13:44:37",
        "state": "active",
        "ru": {
            "source": "ac",
            "capacity_percent": 85,
            "capacity": 27554
        },
        "bu": null
    },

    {
        "uid": "kabir-swift",
        "date": "2022-07-26",
        "time": "10:57:20",
        "state": "connected standby",
        "ru": null,
        "bu": {
            "duration": "00:04:02",
            "energy_percent": 0,
            "energy": 46
        }
    },
  
]
```
