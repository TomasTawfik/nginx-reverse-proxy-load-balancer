# NGINX Reverse Proxy & Load Balancer

A hands-on NGINX project built on Rocky Linux to practice web server configuration, reverse proxying, load balancing, HTTPS, and basic traffic control.

The project uses NGINX as the main entry point for two static websites and two small Python backend services. API requests are handled by NGINX and forwarded to the backend services.

## Architecture

```text
                         Client
                           |
                         HTTPS
                           |
                           v
                  +----------------+
                  |     NGINX      |
                  |  :80 / :443   |
                  +-------+--------+
                          |
                     /api/ traffic
                          |
                 +--------+--------+
                 |                 |
                 v                 v
           Backend 1          Backend 2
             :8080              :8081
```

NGINX serves the frontend websites directly and acts as a reverse proxy for API requests.

## What I Built

The project includes:

- Two static websites hosted with NGINX
- HTTPS using SSL certificates
- Separate NGINX server blocks for the websites
- Reverse proxy for backend API requests
- Two Python backend services
- Load balancing between the backend services
- Rate limiting for API traffic
- Connection limiting
- NGINX access and error logging
- Log rotation
- SELinux kept in enforcing mode
- Firewall configuration for the required services

## Repository Structure

```text
.
├── backend/
│   ├── backend1/
│   │   └── app.py
│   └── backend2/
│       └── app.py
│
├── frontend/
│   ├── site1/
│   └── site2/
│
├── nginx/
│   ├── nginx.conf
│   ├── site1.conf
│   └── site2.conf
│
├── arch/
│   └── architecture.png
│
├── .gitignore
└── README.md
```

The VM files and other local environment files are not included in the repository.

## How It Works

When a user accesses one of the websites, the request reaches NGINX over HTTPS.

For normal website requests, NGINX serves the static files directly.

For requests under `/api/`, NGINX forwards the request to the backend pool:

```text
Client
  |
  | HTTPS
  v
NGINX
  |
  | /api/
  v
Backend Pool
  |
  +----> Backend 1 :8080
  |
  +----> Backend 2 :8081
```

The backend services are simple Python HTTP servers created specifically for testing the NGINX configuration.

## NGINX Configuration

The main configuration is kept under the `nginx/` directory.

The configuration covers:

- Server blocks
- Static file serving
- HTTPS
- Reverse proxying with `proxy_pass`
- Upstream backend servers
- Load balancing
- Rate limiting
- Connection limiting
- Access and error logging

## Testing

I tested the websites and API from the client machine using `curl`.

Basic website test:

```bash
curl -k https://site1.local
```

API test:

```bash
curl -k https://site1.local/api/hello
```

Before applying configuration changes, I checked the NGINX configuration with:

```bash
nginx -t
```

I also tested multiple concurrent API requests to verify the rate limiting:

```bash
for i in {1..100}; do
    curl -k -s -o /dev/null \
    -w "%{http_code}\n" \
    https://site1.local/api/hello &
done
wait
```

The test produced successful `200` responses as well as `503` responses when the configured rate limit was exceeded.

Repeated API requests were also used to verify that traffic was being distributed between the two backend services.

## Logging

NGINX logs were used during the project to check requests and troubleshoot configuration issues.

Access log:

```bash
tail -f /var/log/nginx/access.log
```

Error log:

```bash
tail -f /var/log/nginx/error.log
```

The project also uses the Linux `logrotate` configuration for NGINX logs.

## Security

A few security-related configurations were part of the lab:

- HTTPS enabled for the websites
- SELinux kept in enforcing mode
- Backend ports restricted through the firewall
- Rate limiting for API requests
- Connection limiting
- Private SSL keys excluded from Git

One of the issues I encountered during the setup was SELinux preventing NGINX from connecting to the backend service. Instead of disabling SELinux, I configured the required SELinux policy for NGINX.

## Demo

[Demo Video](YOUR_VIDEO_LINK_HERE)

The demo shows the websites running through NGINX, backend communication, load balancing, rate limiting, and NGINX logs.

## Technologies

- Rocky Linux
- NGINX
- Python
- HTML
- CSS
- JavaScript
- OpenSSL
- SELinux
- VMware
- Git
- GitHub

## Project Status

Completed.

This project was built as a practical lab to gain hands-on experience with NGINX, Linux networking, reverse proxying, load balancing, HTTPS, and basic web server operations.
