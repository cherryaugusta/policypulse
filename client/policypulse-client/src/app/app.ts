import { CommonModule } from "@angular/common";
import { Component, inject, signal } from "@angular/core";
import { PolicyPulseService } from "./api/policypulse.service";
import { DecisionResponse, HealthResponse } from "./api/contracts";

@Component({
  selector: "app-root",
  imports: [CommonModule],
  templateUrl: "./app.html",
  styleUrl: "./app.scss",
})
export class App {
  private readonly api = inject(PolicyPulseService);

  health = signal<HealthResponse | null>(null);
  lastDecision = signal<DecisionResponse | null>(null);
  error = signal<string | null>(null);

  checkHealth() {
    this.error.set(null);
    this.api.health().subscribe({
      next: (res) => this.health.set(res),
      error: (e) => this.error.set(String(e?.message ?? e)),
    });
  }

  submitDemoDecision() {
    this.error.set(null);
    this.api
      .submitDecision({
        applicant_id: "applicant-token-123",
        product: "loan_precheck",
        features: { income: 50000, age: 30, country: "GB" },
      })
      .subscribe({
        next: (res) => this.lastDecision.set(res),
        error: (e) => this.error.set(String(e?.message ?? e)),
      });
  }
}
