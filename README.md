<h1 align="center">Welcome to link_speed_monitor 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
</p>

> Monitoring the Internet link speed and log the results into a csv file.

## Install

Clone this repository and install the requirements
```sh
pip install -r requirements.txt
```

## Usage

Run the following command
```sh
python3 main.py
```

### Scheduling

If you want to monitor the link speed for a while, open the main.py file, and in line 8 set the time interval that the test should be executed.
```
#Timer(180, main).start()
```
Remove # and set the time you want to set as the interval for monitoring, 180 means seconds.

## Results

```
After run the speed test, check the results at result/dados.csv
```

## Author

👤 **Irvin Bezerra**

* Website: https://irvin-s.github.io
* Linked-in: https://www.linkedin.com/in/irvin-bezerra-b568a6204/
* Github: [@irvin-s](https://github.com/irvin-s)

## Show your support

Give a ⭐️ if this project helped you!

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_