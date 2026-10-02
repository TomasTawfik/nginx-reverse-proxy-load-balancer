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

Project Structure
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
├── docs/
│   └── architecture.png
│
├── .gitignore
└── README.md
A Few Things I Learned

The main part of this project was not just getting NGINX running, but understanding what happens between the client and the backend.

I worked with:

NGINX server blocks and virtual hosts
Reverse proxying with proxy_pass
Upstream servers and round-robin load balancing
TLS termination
NGINX rate and connection limits
Linux firewall configuration
SELinux policies for web services
NGINX access and error logs

One issue I ran into was SELinux blocking NGINX from connecting to the backend. I kept SELinux enforcing and fixed the problem by allowing the required network connection for the NGINX service instead of disabling SELinux.

Testing

I tested the API through NGINX:

curl -k https://site1.local/api/hello

I also sent multiple requests to verify load balancing and rate limiting.

For example:

for i in {1..100}; do
    curl -k -s -o /dev/null \
    -w "%{http_code}\n" \
    https://site1.local/api/hello &
done
wait

The test produced successful responses as well as 503 responses when the configured rate limit was exceeded.

Demo

Demo video

The demo shows the websites, backend communication, load balancing, rate limiting, and NGINX logs.

Technologies

NGINX Rocky Linux Python OpenSSL SELinux VMware Git

### Why I prefer this

A recruiter can understand it in **30–60 seconds**:

- **What did he build?** → NGINX reverse proxy/load balancer.
- **Did he actually do it?** → Specific testing and the SELinux problem.
- **What does he know?** → NGINX, Linux, networking, TLS, SELinux, load balancing.
- **Where is the code?** → Clear repository structure.
- **Can I see it?** → Demo link.

And notice what I **didn't** put in it:

❌ "This project demonstrates my passion..."  
❌ "In today's modern infrastructure..."  
❌ Huge explanations of what NGINX is  
❌ 30 commands copied from a tutorial  
❌ "I would like to thank..."  
❌ ChatGPT-style conclusion  
❌ Every single step I performed in the lab  

The README should make the **repository itself** look professional. The detailed learning can go into your interview discussion.

One more thing: I'd also rename your folders from `nginx-lab-website frondend` to `frontend/site1` and `nginx-lab-second-site frondend` to `frontend/site2` before we push. That will make the repo look much cleaner.

