# Telecom OSS/BSS — Course Notes

Source: Etude LMS, *Telecom OSS BSS* course (course 14), lessons 199–261.
These notes cover every lesson from the start of the course through the
current unlock point (79% complete, lesson 261 — end of "eTOM Level 0").
Sections are organized by the course's own module structure, in viewing
order, with each lesson's key concepts captured from its on-screen slide.

## Contents
1. [Introduction](#module-1-introduction)
2. [A Generic Process Flow for a Service & its Basic Building Blocks](#module-2-a-generic-process-flow-for-a-service--its-basic-building-blocks)
3. [Evolution and Architecture of Mobile Communication Systems](#module-3-evolution-and-architecture-of-mobile-communication-systems)
4. [Charging and Billing in 2G GSM Network](#module-4-charging-and-billing-in-2g-gsm-network)
5. [Charging and Billing in 3G and 4G LTE Network](#module-5-charging-and-billing-in-3g-and-4g-lte-network)
6. [Charging and Billing in 5G Network](#module-6-charging-and-billing-in-5g-network)
7. [Interconnect and its Billing](#module-7-interconnect-and-its-billing)
8. [Roaming and its Billing](#module-8-roaming-and-its-billing)
9. [TMN Model](#module-9-tmn-model)
10. [Enhanced Telecom Operations Map (eTOM)](#module-10-enhanced-telecom-operations-map-etom)
11. [Glossary of Acronyms](#glossary-of-acronyms)

---

## Module 1: Introduction

### 1.1 Communication Service Provider (CSP)
A **CSP** is a company that offers telecommunication services to end users:
- Voice
- Data
- Text
- Video, etc.

Two kinds of CSP:
- **Network Operator** — owns its own network infrastructure (towers, core network, etc.).
- **Virtual Network Operator (MVNO)** — does **not** own network infrastructure; it acquires the capacity it needs from other telecom carriers (wholesale) and resells it under its own brand.

### 1.2 Telecommunication Evolution → Support Systems
- A CSP provides various **end-to-end** telecommunication services.
- Before the 1970s, most support activities in a telecom network were done **manually**: taking orders, provisioning services, billing, maintaining the network, etc.
- Over time, computer systems and software applications were created to **automate** these activities — this is the origin of what became OSS and BSS.

### 1.3 The Bigger Picture: Business Support System (BSS)
BSS covers the **customer-facing activities** of a CSP:
- **Product Catalog** — prepaid plans, postpaid plans, international roaming plans
- **Customer Relationship Management (CRM)** — registration & lead generation
- **Order Management** — sourcing subscriber data into different systems for service activation
- **Revenue Management** — charging, billing

In the overall stack: **BSS → OSS → Network (5G, 4G, DSL, or PSTN, etc.)**

### 1.4 The Bigger Picture: Operation Support System (OSS)
OSS covers the **network-facing activities** of a CSP:
- **Service Provisioning**
  - Service delivery & fulfillment — network inventory, activation
  - Service assurance — customer care
- **Network Management System**
  - Monitor network
  - Manage faults

### 1.5 Summarizing the importance of OSS & BSS
A simple mental model: the CSP's **Infrastructure** feeds up through **Infrastructure Management** into the combined **OSS/BSS** layer; OSS/BSS in turn **delivers services** and **manages the service and business** down to the **Customer**, and also handles **Customer Management** directly with the customer. In short — OSS/BSS is the layer that sits between the raw network infrastructure and the customer, translating infrastructure capability into sellable, supportable, billable services.

### 1.6 Advantages of Automating OSS/BSS
- Reduced time for service creation
- Reduced Operation Cost
- Increased Operational Efficiency
- Subscriber Retention (via improved customer care)
- Improved Return on Investment (ROI)

---

## Module 2: A Generic Process Flow for a Service & its Basic Building Blocks

### 2.1 The Generic Flow
The standard chain of blocks for delivering any telecom service:

```
Product Catalog ⇄ CRM ⇄ Order Management ⇄ Provisioning & Activation → Network
                              ⇅                        ⇅
                        Inventory Management ───────────┘
                                                          ↓
                                            Charging System → Billing
```

- **Product Catalog** — BSS. The definitive list of sellable plans/offers.
- **CRM** — BSS. Manages the customer relationship.
- **Order Management** — BSS. Validates and processes the order.
- **Inventory Management** — checks available network resources.
- **Provisioning & Activation** — OSS. Actually turns the service on in the network.
- **Network** — the live 5G/4G/DSL/PSTN infrastructure.
- **Charging System → Billing** — converts network usage into a customer invoice.

### 2.2 Customer Relationship Management (CRM)
CRM is the **process by which a business administers its interactions with customers**. Channels of interaction include:
- Call center
- Company portal
- SMS
- E-mail
- Live chat
- Social Media
- Company store

### 2.3 Registration of Customer
**Registration** is the process of registering a new customer in the CSP's network. Typical steps:
1. **Customer Information Collection** — name, national identification number, contact information
2. **Identity Verification**
3. **Account Creation** — creates a service identity
4. **Order the selected Service/Plan**
5. **Billing Information Collection** — e.g., payment method

### 2.4 Order Management Block & Activation of Service
Order Management performs four steps:
1. Validate the order for completeness and correctness.
2. Determine the steps for provisioning the requested service.
3. Check network inventory for sufficient resources to fulfill the service request.
4. Do any manual installation and setup, if required, by interacting with the workforce management module.

### 2.5 Charging & Billing (transition)
This block closes the loop of the generic flow: once a service is active and being used on the **Network**, the **Charging System** captures usage and **Billing** turns it into an invoice. This is the on-ramp into the next module, which goes deep into exactly how charging and billing work across each network generation.

---

## Module 3: Evolution and Architecture of Mobile Communication Systems

### 3.1 Evolution of Mobile Communication Systems
| Generation | Name | Key characteristics |
|---|---|---|
| 1G | AMPS | Analog system, no digital data |
| 2G | GSM | Digital system, low bitrate data up to 150 kbps (GPRS/EDGE) |
| 3G | UMTS | Broadband data, up to 20 Mbps (HSPA+) |
| 4G | LTE | All-IP systems, low hundreds of Mbps (LTE Advanced) |
| 5G | — | High hundreds of Mbps |

### 3.2 The Three Main Components of a Mobile Network
Every cellular mobile network has three main components:
1. **Mobile Station (MS)** — the device + SIM. The SIM contains the **IMSI** (International Mobile Subscriber Identity).
2. **Radio Access Network (RAN)** — where the MS connects to the mobile network (also just called the Access Network).
3. **Core Network (CN)** — overall control of the MS: call establishment and routing. The CN connects onward to the **External Network** (e.g., PSTN, Internet).

### 3.3 Backhaul Transport Network
The **backhaul** connects the RAN with the CN. It can be implemented as:
- Microwave link
- Electrical cable
- Optical fiber cable — often using a **DWDM** (Dense Wavelength Division Multiplexing) system for capacity

(MS = **ME**, Mobile Equipment, + **SIM**.)

---

## Module 4: Charging and Billing in 2G GSM Network

### 4.1 Introduction to Charging & Billing in 2G GSM
A brief overview of GSM architecture is necessary to understand charging/billing flows. The module covers charging architectures for both **offline charging** and **online charging**. The detailed internal working of the GSM network itself is out of scope — only what's relevant to charging/billing is discussed.

### 4.2 GSM Architecture Overview
- **BTS (Base Transceiver System / basestation)** — the MS connects to the BTS over the wireless channel.
- **BSC (Base Station Controller)** — routes an incoming call to the MSC.
- **MSC (Mobile Switching Center)** — the core switch; connects to **GMSC (Gateway MSC)**, which connects to the **PSTN**.
- MSC is linked to three databases: **VLR** (Visitor Location Register), **HLR** (Home Location Register), **AUC** (Authentication Center).
- So: **RAN = BTS + BSC**, **CN = MSC + GMSC + VLR/HLR/AUC**.

### 4.3 Authentication Procedure
A procedure to verify the identity of a subscriber:
- The SIM holds a secret key **Ki**. The network sends a random challenge **RAND**.
- Both the SIM (via its Authentication Algorithm) and the network's **AUC** independently compute a **Signed Response (SRES)** from Ki + RAND.
- The network compares **SRES** (from the handset) against **SRES\*** (computed at the network). If they match, the subscriber is authenticated.

### 4.4 Call Flow of a Post-paid Call
1. MS sends the dialed (called party) number to BTS → BSC → MSC.
2. MSC checks if the MS is allowed to make the call (authentication).
3. MSC checks the called party number, and the call is routed onward through GMSC to the PSTN.
4. ... (signaling continues between MSC, VLR/HLR/AUC, GMSC)
5. **At the end of the call**, the call details are captured as a **Call Detail Record (CDR)**, generated in the MSC.

### 4.5 Call Detail Record (CDR)
A CDR is generated in the **MSC** at the end of a call. A typical CDR captures:
- Calling party number
- Called party number
- Call start time
- Call end time
- Call duration (End Time − Start Time)
- Call Identifier

### 4.6 Offline Charging System — Mediation
**Offline Charging** allows a subscriber to consume a service **without requiring an upfront balance** (i.e., the postpaid model — pay after use).

**Mediation**: different MSCs may generate CDRs in different (often binary/ASN) formats. Mediation converts all of these CDR files into a **common file format** (ASCII), ready for rating.

Flow so far: **Generated Raw CDRs → Mediation → CDR Rating → Billing** (with a **Price Plan** reference feeding into CDR Rating).

### 4.7 Offline Charging System — CDR Rating
**CDR Rating** determines the cost of a call captured in a CDR, using the Price Plan reference:
- **Time-based** (Peak, off-peak, etc.)
- **Destination-based** (Local, international, etc.)

Rating procedure:
1. Read the CDR.
2. Check calling party number, called party number, time of call.
3. Check the applicable call rate.
4. Multiply call duration by the rate.

### 4.8 Offline Charging System — Billing
**Billing** transforms rated CDRs into invoices:
- Collection of all rated calls over the past 30 days.
- Apply any promotions and discounts.
- Apply taxes and credits.
- Format the bill as an invoice in the desired file format.

Example invoice:
| Item | Amount |
|---|---|
| Monthly Fee | $12.00 |
| Usage | $5.50 |
| **Total** | **$17.50** |
| Taxes (10%) | $1.75 |
| **Grand Total** | **$19.25** |

### 4.9 Architecture for Pre-paid Charging in GSM
Prepaid charging is built on an Intelligent Network (IN) style architecture:
- **SSP (Service Switching Point)** — co-located with the MSC; triggers the prepaid service.
- **SCP (Service Control Point)** — contains and executes the service logic for prepaid billing.
- SCP connects to a **Rating Engine** and to an **SMP**, which connects to the **Voucher Management System** (for recharge/top-up vouchers).

### 4.10 Call Flow for a Pre-paid Call
1. A prepaid subscriber makes a call — it arrives at the MSC; the MSC looks at the calling party number.
2. MSC/SSP **triggers the prepaid platform** — sends a message (with calling & called party number) to the prepaid platform.
3. The message passes to the **Rating Engine** via the SCP.
4. The Rating Engine **queries the database for the calling party's balance**.
5. **The call is rejected if the balance is insufficient.**

> Key difference from postpaid: prepaid checks and reserves credit **before** the call is connected; postpaid just generates a CDR to bill **after** the call.

### 4.11 2G GPRS/EDGE Architecture
Adds packet-switched data capability on top of the GSM voice architecture:
- **SGSN (Serving GPRS Support Node)** — acts like the MSC, but for data service; adds packet-switched capability.
- **GGSN (Gateway GPRS Support Node)** — appears as a router to external networks (e.g. the Internet); allocates an IP address to the MS.
- CDRs are generated in **both**:
  - **SGSN** — based upon data **usage time**
  - **GGSN** — based upon data **volume** used

(GPRS = General Packet Radio Service; EDGE = Enhanced Data for GSM.)

---

## Module 5: Charging and Billing in 3G and 4G LTE Network

### 5.1 3G UMTS Architecture & Charging
UMTS = Universal Mobile Telecommunications System.
- Uses the **same Core Network** as 2G GPRS/EDGE.
- RAN terminology changes: **BSC → RNC** (Radio Network Controller), **BTS → NodeB**.
- Initially, 3G reused the **same charging architecture as 2G**.
- New data services (VoIP, file download, video streaming) increased the focus on **Quality of Service (QoS)**:
  - Data rate (guaranteed or non-guaranteed)
  - Latency
  - Priority

### 5.2 Policy and Charging Control (PCC)
- PCC architecture is defined by **3GPP**.
- Originally proposed for 3G, but mainly deployed starting with **4G LTE**.
- Enables **precise control of individual packet services**, covering both:
  - Quality of Service (QoS)
  - Charging
- Works with both **online** and **offline** charging.

### 5.3 4G LTE Architecture with PCC
Node name mapping from older generations to LTE:
| Older node | LTE equivalent |
|---|---|
| SGSN | Serving Gateway (S-GW) |
| GGSN | PDN Gateway (P-GW) |
| HLR | Home Subscriber Server (HSS) |
| VLR | Mobility Management Entity (MME) |

New PCC-specific elements:
- **PCRF** (Policy and Charging Rules Function) — decides policy/charging rules.
- **PCEF** (Policy and Charging Enforcement Function) — lives inside the **P-GW**; enforces the rules.
- **OCS** (Online Charging System) and **OFCS** (Offline Charging System) — hang off the PCEF.

Path: handset → **eNodeB** → **S-GW** → **P-GW** (with PCEF) → Internet, inside an **EPS Bearer**.

### 5.4 Post-paid Call Flow in 4G LTE
1. MS/UE sends a data connection request to eNodeB → MME.
2. MME performs authentication.
3. MME requests data access to S-GW → P-GW.
4. P-GW queries the **PCRF** about the MS's data session establishment (to get the policy/QoS rule).
5. The **PCEF** (also called the **Charging Trigger Function, CTF**) then monitors service usage and generates charging events.

### 5.5 3GPP Offline Charging System
The **CTF** (inside the PCEF) forwards charging events to the **OFCS** for postpaid/offline billing — conceptually the same offline charging idea as in 2G/3G, just re-architected around PCC.

### 5.6 CDR Rerating
**CDR rerating** is the process of **recalculating the charges** for CDRs that a telecom network has already generated.

Why rerating may be required:
- Rates were wrongly configured.
- New rates need to be applied retroactively from a backdate.

Rerating procedure (for a data call):
1. Read the CDR — check calling party number, called party number, check data usage.
2. Multiply data volume usage by the (corrected) tariff/rate → **Rerate CDR**.
3. **Insert CDR** into the **Rated CDR database**.

### 5.7 Pre-paid Call Flow in 4G LTE
- The **PCEF/CTF** talks to the **OCS (Online Charging System)** for credit units, and receives information from the OCS about available credit units.
- It then **measures and reports the user's usage** against that credit in real time.
- **If credit runs low → PCEF/CTF signals the PCRF**, and the **PCRF terminates the session**.
- The OCS also sends a **credit limit report** to the PCRF.

### 5.8 Account Balance Management Function (ABMF)
Part of the **Online Charging System**, alongside the Rating Function. The **ABMF** stores and manages the subscriber's prepaid account balance (credit units).

### 5.9 Rating Function (RF)
Determines the **monetary cost of credit units**, based on:
- Data volume
- Session/connection time
- Service events
- Also contains provisions for things like **free minutes**.

Sits within the Online Charging System, alongside ABMF, under the **OCF**.

### 5.10 Online Charging Function (OCF) — Sub-types
The OCF has two sub-types:
1. **SBCF — Session Based Charging Function**: used for **real-time charging of a voice or data call** (i.e., something with duration/session).
2. **EBCF — Event-Based Charging Function**: charges are based on the occurrence of discrete **events** — typical events: SMS, MMS, purchase of content (application, game, video on demand, etc.).

Putting it together, the **Online Charging System** = **ABMF + RF + SBCF + EBCF**, sitting (within OSS/BSS) between the **Billing System** above and the network-side **CTF** below.

### 5.11 Online Charging Scenarios
Three types of online charging scenario:
1. **Immediate Event Charging (IEC)** — e.g., SMS.
2. **Event Charging with Unit Reservation (ECUR)** — e.g., MMS that can support an image/video attachment.
3. **Session Charging with Unit Reservation (SCUR)** — e.g., voice calls or data browsing.

#### 5.11.1 Immediate Event Charging (IEC) — detailed flow
1. MS → CTF: Request for resource usage.
2. CTF → OCF: **Debit Units Request** (Service Key).
3. OCF: Units Determination → Rating Control → Account Control.
4. OCF → CTF: **Debit Units Response** (non-monetary units).
5. CTF → MS: Content/Service Delivery.
6. Session released.

A single debit — the unit is charged immediately after the one-off event, no reservation step.

#### 5.11.2 Event Charging with Unit Reservation (ECUR) — detailed flow
1. MS → CTF: Request for resource usage.
2. CTF → OCF: **Reserve Units Request** (Service Key).
3. OCF: Units Determination → Rating Control → Account Control → **Reservation Control**.
4. OCF → CTF: **Reserve Units Response** (non-monetary units).
5. CTF: Granted Units Supervision.
6. CTF → MS: Content/Service Delivery.
7. CTF → OCF: **Debit Units Request** (non-monetary units, actual usage).
8. OCF: Rating Control → Account Control.
9. OCF → CTF: **Debit Units Response**.
10. Session released.

Units are **reserved first**, then the actual usage is **debited afterward** — appropriate for events where the final size isn't known upfront (e.g., an MMS attachment).

#### 5.11.3 Session Charging with Unit Reservation (SCUR) — detailed flow
Same reservation pattern as ECUR, but for an ongoing **session** rather than a single event:
1. MS → CTF: Request for resource usage.
2. CTF → OCF: Reserve Units Request → Units/Rating/Account/Reservation Control → Reserve Units Response.
3. CTF: Granted Units Supervision.
4. **Session ongoing** (this reserve → supervise cycle can repeat multiple times across a long session).
5. Session released.
6. Final Debit Units Request → Rating/Account Control → Debit Units Response.

Used for continuous, metered usage (voice calls, data browsing), where units are periodically re-reserved as the session continues.

---

## Module 6: Charging and Billing in 5G Network

### 6.1 5G Architecture with Charging
Node name mapping from 4G to 5G:
| 4G node | 5G equivalent |
|---|---|
| eNodeB | gNB (next-generation NodeB) |
| MME | AMF (Access & Mobility Management Function) |
| HSS | UDM (Unified Data Management) |
| P-GW | UPF (User Plane Function) |

New 5G elements: **CHF** (Charging Function), **SMF** (Session Management Function), **PCF** (Policy Control Function), **AF** (Application Function) — all interconnected in a service-based architecture, with UDM and CHF also linked in.

5G provides data/IP connectivity to the UE as a **PDU Session**, which consists of one or more **QoS flows**.

### 6.2 Charging Function (CHF) in 5G
The CHF **supports converged charging** — it handles **both Online and Offline charging in a single function**. This **simplifies charging**: there's no longer a need to use separate systems for offline and online charging (unlike 4G's split OCS/OFCS).

### 6.3 Initial Call Flow for Charging in 5G
1. MS/UE sends a PDU session request to gNB → AMF.
2. AMF performs authentication.
3. SMF checks QoS policy with PCF.
4. PCF formulates the PCC rule.
5. PCF activates the PCC rule in the UPF, via the SMF.
6. SMF establishes the PDU session.
7. UE starts using the service.
8. UPF tracks the service usage.

### 6.4 5G Offline Charging
Offline Charging in 5G splits into the same two shapes as 4G, now unified under the CHF:
- **Event-based charging**
- **Session-based charging**

### 6.5 5G Online Charging
Online Charging in 5G uses the **same three scenarios** as 4G/LTE (now handled by the CHF):
1. Immediate Event Charging (IEC)
2. Event Charging with Unit Reservation (ECUR)
3. Session Charging with Unit Reservation (SCUR)

---

## Module 7: Interconnect and its Billing

### 7.1 What is Interconnect
**Interconnect** enables mutual traffic between **two different CSPs**. The two operators need to agree on:
- **Services** — e.g., voice call, SMS
- **Rates for services** — e.g., CSP1 → CSP2: $0.10/min, CSP2 → CSP1: $0.13/min (rates can be, and often are, **asymmetric**)

The two networks are physically joined by a **Trunk Line** between a trunk identifier on each side (e.g., T1 on CSP1, T2 on CSP2).

### 7.2 Interconnect Partners and Their Types
- **Originating Partner** — the CSP where the call is generated.
- **Termination Partner** — the CSP where the call is terminating.

### 7.3 Interconnect Billing Procedure & Settlement
**The terminating partner gets paid by the originating partner** (the network that originates the call pays the network that terminates it, for the cost of terminating/carrying that traffic).

Example: CSP1 = Origination partner, CSP2 = Termination partner. The **terminating partner's (CSP2) invoice calculation**:
1. CSP2 identifies/collects CDRs of calls originating from CSP1 (using its own trunk ID, e.g. T2).
2. Applies the agreed interconnect charges.
3. Calculates the invoice for the calls received from CSP1.
4. Sends the invoice to CSP1 for settlement.

---

## Module 8: Roaming and its Billing

### 8.1 What is Roaming
**Roaming** is the ability of a mobile subscriber to use services **outside their home network's coverage area**.

- The **IMSI** of a subscriber is **globally unique**, stored in the SIM, and used for identification during roaming.
  - IMSI structure: **MCC** (3 digits) + **MNC** (2 or 3 digits) + **MSIN**, not more than **15 digits** total.
- Roaming **requires a prior roaming agreement** between the two operators: the subscriber's **Home Mobile Network** (CSP1) and the **Visited Mobile Network** (CSP2).

### 8.2 Initial Roaming Procedure
1. The mobile subscriber is identified using their **IMSI** in the visited network.
2. The visited network checks if a roaming agreement exists, and performs authentication.
3. The visited network copies data from the home network's **HLR** into its own **VLR**.
4. The home network updates the MS's location in its **HLR**.
5. Terminology: the subscriber is called an **"Inroamer"** in the visited network, and an **"Outroamer"** in their home network.

> Generational note: 2G/3G use **HLR/VLR**; the LTE/5G equivalents are **VLR → MME → AMF** and **HLR → HSS → UDM**.

### 8.3 Call Routing in Roaming — Post-paid
Three parties are involved in routing a call to a roaming subscriber:
- **CSP A** — Home Mobile Network (holds the **HLR**)
- **CSP B** — Visited Mobile Network (holds the **VLR**)
- **CSP C** — the network of the party calling in / routing the call through to reach the roaming subscriber

### 8.4 Post-paid Billing during Roaming
1. The **visited network** collects CDRs of its Inroamers.
2. It sends these CDRs to a **Roaming Settlement System (RSS)**.
3. **Functions of the RSS**:
   - Identifies Inroamers by IMSI.
   - Rates the CDRs according to the agreed tariff.
   - Groups CDRs for a given home CSP into a **TAP (Transfer Account Procedure)** file.
   - Sends TAP files to the respective home CSPs **every week**.

### 8.5 Near Real Time Roaming Data Exchange (NRTRDE)
Problem with the weekly TAP process:
- It's **difficult to verify a roamer's credit limit** before a full week has passed.
- This creates a **possibility of fraud** (e.g., bill-shock-style abuse before the operator even knows usage is happening).

**Solution — NRTRDE**: CDRs are sent **every few hours** instead of weekly, which **reduces fraud risk** by giving the home network near-real-time visibility into roaming usage.

### 8.6 Clearing House
A **Clearing House** is a central hub that facilitates:
- Exchange of TAP files
- Conversion of TAP file formats (between operators using different systems)
- Roaming settlements
- Dispute resolution

It sits between multiple CSPs (e.g., CSP1, CSP2, CSP3, CSP4) — turning what would otherwise be N-to-N bilateral settlement relationships into a simpler hub-and-spoke model.

### 8.7 Voice Call Routing in Pre-Paid (Roaming)
Same three-party structure as the post-paid case:
- **CSP A** — Home Network (HLR)
- **CSP B** — Visited Network (VLR)
- **CSP C** — the calling/transit party's network

### 8.8 Data Call Routing during Roaming in Pre-paid
- **CSP A** — Home Network (GGSN)
- **CSP B** — Visited Network (SGSN)
- **CSP C** — transit/calling network
- Node mapping carried over from the GPRS/LTE discussion: **SGSN → S-GW**, **GGSN → P-GW** — i.e., the same legacy data nodes map onto their LTE equivalents when roaming data sessions are served over newer access technology.

---

## Module 9: TMN Model

### 9.1 Introduction to Telecommunications Management Network (TMN)
- **TMN** is a **management system for the telecom network**.
- The concept is defined in **ITU-T recommendation M.3010**.
- TMN organizes telecom management functionality into a set of **hierarchical layers**.

### 9.2 TMN Layers
From top (most abstract/business-oriented) to bottom (most concrete/physical):
1. **Business Management**
2. **Service Management**
3. **Network Management**
4. **Element Management**
5. **Network Element** (the physical/logical equipment itself)

### 9.3 Fault, Configuration, Accounting, Performance, Security (FCAPS)
- Defined in **ITU-T recommendation M.3400**.
- **FCAPS** is a set of management functions **associated with each TMN layer** (i.e., it's a cross-cutting framework applied at every layer):
  - **Fault** — identify & isolate faults, log & correct faults, predict faults
  - **Configuration** — configuration of Network Elements (NE), plan network expansion
  - **Accounting** — billing management, usage statistics
  - **Performance** — utilisation monitoring, QoS management, resource provisioning
  - **Security** — authorisation, authentication, encryption

### 9.4 TMN Model Implementation in Mobile Networks
A practical layered implementation:
- Bottom: **RAN, Transport Network, Core Network, Application Servers** (the Network Elements).
- Each domain is monitored/managed by its own **Element Management System (EMS1–EMS4)**.
- All the EMSs feed up, via **Consolidation**, into a single **Network Management System (NMS)**.
- The NMS in turn drives **FCAPS**, **Operation Reports**, and **Network Planning** at the top.

### 9.5 EMS – NMS – NOC
**Elements Management System (EMS)** — used to manage and monitor **specific network elements** within one domain:
- Transport network
- Radio Access Network
- Core Network

EMS responsibilities include:
- Logging & backup (e.g., Key Performance Indicators, alarm data)
- Detailed configuration of individual Network Elements (NEs)

(The **NOC**, Network Operations Center, is the operational team that consumes the NMS/EMS outputs to actually run day-to-day network operations.)

---

## Module 10: Enhanced Telecom Operations Map (eTOM)

### 10.1 From TMN to TOM
- The **TMN model isn't elaborate enough** — it does not map telecom *processes* onto its management layers (it's organized around technical layers, not business processes).
- TMN was therefore expanded into the **Telecommunications Operations Map (TOM)** model, which overlays TMN's layers with actual business process groupings:
  - **Customer** (top) interacts via **Customer Interface Management Processes**.
  - Below that, three parallel process groupings:
    - **Customer Care Processes** — Sales, Order Handling, Problem Handling, Customer QoS Management, Invoicing & Collections
    - **Service Development and Operations Processes** — Service Planning & Development, Service Configuration, Service Problem Management, Service Quality Management, Rating & Discounting
    - **Network and Systems Management Processes** — Network Planning & Development, Network Provisioning, Network Inventory Management, Network Maintenance & Restoration, Network Data Management
  - All of the above are supported end-to-end by **Network Element Management Processes** at the base, and by an **Information Systems Management Processes** pillar running alongside the whole stack.

### 10.2 From TOM to eTOM
TOM was further evolved into **eTOM** (enhanced Telecom Operations Map) — broadening the process map beyond pure operations to cover the **whole enterprise** (see Level 0, next).

### 10.3 eTOM Level 0
The highest-level (most abstract) view of eTOM:
- **Customer** sits at the top of the model.
- Two major process areas sit below the customer:
  - **Strategy, Infrastructure & Product (SIP)** — covers planning and lifecycle management, associated with the **development and delivery** of services/infrastructure.
  - **Operations** — covers the **core of day-to-day operational management**.
- Below both of these: **Enterprise Management** — concerned with managing the enterprise as a whole (cross-cutting corporate functions, e.g., HR, finance, strategy — not telecom-specific).

**Why the SIP / Operations split matters**: eTOM explicitly differentiates **SIP** from **Operations** processes because **SIP processes do not directly support the customer** — they're about planning, building, and developing the capability — whereas **Operations** processes are what actually run and deliver the live, customer-facing service day to day.

---

## What's not yet covered

The course is unlocked through lesson 261 (79% complete) at the time of writing. The remaining modules — not yet available to capture — are:
- **eTOM Process Groupings, eTOM Enterprise Management, eTOM Business Processes** (rest of Module 10)
- **Examples of eTOM Business Flows** (Request-to-Answer and Usage-to-Payment process flow walkthroughs)
- **ITIL and eTOM** (what ITIL is, eTOM vs. ITIL, ITIL lifecycle stages, aligning ITIL with eTOM)

These can be added to this document once more of the course is unlocked.

---

## Glossary of Acronyms

| Acronym | Meaning |
|---|---|
| CSP | Communication Service Provider |
| MVNO | Virtual Network Operator (no owned infrastructure) |
| BSS / OSS | Business / Operation Support System |
| CRM | Customer Relationship Management |
| MS / RAN / CN | Mobile Station / Radio Access Network / Core Network |
| BTS / BSC | Base Transceiver Station / Base Station Controller |
| MSC / GMSC | (Gateway) Mobile Switching Center |
| VLR / HLR / AUC | Visitor / Home Location Register / Authentication Center |
| CDR | Call Detail Record |
| SSP / SCP / STP | Service Switching / Control Point, Signal Transfer Point |
| SGSN / GGSN | (Gateway) GPRS Support Node |
| GPRS / EDGE | General Packet Radio Service / Enhanced Data for GSM |
| UMTS / RNC | Universal Mobile Telecom. System / Radio Network Controller |
| PCC / PCRF / PCEF | Policy & Charging Control / Rules Function / Enforcement Function |
| OCS / OFCS | Online / Offline Charging System |
| S-GW / P-GW | Serving / PDN Gateway (4G) |
| HSS / MME | Home Subscriber Server / Mobility Management Entity |
| EPS | Evolved Packet System (4G bearer) |
| CTF | Charging Trigger Function |
| ABMF / RF | Account Balance Management Function / Rating Function |
| OCF / SBCF / EBCF | Online Charging Function / Session- / Event-Based variants |
| IEC / ECUR / SCUR | Immediate / Event- / Session-based charging with reservation |
| gNB / AMF / UDM / UPF | 5G base station / mobility, data, user-plane functions |
| CHF / SMF / PCF / AF | 5G Charging / Session Mgmt / Policy Control / Application Function |
| PDU | Protocol Data Unit (5G session type) |
| IMSI / MCC / MNC / MSIN | Int'l Mobile Subscriber Identity and its parts |
| TAP | Transfer Account Procedure (roaming billing file) |
| NRTRDE | Near Real Time Roaming Data Exchange |
| TMN | Telecommunications Management Network |
| FCAPS | Fault, Configuration, Accounting, Performance, Security |
| EMS / NMS / NOC | Element / Network Management System, Network Operations Center |
| TOM / eTOM | (enhanced) Telecom Operations Map |
| SIP (eTOM context) | Strategy, Infrastructure & Product — *not* Session Initiation Protocol |
