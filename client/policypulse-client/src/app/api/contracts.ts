export interface DecisionSubmitRequest {
  applicant_id: string;
  product: string;
  features: Record<string, number | string | boolean>;
}

export interface ProvenanceRecord {
  model_version: string;
  prompt_id?: string | null;
  prompt_version?: string | null;
  retrieval_sources: { id?: string; title?: string; uri?: string }[];
  confidence: number;
  explanation: Record<string, unknown>;
  created_at: string;
}

export interface DecisionResponse {
  decision_id: string;
  product: string;
  applicant_id: string;
  outcome: "approve" | "review" | "reject";
  reason_codes: string[];
  provenance: ProvenanceRecord;
  created_at: string;
}

export interface HealthResponse {
  service: string;
  database: boolean;
  redis: boolean;
}
