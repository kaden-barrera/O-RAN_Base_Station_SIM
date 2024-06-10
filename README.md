# O-RAN Base Station Simulator

## Project Overview
The O-RAN Base Station Simulator is a comprehensive tool designed to simulate Open Radio Access Network (O-RAN) base stations. This simulator supports key features such as TV White Space (TVWS) and Massive-MIMO technologies, real-time optimization, and integration with machine learning models for enhanced network performance.

## Features
- **API Gateway**: Routes requests to appropriate backend services.
- **Radio Unit (RU)**: Supports TVWS and Massive-MIMO technologies.
- **Distributed Unit (DU)**: Implements real-time baseband processing functions.
- **Centralized Unit - Control Plane (CU-CP)**: Manages control plane tasks like signaling and connection setup.
- **Centralized Unit - User Plane (CU-UP)**: Handles user plane tasks like data packet forwarding and QoS enforcement.
- **RIC Near Real-Time (Near-RT)**: Provides real-time optimization and control using machine learning models.
- **RIC Non Real-Time (Non-RT)**: Manages long-term network optimization, policy control, and data analytics.
- **Service Management and Orchestration (SMO)**: Manages the lifecycle of network services and resources.
- **Edge Node**: Implements edge computing for local processing and low-latency tasks.

## Quick Start Guide
1. Clone the Repository:
   git clone https://github.com/yourusername/O-RAN_Base_Station_SIM.git
2. Navigate to the Project Directory:
   cd O-RAN_Base_Station_SIM
3. Install Dependencies:
   pip install -r requirements.txt
4. Build the Docker Images:
   docker-compose build
5. Run the Simulator:
   docker-compose up

### Prerequisites
- Docker
- Docker Compose
- Python 3.8+
- Node.js
- Git

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/O-RAN_Base_Station_SIM.git
