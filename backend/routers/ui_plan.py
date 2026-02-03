"""
UI Plan Router - Handles /generate-ui-plan endpoint.
"""
from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import Any, Dict, List, Optional

from services.ui_service import generate_ui_plan, get_conservative_ui_plan

router = APIRouter()


class VerdictInput(BaseModel):
    """Input schema - safety verdict for UI plan generation."""
    urgency: bool = Field(..., description="Whether request shows urgency")
    threat: bool = Field(..., description="Whether threat was detected")
    sensitive_request: bool = Field(..., description="Whether sensitive data involved")
    components: Optional[List[str]] = Field(default=None, description="Optional component hints")
    restrictions: Optional[Dict[str, Any]] = Field(default=None, description="Optional restriction hints")
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "urgency": True,
                "threat": False,
                "sensitive_request": True,
                "components": ["EndpointList", "RequestBuilder", "ResponseViewer"],
                "restrictions": {"execute_requests": False, "editable_fields": ["email", "password"]}
            }
        }
    }


class UIPlanResponse(BaseModel):
    """Response schema for UI plan."""
    components: List[str] = Field(..., description="UI components to render")
    restrictions: Dict[str, Any] = Field(..., description="UI restrictions to apply")
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "components": ["EndpointList", "RequestBuilder", "ResponseViewer"],
                "restrictions": {
                    "execute_requests": False,
                    "editable_fields": ["email", "password"]
                }
            }
        }
    }


@router.post("/generate-ui-plan", response_model=UIPlanResponse)
async def generate_ui_plan_endpoint(verdict: VerdictInput):
    """
    Generate a UI plan based on the safety verdict.
    Returns components to render and restrictions to apply.
    """
    try:
        ui_plan = generate_ui_plan({
            "urgency": verdict.urgency,
            "threat": verdict.threat,
            "sensitive_request": verdict.sensitive_request
        })
        return UIPlanResponse(**ui_plan)
    except Exception as e:
        print(f"Error in generate_ui_plan: {e}")
        return UIPlanResponse(**get_conservative_ui_plan())
