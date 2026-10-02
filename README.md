# NGINX Reverse Proxy & Load Balancer

A hands-on NGINX lab I built to understand how a reverse proxy and load balancer work in a real Linux environment.

The setup uses NGINX as the entry point for two static websites and two backend services. API requests are handled by NGINX and distributed between the backend servers.

## What I Built

- Hosted two websites with NGINX using separate server blocks
- Configured HTTPS with SSL certificates
- Set up NGINX as a reverse proxy for backend API requests
- Added two backend services and configured load balancing
- Added rate limiting and connection limiting for API traffic
- Configured access and error logging
- Kept SELinux enabled and configured it correctly for NGINX
- Tested the setup with curl and concurrent requests

## Architecture

```text
                    Client
                      |
                    HTTPS
                      |
                      v
              +---------------+
              |     NGINX     |
              | :80 / :443    |
              +-------+-------+
                      |
                  /api/ traffic
                      |
               +------+------+
               |             |
               v             v
          Backend 1      Backend 2
            :8080          :8081


