import { inject, Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable } from "rxjs";
import { DecisionSubmitRequest, DecisionResponse, HealthResponse } from "./contracts";

@Injectable({ providedIn: "root" })
export class PolicyPulseService {
  private readonly http = inject(HttpClient);
  private readonly baseUrl = "/api";

  health(): Observable<HealthResponse> {
    return this.http.get<HealthResponse>(`${this.baseUrl}/ops/health`);
  }

  submitDecision(payload: DecisionSubmitRequest): Observable<DecisionResponse> {
    return this.http.post<DecisionResponse>(`${this.baseUrl}/decisions/submit`, payload);
  }
}
