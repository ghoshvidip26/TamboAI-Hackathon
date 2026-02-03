-- SQL Schema for Policy-Aware AI API Explorer
-- Tables: api_specs, safety_verdicts, policies

-- API Specifications table
CREATE TABLE IF NOT EXISTS api_specs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT,
    spec_text TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Safety Verdicts table (audit log)
CREATE TABLE IF NOT EXISTS safety_verdicts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    api_spec_id UUID REFERENCES api_specs(id),
    user_intent TEXT,
    verdict_json JSONB,
    ui_contract_json JSONB,
    risk_score FLOAT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Policies table
CREATE TABLE IF NOT EXISTS policies (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    policy_name TEXT,
    policy_json JSONB,
    version INT,
    active BOOLEAN DEFAULT true,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
