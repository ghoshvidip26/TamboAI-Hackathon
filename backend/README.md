# Policy-Aware AI API Explorer - Backend

A FastAPI backend for analyzing API safety and generating dynamic UI plans.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn main:app --reload --port 8000
```

## Expected Output

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started server process [PID]
INFO:     Waiting for application startup.
Policy-Aware AI API Explorer started
INFO:     Application startup complete.
```

## API Documentation

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## Endpoints

### Health Check
```http
GET /health
```
Response:
```json
{"status": "healthy"}
```

### Safety Analysis
```http
POST /analyze-api
Content-Type: application/json

{
  "api_spec": "openapi: 3.0.0...",
  "user_intent": "process payment",
  "example_payloads": [],
  "constructed_input": {"card_number": "4111"}
}
```
Response:
```json
{
  "urgency": false,
  "threat": false,
  "sensitive_request": true,
  "explanation": "Sensitive fields detected: card_number"
}
```

### UI Plan Generation
```http
POST /generate-ui-plan
Content-Type: application/json

{
  "urgency": true,
  "threat": false,
  "sensitive_request": true,
  "explanation": "API requests card number and CVV"
}
```
Response:
```json
{
  "components": ["EndpointList", "RequestBuilder", "ResponseViewer", "SafetyInspector"],
  "restrictions": {
    "execute_requests": false,
    "edit_payloads": true,
    "show_sensitive_fields": false,
    "editable_fields": []
  }
}
```

## Console Logs

Successful requests:
```
INFO:     127.0.0.1:12345 - "POST /analyze-api HTTP/1.1" 200 OK
```

## Environment Variables

See `.env.example` for required configuration:
- `SUPABASE_URL` - Supabase project URL
- `SUPABASE_KEY` - Supabase anon key
- `LOCAL_MODE` - 1 for rules only, 0 for rules + LLM

## Project Structure

```
backend/
├── middleware/          # CORS, logging, error, safety middleware
├── routers/             # API routes
│   ├── api.py           # Health check
│   ├── analyze_api.py   # POST /analyze-api
│   └── ui_plan.py       # POST /generate-ui-plan
├── services/            # Business logic
│   ├── safety_service.py
│   ├── ui_service.py
│   └── supabase_service.py
├── sql/                 # Database schema & policies
├── config.py            # Configuration
├── main.py              # FastAPI app
└── requirements.txt     # Dependencies
```
