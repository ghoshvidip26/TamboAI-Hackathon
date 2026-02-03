# Frontend Integration Notes

This directory contains the frontend for the Policy-Aware AI API Explorer.

## Structure

```
frontend/
├── nextjs/          # Next.js application
│   ├── pages/       # Page components
│   ├── components/  # Reusable components
│   └── README.md    # Frontend-specific instructions
└── README.md        # This file
```

## Integration with Backend

The frontend communicates with the backend safety analyzer via REST API:

**Backend Endpoint:** `http://localhost:8000/analyze`

**Request Format:**
```json
{
  "api_spec": "OpenAPI/Swagger spec as text",
  "user_intent": "What the user wants to do",
  "example_payloads": [{"key": "value"}],
  "constructed_input": {"key": "value"}
}
```

**Response Format:**
```json
{
  "verdict": {
    "urgency": false,
    "threat": false,
    "sensitive_request": true,
    "execution_risk": true,
    "data_exposure_risk": false,
    "policy_explanation": "sensitive data + execution risk"
  },
  "ui_contract": {
    "components": ["EndpointList", "SchemaViewer", "SafetyInspector"],
    "restrictions": {
      "execute_requests": false,
      "edit_payloads": false,
      "show_sensitive_fields": false
    },
    "warnings": ["Warning message"],
    "blocked": false
  }
}
```

## UI Contract Rendering

The frontend renders UI based on the `ui_contract`:

- **components**: Which components to display
- **restrictions.execute_requests**: Enable/disable Execute button
- **restrictions.edit_payloads**: Enable/disable payload editing
- **restrictions.show_sensitive_fields**: Show/hide sensitive values
- **warnings**: Display warning banners
- **blocked**: Show blocked state with SafetyInspector only
