# AI Microservices App

## Overview
This repository contains a set of AI-based microservices designed to streamline the data processing, model training, prediction, and monitoring of AI models.
The AI Microservices App, which consists of multiple microservices designed to handle tasks related to AI. These include services for data processing, model training, prediction deployment, and monitoring the health of the entire system. Each service is modular, making it easy to scale and maintain independently while working together to perform complex AI tasks in a distributed manner. The system is designed to streamline AI workflows using modern microservices architecture.

### Key Components
1. **Data Processing Service** - Responsible for data preparation and cleaning.
2. **Model Training Service** - Trains machine learning models based on processed data.
3. **Prediction Service** - Deploys the trained models and serves predictions.
4. **Monitoring Service** - Monitors the health and performance of deployed services.

## Requirements
- Python 3.x
- Docker
- Jenkins (for CI/CD)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Yash-Raj-96/ai-microservices-app.git
    cd ai-microservices-app
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Build and run Docker containers:
    ```bash
    docker-compose up
    ```

## Usage
- Use Docker to manage containers for each microservice.
- Access services via their respective APIs (details to be added).
