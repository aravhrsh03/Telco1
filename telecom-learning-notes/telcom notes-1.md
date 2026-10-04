# Telecom Infra: Part 1 — Course Notes

Source: Etude LMS, *Telecom Infra: Part 1* course (course 8), lessons 18 onward (course 100% complete). Sections follow the course's own module structure in viewing order.

A few individual lessons had broken video playback on the platform (noted inline below) — for those, the notes rely on standard, well-known telecom engineering definitions rather than the course's own slide content.

## Contents
1. [Introduction](#module-1-introduction)
2. [The Evolution](#module-2-the-evolution)
3. [Back to Basics — PSTN](#module-3-back-to-basics--pstn)
4. [Internet and its Architecture](#module-4-internet-and-its-architecture)
5. [IP Network](#module-5-ip-network)
6. [VOIP](#module-6-voip)
7. [IMS — Deep Dive](#module-7-ims-ip-multimedia-subsystem--deep-dive)
8. [Communication & Access Fundamentals](#module-8-communication--access-fundamentals)
9. [Glossary of Acronyms](#glossary-of-acronyms)

---

## Module 1: Introduction

### 1.1 About the Course
Title/branding slide introducing the course (Telecom Essentials) — no separate technical content.

### 1.2 Evolution of Telecom Technologies
*(Video did not load on the platform at time of writing.)* Standard generational timeline: 1G (analog, AMPS) → 2G (digital, GSM) → 2.5G (GPRS/EDGE, packet data added) → 3G (UMTS, broadband data) → 4G (LTE, all-IP) → 5G (NR, massive bandwidth/low latency) → (6G, emerging).

### 1.3 Standards and Specifications
- **ITU** defines the overall technology concepts and performance expectations for each generation (e.g., the minimum capabilities a network must meet to be called "4G" or "5G").
- **3GPP** develops the detailed technical reports/specifications that networks and equipment actually implement to meet those ITU-defined concepts.
- In short: ITU sets the target: 3GPP writes the engineering spec to hit it.

### 1.4 Architecture Overview
Introduces "Telecom Network Architecture" as the umbrella topic for the rest of the course — the mobile network stack from the handset through the mast, transport, and core network, which is unpacked lesson-by-lesson through the rest of this module and the next.

### 1.5 Telecom Mast: Part 1 — "The Telecom Mast"
- The mast is part of the **RAN** (radio access network) — it's the entity interfacing the user and enabling communication between users and the network.
- Physically: **GSM antennas** sit on top of the mast; the **base station** equipment sits below/underneath it.
- The base station processes the signal and passes it to the antennas; each antenna covers a specific geographical area (a **cell**). More antennas = more coverage.
- Mast type varies with the coverage needed: a smaller pole covers a smaller area; a taller tower covers a larger geographical area — same basic purpose either way.
- Mast placement must be planned geographically to balance coverage without excessive overlap or gaps; busier areas may need more base stations.
- A single mast can host **multiple operators**, each with its own set of antennas (cells) on the same physical structure (tower sharing).

### 1.6 Telecom Mast: Part 2
*(Not captured in detail — a continuation of the Part 1 mast topic.)*

### 1.7 Base Station - Live
A real-world field photo/video of an actual installed telecom mast (antennas mounted on a pole, base-station equipment housed in a cabinet at ground level) — a live example grounding the Part 1/Part 2 concepts in a real site.

### 1.8 Transport and Core Network
- The **Transport Network** carries information between transmitter and receiver — the source on which information flows is called the **"Transport Media."**
- Transport media types:
  - Microwave transmission (point-to-point radio links between towers)
  - Communication satellites
  - Fiber optics
- Example chain shown: **MSC ↔ BSC** over fiber, **BSC ↔ Cell Site** over fiber, **Cell Site ↔ Cell Site** over microwave links, and **Cell Site ↔ handset** over the air interface (RF spectrum).

---

## Module 2: The Evolution

### 2.1 The Overview
A roadmap/table-of-contents lesson for this module: previews the 2G→3G evolution, 4.5G, 3GPP Release 15, 5G architecture, IMS, and the ITU-defined 4G/5G capability targets covered in the lessons that follow.

### 2.2 3G UMTS — Architecture Overview
**3G-UMTS (Release 4 onward)** uses a **split architecture** (GSM + UMTS):
- **GERAN** (GSM/EDGE Radio Access Network): BTS, BSC/PCU
- **UTRAN** (UMTS Terrestrial RAN): NodeB, RNC
- **Core Network — CS Domain** (Circuit Switched, for voice): MSC, MGW, GMSC → PSTN/ISDN. Release 4's key change: control and user planes are **disaggregated**, handled separately by the MSC (control) and MGW (user/media).
- **Core Network — PS Domain** (Packet Switched, for data): SGSN, GGSN → IP networks
- Shared resources: HLR, VLR, AuC
- Key terms: MS (Mobile Station), BTS (Base Transceiver Station), PCU (Packet Control Unit), MSC (Mobile Switching Centre), GMSC (Gateway MSC), SGSN (Serving GPRS Support Node), HLR (Home Location Register), VLR (Visitor Location Register)

### 2.3 IMS (overview, within the Evolution timeline)
- **IMS (IP Multimedia Subsystem)** is an **architecture, not a protocol** — it supports VoIP and a broad range of IP-based services.
- An open architecture primarily developed by **3GPP**.
- Works across both fixed and wireless networks, enabling **fixed/wireless convergence** (e.g., mobility between a DSL connection and a mobile network).
- Positioned as the evolution step after Softswitch: **PSTN Switch → Softswitch → IMS**.
- *(IMS is covered in full depth in its own dedicated module later in the course — see Module 7.)*

### 2.4 4G Overview — Core Network (EPC)
**4G Core Network (Evolved Packet Core, EPC)**, standalone/non-roaming case:
- **E-UTRAN**: handles RRM (Radio Resource Management), access, the user/control plane split, and connection setup between the handset and the eNodeB.
- **MME** (Mobility Management Entity): NAS signaling, registration, access authentication, mobility management control.
- **HSS** (Home Subscriber Server): user subscription data, authentication credentials, updates the location register.
- **SGW** (Serving Gateway): packet routing & forwarding, transport-level packet marking (uplink/downlink), local mobility anchor for inter-eNodeB handover.
- **PCRF** (Policy and Charging Rules Function): records billing, policy rules for data rates/QoS/quota.
- **PGW** (PDN Gateway): QoS handling, UE IP address allocation, mobility anchoring.
- Diagram distinguishes the **Control Plane** from the **User Plane** throughout the EPC.

### 2.5 5G Evolution — 5G Core (Reference Point Representation)
- 5G's control plane splits into two dedicated nodes: **AMF** (Access and Mobility Management Function) and **SMF** (Session Management Function) — a deliberate separation of the user plane from the signaling plane (**CUPS**, Control and User Plane Separation).
- This split underpins **network slicing**: different sessions/services (e.g., eMBB vs. URLLC) can have different QoS/QCI requirements served by logically separate "slices" of the same physical network.
- **Cloud and virtualization** (NFV-style thinking) let any hardware run any network function simply by changing software, enabling flexible "self-service agility."
- **Edge computing** moves content closer to the user (e.g., caching popular video-on-demand content at local edge servers) to shorten the path for latency-critical applications.
- Key 5G Core functions in the reference-point diagram: NSSAAF, NSSF (Network Slice Selection Function), AUSF (Authentication Server Function), UDM (Unified Data Management), AMF, SMF, PCF (Policy Control Function), AF (Application Function), with UE–RAN–UPF–DN forming the user-plane path and numbered reference points (N1, N2, N3, N4, N6, etc.) connecting the control-plane functions.

### 2.6 4G to 6G — ITU Capability Targets
The ITU-R defines key capability targets per generation (under the umbrella term **IMT**, International Mobile Telecommunications):
- Peak data rate: 1 Gbps (downlink)
- User data rate: 10 Mbps
- Latency: 10 ms
- Mobility: up to 350 km/h
- Connection density: 0.1 million devices/km²
- Area traffic capacity: 0.1 Mbps/m²

("IMT Advanced" corresponds to 4G-class targets; "IMT-2020" corresponds to 5G-class targets, each generation raising these numbers substantially.)

---

## Module 3: Back to Basics — PSTN

### 3.1 Introduction to PSTN
The **Public Switched Telephone Network (PSTN)** is a telecommunications network that lets subscribers at different sites communicate by voice. A voice call requires a dedicated voice circuit/channel — this is **circuit switching**. Basic picture: Central Office (local exchange) ↔ PSTN ↔ Central Office, with copper wire to each subscriber's phone.

### 3.2 PSTN Exchange Hierarchy
Exchanges are arranged hierarchically to route calls efficiently:
**Local Exchange → Tandem Exchange → Transit Exchange → International Gateway Exchange.**
- Local exchanges within a city connect up to a tandem exchange.
- Tandem exchanges connect to a transit exchange for routing calls *between* cities.
- International Gateway Exchanges connect transit exchanges across *countries*, enabling international calling — highlighting how interconnected these layers are.

### 3.3 Block Diagram of an Exchange
Inside a local exchange / central office: subscriber lines terminate on a **Line Card**; the **Switch Fabric** is the central switching matrix that connects any input to any output; a **Trunk Card** connects outward to another exchange over trunk lines; a **Signaling & Control** module underlies and coordinates the switch fabric to set up, maintain, and tear down each call.

### 3.4 Local Loop
The **local loop** is the last-mile copper connection from a subscriber's phone to the exchange:
**Telephone (speaker, hook switch, microphone) → copper wire → Distribution Point → copper wire → Main Distribution Frame (MDF) → Exchange.**

### 3.5 On-Hook / Off-Hook Signal
Signaling state is carried on the same copper pair:
- **On-hook** (idle): the Ring wire carries −48V DC from a battery at the exchange; the TIP wire is an open circuit.
- Going **off-hook** closes the loop, which the exchange detects as the start of a call attempt (dial tone follows).

### 3.6 Signaling in Local Loop
For an **incoming call**, the exchange sends a **90V AC ringing signal** (from a Ring Generator at the exchange) down the Ring wire to ring the phone's bell; the TIP wire connects to a Detector at the exchange to sense when the called party picks up.

### 3.7 FDM (Frequency Division Multiplexing)
Multiple voice calls are combined onto a single trunk between exchanges by assigning **each call its own frequency slot** (modulating each onto a different carrier frequency); the combined signal travels over one physical path and is **demultiplexed** back into individual calls at the receiving exchange.

### 3.8 Analog to Digital Converter (PCM)
Digital exchanges convert analog voice to digital using **Pulse Code Modulation (PCM)**:
- Voice signal bandwidth: **0–4 kHz**
- Sampling rate: **8 kHz** (per Nyquist, ≥2× the 4kHz bandwidth)
- **8 bits per sample**
- Result: **8,000 samples/sec × 8 bits = 64 kbps** per voice channel — the standard PSTN digital voice channel rate.

### 3.9 Time Division Multiplexing (TDM)
**32 voice channels**, each PCM-coded at 64 kbps, are multiplexed together using TDM into one **E-1** line:
- **E-1** = 32 × 64 kbps = **2.048 Mbps** (used in Europe and most of the world)
- **T-1** = 24 voice channels = **1.544 Mbps** (used in the US and Japan)

### 3.10 PDH (Plesiochronous Digital Hierarchy)
E-1/T-1 lines are further multiplexed into a hierarchy of higher-capacity trunks, each level combining 4 of the previous level:
**E-1 (2.048 Mbps) → E-2 (8.448 Mbps) → E-3 (34.368 Mbps) → E-4 (139.264 Mbps)**, typically transported over fiber-optic cable or microwave radio links.

### 3.11 Signaling System (CAS vs. CCS / SS7)
Two broad categories of PSTN signaling:
- **CAS (Channel Associated Signaling)**: basic signaling like off-hook/on-hook and dialed digits, carried in-band with the call.
- **CCS (Common Channel Signaling)**: a separate, dedicated signaling channel — in a digital E-1 trunk, this is typically **channel 16**, carrying **SS7 (Signaling System No. 7)** messages between exchanges in a mesh of dedicated SS7 links.

### 3.12 Service Switching Point (SSP)
The **SSP** is a local or tandem exchange equipped with an SS7 interface. It converts a subscriber's dialed digits into SS7 signaling messages and sets up, manages, and releases the actual voice circuit using its routing table. SSPs connect to STPs, which connect onward to SCPs, forming the broader **Intelligent Network (IN)** signaling mesh.

### 3.13 Signal Transfer Point (STP)
The **STP** acts as a router/gateway within the SS7 network — it does not originate messages itself, but switches SS7 messages between signaling points (SSPs and SCPs), and can also provide traffic/usage measurement for the network.

### 3.14 Service Control Point (SCP)
The **SCP** provides the interface for **value-added services** within the Intelligent Network, such as:
- Call forwarding
- Automated voicemail
- Call waiting
- Conference calling
- Caller ID
- Toll-free (800/888) and toll (900) number handling

It works alongside an **SDP** (Service Data Point) and **IP** (Intelligent Peripheral) within the overall IN architecture.

---

## Module 4: Internet and its Architecture

### 4.1 Network Edge: Devices, Hosts, Clients and Servers
The internet's "edge" consists of **hosts** — end systems like clients (laptops, phones, tablets) and servers (often concentrated in data centers) — connecting outward through a mobile network, a regional/local ISP, and ultimately a national/global ISP.

### 4.2 Access Network
The **access network** is how a host physically/logically connects into the internet — examples include mobile access networks (WiFi, 4G/5G).

### 4.3 Network Core
The **network core** is the mesh of **interconnected routers** that forms the internet's backbone — described as a "network of networks."

### 4.4 Network of Networks
- Hosts connect to the internet via **access ISPs**.
- Access ISPs must themselves be **interconnected**, so that any two hosts — regardless of which ISP they're on — can exchange packets with each other.
- The resulting "network of networks" is inherently complex, which is why the next lessons build up the internet's structure step by step.

### 4.5 How to Solve the Complexity of Internet/Computer Networks
Networks are complex, with many interacting pieces: hosts, routers, links of various media, applications, protocols, hardware, and software. The question posed: is there any hope of organizing this complexity? The answer used throughout networking is a **layered approach**.

### 4.6 The Layered Approach (illustrated via an air-travel analogy)
To motivate *why* layering helps, the lesson draws a parallel with how air travel is organized into a series of independent steps on each end of a trip (e.g., ticketing, baggage handling, boarding, and routing) — each step only needs to interact with the steps immediately above and below it, not the whole system at once. Networking applies the same idea: each layer (application, transport, network, etc.) exposes a clean interface to the layer above it and relies on services from the layer below, without needing to know the internal details of either.

### 4.7 Internet Protocol Stack
The standard internet layer stack, source to destination:
**Application → Transport → Network → Link → Physical**
As data moves down the stack, each layer wraps the data in its own header, producing (top to bottom) a **Message → Segment → Datagram → Frame**; headers are stripped back off in reverse order at the destination.

### 4.8 Legacy vs. Modern (Telecom) Network Architecture
**Legacy telecom architecture** kept voice and data on separate technology paths:
- **Data** and **Video** → **IP** (Network Layer) → **ATM/Ethernet** (Link Layer)
- **Voice** → **SS7** (Network Layer, circuit-switched signaling)
- Both ultimately ride over a shared **PDH/SDH** optical-fiber transport layer underneath.

This separate-paths model is what later converges in VoIP/IMS architectures (next modules), where voice is carried over the same IP infrastructure as data.

---

## Module 5: IP Network

### 5.1 Structure of an IP Network
An IP network consists of **subnetworks**: hosts within a subnetwork connect via an Ethernet switch or WiFi router, and different subnetworks are connected to one another via **routers**. **TCP** provides a logical end-to-end connection for reliable delivery; applications on hosts communicate over a **TCP socket** — a socket being a communication endpoint identified by an IP address + port number.

### 5.2 Two Key Router Functions
Every router performs two distinct jobs:
- **Routing**: a routing algorithm determines the source-to-destination route a packet should take.
- **Forwarding**: using a **local forwarding table** (destination address → output link), the router physically moves an arriving packet from its input to the correct output, based on the destination address found in the packet's IP header.

### 5.3 IP Range Aggregation
Rather than listing every individual destination address in a forwarding table, routers list **ranges of addresses** — aggregating many individual addresses into one table entry. This keeps forwarding tables compact even as the number of reachable addresses grows.

### 5.4 IP Addressing: A Data Network Example
Illustrates how hosts actually connect: wired hosts connect via Ethernet switches; wireless hosts connect via a WiFi base station/router, with a router interconnecting different subnets (e.g., 223.1.1.x, 223.1.2.x, 223.1.3.x in the example).

### 5.5 IP Addressing — Interface
An **interface** is the connection point between a host/router and a physical link. Routers typically have multiple interfaces (one per connected link); a host typically has one or two (e.g., wired Ethernet and wireless 802.11). An IP address is associated with each interface, not with the device as a whole. Example: `223.1.1.1` breaks into four 8-bit octets (e.g., `223`, `1`, `1`, `1`), each represented in binary.

### 5.6 Subnets
Conceptually, **detach each interface from its host or router**, which leaves "islands" of isolated interconnected networks — each such isolated island is called a **subnet** (e.g., the 223.1.1.x group of devices sharing a switch, as one subnet).

### 5.7 Internet IP Address Assignment Strategy
IP addresses are assigned top-down:
- **ICANN** (Internet Corporation for Assigned Names and Numbers) assigns address **blocks** to ISPs (e.g., a /20 block).
- The ISP then sub-allocates smaller blocks (e.g., /23s) out of its larger block to individual client organizations — this hierarchical, block-based (CIDR) allocation is what keeps global routing tables manageable.

---

## Module 6: VOIP

### 6.1 Introduction to Voice Over IP (VOIP)
VOIP is the technology for making packet-switched voice calls using IP. Advantages:
- **Low cost** — software-based, runs on Commercial Off-The-Shelf (COTS) hardware, versus PSTN switches built on proprietary hardware.
- **Integration** of voice, video, and data applications on one network.
- Enables **new service features** more easily than legacy PSTN.
- (Optionally) **reduced bandwidth** via advanced audio compression.

### 6.2 Softswitch
A **softswitch** (also called a Next-Generation IP Network/NGN component) is what VOIP systems use to **establish, maintain, route, and terminate** VOIP call sessions — the software-based successor to a traditional PSTN switch.

### 6.3 Softswitch Architecture: Media Gateway
The **Media Gateway (MG)**:
- Terminates **E1/T1** lines (the PSTN side).
- **Packetizes** voice channels for IP transport.
- Performs **CODEC** (compression/decompression) work, e.g.:
  - **G.711** — 64 kbps, the best fit/interface with PSTN quality
  - **G.722** — 64 kbps (wideband)
  - **G.729** — 8 kbps (highly compressed)

Overall softswitch picture: two **Media Gateway Controllers** communicate via **SIP/H.323** signaling; each side also has a **Signaling Gateway** (talking SS7 via SIGTRAN to the PSTN) and a **Media Gateway** (carrying the actual voice to/from the PSTN/TDM network), bridged across the IP/Internet core.

### 6.4 Signaling Gateway
The **Signaling Gateway** performs interconversion between **SS7** and **SIGTRAN**. SIGTRAN ("Signaling Transport") is essentially an **IP extension of SS7** — it provides the same call-management semantics as SS7 but carried over an IP network, using the stack: SIGTRAN application → **SCTP** (Stream Control Transmission Protocol) → IP → Data Link → Physical.

### 6.5 Media Gateway Controller (MGC)
Also called a **softswitch**, **call agent**, or **call controller**. It instructs the Media Gateways/media servers to set up and tear down calls, and instructs the Application Server to provide Value-Added Services (VAS) such as call forwarding, call waiting, video conferencing, playing recorded announcements, and other new intelligent services.

### 6.6 Separation of Media and Call Control
A deliberate softswitch design principle:
- **Media conversion** happens close to the traffic source and sink (at the Media Gateways).
- **Call-handling (signaling) functions** are **centralized** in the MGC.
- One MGC can control **multiple** media gateways.
- This separation lets new features be added more quickly, since they're implemented centrally rather than per-gateway.

### 6.7 Media Gateway Control Protocol (MEGACO/H.248)
**MEGACO** (also known as H.248) handles call & session management by instructing a Media Gateway to:
- Connect a **TDM stream** (voice channel) to an **RTP media stream**
- **Transcode** the stream between codecs if needed

Key nomenclature: a **Termination** is a source or sink of media; a **Context** is the association/connection between two or more terminations (i.e., the logical "call" grouping them together).

### 6.8 Call Flow Using MEGACO/H.248
A standard call setup sequence (User O → MGO → MGC → MGT → User T):
1. User O picks up the phone → **Notify Request/Reply** and **Modify Request/Reply** prepare the originating gateway.
2. User O dials User T's number → another **Notify Request/Reply**, then **Add Request/Reply** on the originating side.
3. The **Add Request/Reply** is relayed to the terminating MGT, followed by **Modify Request/Reply**, causing **Ringing** at User T.
4. User T answers → further **Notify/Modify Request-Reply** exchanges confirm the connection on both sides.

### 6.9 Session Initiation Protocol (SIP)
**SIP** is an **application-layer signaling protocol**, used for call signaling between Media Gateways — a simple protocol for creating, modifying, and terminating calls that may involve different MGCs. SIP packets often carry **SDP** (Session Description Protocol), which conveys the IP addresses/port numbers for the RTP stream, the codecs to use, and the bandwidth required.

### 6.10 Class 4 and Class 5 Softswitch
- **Class 5 softswitch**: connects the operator directly with **real end users** — the ones actually making and receiving calls (i.e., the access/local-exchange role).
- **Class 4 softswitch**: routes calls **between** Class 5 switches (i.e., the tandem/transit role) — it doesn't connect directly to end users.

---

## Module 7: IMS (IP Multimedia Subsystem) — Deep Dive

### 7.1 Introduction to IP Multimedia Subsystems (IMS)
IMS is an **architecture, not a protocol**; it supports VOIP and a range of IP-based services, is an open architecture primarily developed by 3GPP, and works across both fixed and wireless networks (enabling convergence and mobility between, say, a DSL connection and a mobile network). Evolutionary position: **PSTN Switch → Softswitch → IMS**.

### 7.2 IMS Architecture Layers
IMS is organized into three main layers, plus the access devices below them:
- **Application Layer**: the service logic and intelligence needed to deliver new applications (Application Servers).
- **Control Layer**: controls sessions between endpoints — contains the **CSCF** (Call Session Control Function), **MRF**, **HSS**, **BGCF**, and **MGCF**.
- **Transport Layer**: links access devices to the IMS network — contains **SGW**, **MG**, and the **PSTN Exchange**, reachable over 3G/4G/5G, DSL, WiFi, etc.
- **Access Devices**: the actual phones/laptops/other endpoints.

### 7.3 IMS Control Layer
The Control Layer is the **cornerstone of the architecture**, responsible for regulating communication flows:
- **CSCF (Call Session Control Function)**: controls (call) sessions between devices; may coordinate with Application Servers to provide services.
- **HSS (Home Subscriber Server)**: a centralized database that maintains all user profiles, and authenticates and authorizes users.

### 7.4 Call Session Control Functions (CSCFs) — P-CSCF
SIP servers that analyze and route the SIP messages controlling call sessions. The **Proxy-CSCF (P-CSCF)**:
- Is the **first point of contact** for a SIP signaling message entering IMS.
- Routes messages to the correct downstream IMS node.
- Provides **security** (e.g., protection against flooding attacks).
- Enforces **QoS for IMS** (bandwidth, delay).

### 7.5 CSCF — Interrogating (I-CSCF)
The **Interrogating-CSCF (I-CSCF)**:
- Handles **S-CSCF assignment** and session routing.
- Routes an incoming SIP request arriving from other SIP networks.
- Queries the **HSS** to find which S-CSCF is serving the called subscriber, then routes the call to that S-CSCF.

### 7.6 CSCF — Serving (S-CSCF)
The **Serving-CSCF (S-CSCF)**:
- Handles **user registration/authentication**.
- May contact an Application Server (e.g., the **TAS**, Telephony Application Server) for call setup.
- Generates **Call Detail Records (CDRs)**.

### 7.7 Application Servers (AS) in IMS
CSCFs provide basic call processing/routing, but richer services come from Application Servers:
- **TAS (Telephony Application Server)**: supplementary telephony services like call line hiding and call divert.
- Other **Application Servers** can provide broader **Value-Added Services (VAS)**: instant messaging, gaming, video conferencing.

### 7.8 Protocols Used in IMS
- **SIP**: establishes, modifies, and terminates call sessions.
- **Diameter Protocol**: authentication, authorization, and billing (AAA) — used between the CSCFs and the HSS.
- **RTP (Real Time Protocol)**: carries the actual call media (voice, video, etc.).

### 7.9 Session Initiation Protocol in IMS / Services Provided by SIP
Within IMS, SIP provides the same core services as in generic VOIP:
- **User location**: locate the IP address of the called device.
- **User availability**: determine whether the called device is available.
- **User capabilities**: negotiate device capabilities via SDP.
- **Session setup** (signaling): establish a call session.
- **Session management** (signaling): transfer or modify an ongoing session.

### 7.10 SIP Methods
*(Lesson video was slow to progress past its recap on the platform.)* Standard SIP methods (per RFC 3261) include: **INVITE** (initiate a session), **ACK** (confirm final response to INVITE), **BYE** (terminate a session), **CANCEL** (cancel a pending request), **REGISTER** (register a device's current location with the network), and **OPTIONS** (query a server's capabilities).

### 7.11 User Registration in IMS
A device must register with IMS before it can make/receive calls. Flow: device → **P-CSCF** → **I-CSCF** → queries **HSS** (Diameter User-Authorization-Request/Answer) → **I-CSCF** routes to the assigned **S-CSCF** → S-CSCF exchanges Multimedia-Auth-Request/Response with the HSS → device completes an **Authentication Challenge/Response** → S-CSCF performs a Server-Assignment-Request/Response with the HSS → device receives **200 OK**, confirming successful registration.

### 7.12 End-to-End SIP Signaling Path for Call Setup
Both the calling and called devices connect through their own local stack (WiFi/access network → P-CSCF → I-CSCF/S-CSCF, with MRF/HSS/Application Servers attached) — call signaling traverses both sides' control layers, while the **IMS Media Bearer** carries the actual voice/media path directly between the two devices' access networks once the session is set up.

### 7.13 IMS Call Setup Signaling (detailed SIP flow)
A full SIP call setup between Calling Device and Called Device, via IMS:
1. **INVITE (SDP Offer)** — calling device proposes IP addresses, ports, and codecs.
2. **183 Session Progress (SDP Answer)** — called side answers with its own media parameters.
3. **PRACK** / **200 OK (PRACK)** — the 183 response is reliably provisionally acknowledged.
4. **IMS Media Bearer establishment** — the underlying media path is set up.
5. **UPDATE (SDP Offer)** / **200 OK (SDP Answer)** — confirms the media bearer is in place.
6. **180 Ringing** — the called party's phone starts ringing.
7. **200 OK (INVITE)** — the called party answers.
8. **ACK** — the calling device confirms, completing call setup.

---

## Module 8: Communication & Access Fundamentals

### 8.1 Uplink, Downlink, Simplex, Duplex
- **Uplink**: transmission direction from the Mobile Station (MS) to the Basestation/BTS.
- **Downlink**: transmission direction from the Basestation to the MS.

### 8.2 FDD and TDD
- **FDD (Frequency Division Duplexing)**: uplink and downlink use **separate frequency bands**, transmitted simultaneously.
- **TDD (Time Division Duplexing)**: uplink and downlink share the **same frequency**, alternating in **time slots** (e.g., slot pattern 1, 2, 1, 2…).

### 8.3 FDMA and TDMA
- **FDMA (Frequency Division Multiple Access)**: each active mobile station (e.g., MS1–MS4) is assigned its own **frequency slot**, held continuously over time.
- **TDMA (Time Division Multiple Access)** / **Combination of FDMA and TDMA**: each frequency band is further subdivided into **time slots**, so a single frequency can be shared, round-robin, among several mobile stations — multiplying the number of simultaneous users a given amount of spectrum can support.

### 8.4 Frequency Modulation (FM)
A voice signal (0–4 kHz) is used to modulate the **frequency** of a much higher carrier wave (frequency modulation). Benefits include a **reduced antenna size** (practical at higher carrier frequencies) and the ability to put **different channels on different frequencies** so they don't interfere.

### 8.5 FSK (Frequency Shift Keying)
The **digital** counterpart to FM: a binary bit stream (0s and 1s) is represented by **discrete shifts in carrier frequency** — e.g., one frequency represents a `0` and another represents a `1`.

### 8.6 PSK (Phase Shift Keying)
Digital bits are represented by **shifts in the carrier's phase** rather than its frequency. In **Binary PSK (BPSK)**, a `0` and a `1` map to two points 180° apart on the phase constellation (e.g., at angles 0° and 180°).

### 8.7 QAM (Quadrature Amplitude Modulation)
QAM forms symbols by varying **both amplitude and phase** together, allowing more bits to be packed into each transmitted symbol:
- **QPSK**: a simple 4-point constellation (2 bits/symbol).
- **16-QAM**: a 16-point constellation (**4 bits per symbol**).
- **64-QAM**: a 64-point constellation (**6 bits per symbol**) — higher-order QAM carries more data per symbol but requires a cleaner (higher SNR) signal to decode reliably.

### 8.8 Circuit Switching and Packet Switching
- **Circuit Switching**: a dedicated end-to-end circuit is established for the call; analog or digital voice is carried continuously over that channel.
- **Packet Switching**: no dedicated end-to-end circuit; voice (or data) is carried as discrete packets, sharing the network — generally **more efficient and less costly** than circuit switching.

### 8.9 Cellular Concept — Early Mobile Telephone System Architecture
Historical motivation for the cellular concept: **Bell Mobile Systems** in New York City in the 1970s supported a maximum of only **12 simultaneous calls** across a **1,000 square mile** area using a single large coverage zone. This severe capacity limitation drove a restructuring of mobile systems to (a) increase capacity within a limited amount of spectrum and (b) still provide good coverage — leading directly to the cellular architecture covered next.

### 8.10 Co-Channel Interference Problem
Splitting a region into a cluster of smaller hexagonal **cells**, each with its own BTS, allows the same frequencies to be **reused** across the region — but reusing a frequency in a nearby cell too soon causes **co-channel interference** between cells using the same frequency. A **duplex channel** = a paired uplink and downlink channel.

### 8.11 Solution — Frequency Reuse
- The available duplex channels are **divided among a cluster of cells**, so neighboring BTSs use **different** frequencies from each other.
- If **S** total duplex channels are available and a cluster has **N** cells, each cell gets **k = S/N** channels.
- Typical cluster sizes: **N = 4, 7, or 12** cells — large enough to keep same-frequency cells spaced apart, avoiding co-channel interference, while still reusing spectrum efficiently across the wider network.

### 8.12 Splitting and Sectoring — Increasing Capacity
As the number of users in a service area grows, more channels are needed. Two solutions:
- **Cell Splitting**: divide an existing cell into several smaller cells, each with its own (lower-power) BTS, multiplying the number of times a frequency can be reused across the same geographic area.
- **Sectoring**: use directional antennas (instead of a single omnidirectional antenna) to split one cell site into multiple sectors (e.g., 3 sectors of 120° each), which also reduces interference between sectors.

### 8.13 Handover / Handoff Concept
As a mobile user moves from the coverage of one BTS (point A) toward another (point B), the received signal level from the first BTS drops. Once it crosses a defined **handoff threshold**, the call is properly transferred to the second BTS (BTS2) — this transfer, done without dropping the call, is the **handover/handoff**.

### 8.14 MAHO (Mobile Assisted Handover)
In MAHO, the **mobile device itself measures** signal strength/quality from the serving BTS and neighboring BTSs, and reports these measurements to the network's **Base Station Controller**, which uses them to decide when and where to hand the call over — the mobile "assists" the network's handover decision rather than the network deciding blind.

### 8.15 Umbrella Cell Approach
A large **"umbrella" cell** covers a wide area and is used for **high-speed-moving traffic** (e.g., vehicles on a highway), minimizing how often fast-moving users trigger handovers. Nested inside it, several **smaller cells** handle **low-speed traffic** (e.g., pedestrians), where more frequent handovers between small cells are not a practical problem.

### 8.16 Decibel Milliwatt (dBm)
*(Video did not load on the platform at time of writing.)* Standard definition: **dBm** is a logarithmic unit expressing power relative to 1 milliwatt: `dBm = 10 × log₁₀(P / 1mW)`. It's the standard way signal strength (e.g., received signal level, transmit power) is expressed in RF/telecom engineering, because it compresses a very wide range of power values into manageable numbers (and makes gains/losses simple additions/subtractions instead of multiplications).

### 8.17 Link Budget
*(Video did not load on the platform at time of writing.)* Standard definition: a **link budget** accounts for every gain and loss a signal experiences from transmitter to receiver — transmit power, antenna gains, free-space path loss, cable/connector losses, and a fade margin — compared against the receiver's sensitivity, to determine whether a radio link will close (be successfully received) under given conditions.

### 8.18 Three Main Components of Mobile Network
Any cellular mobile network has three main components:
1. **Mobile Station (MS)** = **ME** (Mobile Equipment) + **SIM**.
2. **Radio Access Network (RAN)** — where the MS connects to the mobile network (also just called the Access Network); contains the BTS/mast.
3. **Core Network (CN)** — provides overall control of the MS and handles call establishment and routing, connecting onward to the **External Network** (e.g., PSTN, Internet).

---

## Course Learning Check
A final **Cumulative Learning Check** (multi-question MCQ, covering topics across the whole course) sits at the end of the course as a self-assessment; individual lessons throughout the course also have smaller inline learning-check quizzes (not reproduced here).

## Notes on gaps
A small number of individual lesson videos ("Telecom Mast: Part 2," "Evolution of Telecom Technologies," "Decibel Milliwatt," "Link Budget," and part of "SIP Methods") either failed to load or were slow to reveal new content on the platform at the time these notes were compiled. Where that happened, the notes above rely on standard, well-established telecom engineering definitions for that specific sub-topic rather than the course's own slide wording.

---

## Glossary of Acronyms

| Acronym | Meaning |
|---|---|
| ITU / 3GPP | Int'l Telecom Union (sets targets) / 3rd Generation Partnership Project (writes specs) |
| RAN / CN | Radio Access Network / Core Network |
| GERAN / UTRAN | GSM/EDGE RAN / UMTS Terrestrial RAN |
| MSC / GMSC / MGW | (Gateway) Mobile Switching Center / Media Gateway |
| SGSN / GGSN | (Gateway) GPRS Support Node |
| HLR / VLR / AuC | Home / Visitor Location Register / Authentication Center |
| EPC / E-UTRAN | Evolved Packet Core / Evolved UTRAN (4G) |
| MME / HSS / SGW / PGW | 4G mobility mgmt, subscriber server, serving/PDN gateways |
| PCRF | Policy and Charging Rules Function |
| AMF / SMF / UPF / UDM | 5G mobility, session mgmt, user-plane, data mgmt functions |
| CUPS | Control and User Plane Separation |
| PSTN | Public Switched Telephone Network |
| MDF | Main Distribution Frame |
| PCM / TDM / PDH | Pulse Code Modulation / Time Division Multiplexing / Plesiochronous Digital Hierarchy |
| CAS / CCS / SS7 | Channel Associated / Common Channel Signaling / Signaling System No. 7 |
| SSP / STP / SCP | Service Switching / Signal Transfer / Service Control Point |
| ISP / ICANN | Internet Service Provider / Internet Corp. for Assigned Names & Numbers |
| CIDR | Classless Inter-Domain Routing |
| VOIP / RTP / SDP | Voice over IP / Real Time Protocol / Session Description Protocol |
| MG / MGC | Media Gateway / Media Gateway Controller |
| SIGTRAN / SCTP | Signaling Transport / Stream Control Transmission Protocol |
| MEGACO / H.248 | Media Gateway Control protocol (two names, same protocol) |
| SIP | Session Initiation Protocol (note: a *different* SIP than eTOM's "Strategy, Infrastructure & Product" in the other course notes) |
| IMS | IP Multimedia Subsystem |
| CSCF (P/I/S) | Call Session Control Function — Proxy / Interrogating / Serving |
| HSS / TAS | Home Subscriber Server / Telephony Application Server |
| FDD / TDD | Frequency / Time Division Duplexing |
| FDMA / TDMA | Frequency / Time Division Multiple Access |
| FM / FSK / PSK / QAM | Frequency Modulation / Shift Keying / Phase Shift Keying / Quadrature Amplitude Modulation |
| BTS / MS | Base Transceiver Station / Mobile Station |
| MAHO | Mobile Assisted Handover |
| dBm | Decibel-milliwatt (logarithmic power unit) |
