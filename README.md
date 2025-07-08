# Asset-tracker
Abstract
This project aims to develop an asset-tracking system suitable for both indoor and outdoor environments. A Raspberry Pi mounted on the asset periodically broadcasts Bluetooth Low Energy (BLE) signals. Two stationary Raspberry Pis, placed at fixed and known locations, detect these signals and measure their Received Signal Strength Indicator (RSSI) values. The collected RSSI data is then transmitted to a centralized server, which estimates the asset’s position using RSSI-based distance estimation and trilateration techniques. To support outdoor tracking, a GPS module is also interfaced with the mobile Raspberry Pi, providing accurate location coordinates when satellite connectivity is available. This hybrid approach enables seamless switching between indoor RSSI-based localization and outdoor GPS tracking. The system ensures real-time monitoring of asset location with minimal infrastructure and cost, making it ideal for various industrial and research applications.


Project Overview
This project aims to develop an asset-tracking system suitable for both indoor and outdoor environments. A Raspberry Pi mounted on the asset periodically broadcasts Bluetooth Low Energy (BLE) signals. Two stationary Raspberry Pis, placed at fixed and known locations, detect these signals and measure their Received Signal Strength Indicator (RSSI) values. The collected RSSI data is then transmitted to a centralized server, which estimates the asset’s position using RSSI-based distance estimation and trilateration techniques.

To support outdoor tracking, a GPS module is also interfaced with the mobile Raspberry Pi, providing accurate location coordinates when satellite connectivity is available. This hybrid approach enables seamless switching between indoor RSSI-based localization and outdoor GPS tracking. The system ensures real-time monitoring of asset location with minimal infrastructure, making it ideal for various industrial and research applications.


Introduction
Asset tracking is a critical requirement across various industries, including logistics, manufacturing, healthcare, and warehousing, where real-time location of equipment or inventory is essential for operational efficiency. Traditional tracking systems often rely on expensive infrastructure and specialized wireless networks, which may not be practical for indoor environments or budget-constrained deployments.

This project introduces a cost-effective, Raspberry Pi- based asset-tracking system designed to operate seamlessly in both indoor and outdoor settings. By leveraging Bluetooth Low Energy (BLE) and the signal strength of BLE advertisements (RSSI), the system estimates the location of an asset using trilateration.

A mobile Raspberry Pi unit attached to the asset emits periodic BLE beacons, which are picked up by two or more stationary Raspberry Pis strategically placed at fixed, known positions. These receivers record the RSSI values and forward the data to a central server, where distance estimation algorithms compute the asset's position.

For outdoor tracking, a GPS module is interfaced with the mobile Raspberry Pi to provide precise latitude and longitude coordinates when satellite connectivity is available. This hybrid approach allows the system to switch seamlessly between indoor RSSI-based localization and outdoor GPS tracking, ensuring continuous and accurate asset monitoring under varied conditions.


Literature Survey
Asset-tracking technologies have evolved significantly to support real-time monitoring of items across sectors like logistics, healthcare, and manufacturing. Several positioning methods have been explored in literature, including GPS, RFID, Wi-Fi, and Bluetooth Low Energy (BLE).

GPS is highly accurate for outdoor environments but suffers from poor indoor performance and high power consumption, making it unsuitable for indoor tracking scenarios (Zafari et al., 2019). RFID systems offer low-cost tracking but require dense reader infrastructure, especially for real-time applications (Want, 2006). Wi-Fi-based localization is commonly used due to infrastructure availability, but its accuracy is limited by RSSI fluctuations caused by multipath interference (Youssef & Agrawala, 2005).

BLE has emerged as a viable alternative due to its low power usage, ease of deployment, and compatibility with mobile devices. BLE-based localization techniques rely on the Received Signal Strength Indicator (RSSI) to estimate the distance between the asset and fixed receivers. Although RSSI is inherently noisy, filtering techniques such as moving averages or Kalman filters can improve consistency (Faragher & Harle, 2015).

WiFi SLAM: Research by Stanford explores indoor localization through Wi-fi based simultaneous localization and mapping.

Position estimation often uses trilateration, which involves calculating distances from at least three known points based on signal strength to estimate a target’s position. In contrast, triangulation uses angles of arrival from multiple reference points. While triangulation typically requires angle sensors or antenna arrays, trilateration is more suitable for BLE systems since it works with scalar RSSI values and simple hardware.

Several studies have demonstrated the use of Raspberry Pi as a cost-effective platform for BLE scanning and data aggregation. For instance, Patil et al. (2021) implemented a BLE-based indoor localization system using Raspberry Pi and achieved room-level accuracy. However, many existing solutions require extensive calibration or proprietary software.

This project builds upon such efforts by proposing a low-cost, Raspberry Pi-based asset-tracking system that uses BLE beacons and RSSI-based trilateration. By leveraging a centralized server and cloud tunneling (via ngrok), the system enables real-time tracking with minimal infrastructure, making it ideal for rapid prototyping and educational use.


Technologies Used:
Raspberry Pi Zero 2 W
Neo 7M
Flask
ngrock


Methodology
Indoor Tracking
Components:

● RPi-A and RPi-B → send BLE RSSI values

● Laptop server → receives and prints them via Flask

● ngrok → makes the server reachable over the internet

Step 1: Central Server (Laptop)
1.1 Install Flask
