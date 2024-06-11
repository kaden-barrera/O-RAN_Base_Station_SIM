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

# Microservices
### 1. Centralized Unit Control Plane (CU-CP)
Path: backend/centralized_unit_cp
Description: Manages control plane functionalities.
Endpoint: /setup_connection
Port: 5000
Documentation: CU-CP Documentation
### 2. Centralized Unit User Plane (CU-UP)
Path: backend/centralized_unit_up
Description: Manages user plane functionalities.
Endpoint: /manage_data
Port: 5001
Documentation: CU-UP Documentation
3. Radio Unit (RU)
Path: backend/radio_unit
Description: Processes radio signals.
Endpoint: /process_signal
Port: 5004
Documentation: RU Documentation
4. Edge Node
Path: backend/edge_node
Description: Processes data at the edge.
Endpoint: /process_data
Port: 5005
Documentation: Edge Node Documentation
5. Service Management and Orchestration (SMO)
Path: backend/smo
Description: Manages and orchestrates services.
Endpoint: /smo_action
Port: 5006
Documentation: SMO Documentation
6. API Gateway
Path: backend/api_gateway
Description: Acts as an entry point for API requests.
Endpoints: /api/setup_connection, /api/manage_mobility
Port: 8080
Documentation: API Gateway Documentation
7. RIC Near Real-Time (Near-RT)
Path: backend/ric_near_rt
Description: Provides real-time optimization and control using machine learning models.
Endpoint: /near_rt_function
Port: 5002
Documentation: RIC Near-RT Documentation
8. RIC Non Real-Time (Non-RT)
Path: backend/ric_non_rt
Description: Manages long-term network optimization, policy control, and data analytics.
Endpoint: /non_rt_function
Port: 5003
Documentation: RIC Non-RT Documentation
