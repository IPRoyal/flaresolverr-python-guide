# FlareSolverr 2025: The Ultimate Guide to Bypassing Cloudflare

---

## How it works
- FlareSolverr runs as a background server and accepts JSON POST payloads.  
- Each request spins up an automated browser (Undetected Chrome) to visit the target URL.  
- If Cloudflare challenges are solved, FlareSolverr returns the HTML and cookies. If a CAPTCHA appears, it fails.

---

## Install (recommended: Docker)
**Docker (recommended):**
```bash
docker pull flaresolverr/flaresolverr
docker run flaresolverr/flaresolverr
```

**Linux (binary):**
```bash
mkdir FlareSolverr
cd FlareSolverr
wget <release-tar.gz>
tar -xzf flaresolverr_linux_x64.tar.gz
cd flaresolverr
./flaresolverr
```

**Windows (binary):** download & run `Flaresolverr.exe`, allow firewall if needed.

---

## Configure (examples)
Change timeouts or timezone via environment variables when running Docker:
```bash
docker run -d --name flaresolverr -p 8191:8191 -e BROWSER_TIMEOUT=60000 flaresolverr/flaresolverr
docker run -d --name flaresolverr -p 8191:8191 -e TZ=America/New_York flaresolverr/flaresolverr
```

Or use `docker-compose.yml`:
```yaml
version: '3'
services:
  flaresolverr:
    image: flaresolverr/flaresolverr
    container_name: flaresolverr
    ports:
      - "8191:8191"
    environment:
      - TZ=America/New_York
    restart: unless-stopped
```

Run with `docker-compose up -d` after creating the file.

---

## Usage: send POST requests to FlareSolverr
Below are two verbatim Python examples taken from the article. Each example demonstrates sending a JSON payload to the FlareSolverr HTTP API. The first is a basic request; the second includes a custom `userAgent` field.

### Example 1 — Basic FlareSolverr request
*Send a POST to `http://localhost:8191/v1` with a `request.get` command and a timeout.*
```python
import requests
import json

# Flaresolverr endpoint
url = 'http://localhost:8191/v1'

# Request payload
data = {
    "cmd": "request.get",
    "url": "https://iproyal.com",
    "maxTimeout": 60000  # 60 seconds
}

# Headers
headers = {
    'Content-Type': 'application/json'
}

# Send POST request to Flaresolverr
response = requests.post(url, data=json.dumps(data), headers=headers)

# Print the response content
print(response.text)
```

### Example 2 — Add a custom User-Agent
*Same request but include a `userAgent` field in the payload to specify the browser identity.*
```python
import requests
import json

# Flaresolverr endpoint
url = 'http://localhost:8191/v1'

# Request payload, including a custom User-Agent
data = {
    "cmd": "request.get",
    "url": "https://example.com",
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "maxTimeout": 60000  # 60 seconds
}

# Headers for the POST request
headers = {
    'Content-Type': 'application/json'
}

# Send POST request to Flaresolverr
response = requests.post(url, data=json.dumps(data), headers=headers)

# Print the response content
print(response.text)
```

---

## Pros & Cons (brief)
**Pros:** quick, minimal setup for many Cloudflare challenges; works out of the box.  
**Cons:** heavy resource usage (each request may spawn a browser), not ideal at huge scale, and cannot solve CAPTCHAs.

---

## Final note
Use FlareSolverr for short-to-medium scraping projects where Cloudflare protections are common. For large-scale or performance-critical scraping, consider a custom solution or additional anti-CAPTCHA services.
