# SCENARIO: Conflicting Metrics Across Internal Teams

> **The Challenge:** Three teams generated wildly different figures for the exact same metric in the same quarter—Finance reports **2.1%**, Marketing reports **3.4%**, and Network Operations reports **5.8%**.

---

## 🔍 Diagnosis: Metric Definition & Scope Mismatch

The root cause of multi-departmental metric divergence is almost never a math error. Instead, each department is measuring a **different scope, timeline, or underlying event** based on their unique operational definitions of what constitutes a "lost customer."

### Key Red Flags to Check First:

* **Revenue Churn vs. Customer Churn:** Finance typically tracks revenue/MRR loss or contract cancellations, whereas operational teams track active usage or technical disconnects.
* **Date & Boundary Criteria:** Differences in accounting cutoffs (e.g., invoice unpaid for 30 vs. 90 days) versus physical hardware deactivations or marketing subscription drops.

---

## 🛠️ Reconciliation Strategies (Before the Board Meeting)

Before attempting to force a single number, audit the underlying definitions and reconcile the discrepancies using these steps:

### 1. Audit Departmental Definitions

* **Finance (2.1%): Likely Net Involuntary or Contracting Churn.** Finance usually measures formal contract terminations or net dollar churn, often excluding users in grace periods or pending payment retries.
* **Marketing (3.4%): Likely Voluntary User Churn.** Marketing generally tracks active account cancellations, unsubscribes, or user-initiated churn, excluding non-paying delinquent accounts.
* **Network Operations (5.8%): Likely Inactive/Technical Churn.** Ops typically monitors signal drop-offs, zero-usage accounts, or hardware deactivations, catching inactive users long before Finance officially writes off the contract.

### 2. Establish a Single Source of Truth (SSOT)

* **Canonical Definition Map:** Document the exact SQL criteria and business rules behind each team's metric to map out precisely where the numbers diverge.
* **Unified Metrics Dictionary:** Define a standardized metric name for each variation (e.g., *Logo Churn*, *Revenue Churn*, and *Active Usage Churn*) so the board understands the distinction.

### 3. Board Presentation Alignment

* **Lead with Revenue Churn:** Present the Finance number (2.1%) as the primary financial benchmark, as it directly impacts official reporting and revenue.
* **Contextualize Operational Insights:** Frame the higher numbers from Marketing and Ops as leading operational indicators that reflect user engagement and future financial risk rather than contradictory data.