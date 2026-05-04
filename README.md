# Smart Home v2

> A complete IoT system I built for managing smart homes. It connects microcontrollers around your house to a web interface where you can control everything and set up automation rules.

[![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.0%2B-darkgreen?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18.3-61dafb?style=flat-square&logo=react)](https://react.dev/)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=flat-square&logo=docker)](https://www.docker.com/)

## What does it do?
This system lets you control IoT devices in your home through a web interface. You can set up sensors, switches, lights, cameras etc. and manage them from your phone or computer.
The main idea is that you have a small hub (like a Raspberry Pi) in your house that talks to all your Arduino/ESP32 devices via MQTT. This hub then connects to a backend server where all your settings, automation rules, and data are stored.

## How it works
* **Smart Home Setup:** Create an account, define rooms, and manage access permissions.
* **Dynamic Configuration:** Map microcontroller pins to specific functions (lights, sensors) directly from the UI.
* **Automation Engine:** Create "If-Condition-Then-Action" rules (e.g., *if temp > 25°C, turn on the fan*).
* **Live Monitoring:** Watch real-time sensor data and camera streams.

### The Hub (Router)

* Acts as a local bridge between your devices and the cloud.
* Communicates with microcontrollers (ESP32, Arduino) via **MQTT**.
* Handles **OTA (Over-the-Air)** firmware updates with local caching.
* Streams video from IP cameras using **HLS**.

### The Backend

* **Django:** Manages the "brain" – users, permissions, and complex configurations.
* **FastAPI:** Handles the heavy lifting – aggregating and processing high-volume sensor data.
* **WebSockets:** Streams live updates from the backend to the user interface instantly.

## Main features
*   **Real-time Dashboard:** Full-duplex communication via WebSockets for instant device monitoring and control.
*   **Hardware Abstraction:** Dynamic peripheral configuration (pin mapping) and remote uC management directly from the UI.
*   **Intelligent Rule Engine:** Custom-built automation engine supporting *If-Condition-Then-Action* logic.
*   **Advanced Access Control:** Home-room-device hierarchy with "Private" vs "Public" room visibility and one-time code (OTC) invite system.
*   **Optimized OTA Updates:** Firmware distribution with local caching at the Gateway level to minimize main server bandwidth consumption.
*   **Multimedia Integration:** Live camera streaming support using the **HLS** (HTTP Live Streaming) protocol.

## Tech Stack

*   **Backend:** Python (Django, FastAPI, Channels)
*   **Frontend:** React (WebSockets, HLS.js)
*   **Messaging:** RabbitMQ (Event-driven), Celery (Task Queue), MQTT
*   **Data & Caching:** PostgreSQL, Redis (Pending states & volatile data)
*   **DevOps:** Docker, Docker Compose, Environment-based configuration (.env)

##  Architecture
![architecture.png](readme/architecture.png)
