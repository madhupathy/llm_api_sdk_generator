# LLM API/SDK Generator

This is a full-stack project that uses a **React (Next.js) frontend** and a **Python FastAPI backend** to generate OpenAPI specifications, gRPC definitions, and SDK code using LLMs (e.g., OpenAI or similar).

---

##  URLs

- **Frontend** (Vercel): [https://llm-api-sdk-generator.vercel.app/](https://llm-api-sdk-generator.vercel.app/)
- **Backend** (Render): [https://llm-api-backend.onrender.com/](https://llm-api-backend.onrender.com/)

---

## Features

- Input plain English descriptions of API features
- Generate:
  - OpenAPI (Swagger) schema
  - gRPC service definitions
  - SDK code samples (e.g., Python)

---

## Example Input

Paste the following into the frontend and click **Generate**:

```
Design a REST API for a user management system. It should support:
- User registration with email and password
- Login with JWT authentication
- Fetching the current user's profile
- Updating user details (email, name)
- Deleting the account
```

---

## Expected Output

###  OpenAPI
```json
{
  "paths": {
    "/register": {
      "post": {
        "summary": "Register new user"
      }
    },
    "/login": {
      "post": {
        "summary": "Login and return JWT"
      }
    }
  }
}
```

###  gRPC
```proto
service UserService {
  rpc Register(UserRequest) returns (UserResponse);
  rpc Login(LoginRequest) returns (LoginResponse);
}
```

###  SDK (Python)
```python
import requests
def register_user(email, password):
    return requests.post("https://api.example.com/register", json={"email": email, "password": password})
```

---

##  Project Structure

```
llm_api_sdk_generator/
├── backend/
│   ├── main.py
│   ├── requirements.txt
├── frontend/
│   ├── pages/
│   │   └── index.js
│   ├── public/
│   ├── next.config.js
│   └── package.json
├── render.yaml
├── README.md
```

---

##  Deployment Guide

### Frontend (Vercel)

1. Go to [https://vercel.com](https://vercel.com) and import the repo.
2. Set:
   - **Root Directory**: `frontend`
   - **Framework Preset**: `Next.js`
3. Leave build commands as default:
   - `npm install`
   - `npm run build`
4. Deploy.

URL: https://llm-api-sdk-generator.vercel.app/

---

### Backend (Render)

1. Go to [https://render.com](https://render.com) and create a **Web Service**.
2. Set:
   - **Environment**: Python
   - **Start Command**: `uvicorn main:app --host=0.0.0.0 --port=10000`
   - **Root Directory**: `backend`
   - **Build Command**: `pip install -r requirements.txt`
3. Deploy.

URL: https://llm-api-backend.onrender.com/

---
