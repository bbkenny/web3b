# AfrikFund Project Issues & Tasks

This document outlines all the development tasks needed to build **AfrikFund (DiasporaDAO)**, a decentralized platform for transparent community funding in Africa.

---

## 🛠️ Smart Contract Issues (Solidity)

### Phase 1: Core Fundraising Engine

#### Issue #1: Hardhat Project Setup & Standards
- [ ] Initialize Hardhat environment with TypeScript
- [ ] Configure `hardhat.config.ts` for Base L2 (Testnet/Mainnet)
- [ ] Install OpenZeppelin contracts (v5.0+)
- [ ] Setup linting (Solhint) and formatting (Prettier-Solidity)

#### Issue #2: Campaign Registry Implementation
- [ ] Define `Campaign` struct (goal, deadline, beneficiary, totalRaised, metadataHash)
- [ ] Implement `createCampaign` function with validation (min duration, valid beneficiary)
- [ ] Add event emission for `CampaignCreated`
- [ ] Implement read-only functions to fetch campaign data

#### Issue #3: Donation & Fund Management (Native ETH)
- [ ] Implement `donate` function for campaigns
- [ ] Track individual donor contributions for impact reporting
- [ ] Prevent donations after deadline or goal met (optional: overflow handling)
- [ ] Add event emission for `DonationReceived`

#### Issue #4: ERC-20 (USDC) Support
- [ ] Integrate OpenZeppelin's `IERC20` interface
- [ ] Support stablecoin (USDC) donations alongside native ETH
- [ ] Implement safe transfer patterns for tokens

### Phase 2: Transparency & Governance

#### Issue #5: Proof-of-Impact (IPFS Hash Storage)
- [ ] Add `withdrawalRequests` map and structs
- [ ] Implement `submitWithdrawalRequest` (Admin only) requiring IPFS hash of proofs (receipts/photos)
- [ ] Store immutable audit trail of withdrawals

#### Issue #6: Multi-sig / DAO Approval Logic
- [ ] Implement community voting or threshold approval for withdrawal requests
- [ ] Add `approveWithdrawal` and `executeWithdrawal` functions
- [ ] Ensure funds are sent directly to the verified project beneficiary

#### Issue #7: Security & Access Control
- [ ] Implement `Ownable` or `AccessControl` for admin roles
- [ ] Integrate `ReentrancyGuard` for all fund-moving functions
- [ ] Add `Pausable` functionality for emergency circuit breaking

#### Issue #8: Testing & Quality Assurance
- [ ] Write unit tests for campaign creation and edge cases (Chai/Mocha)
- [ ] Write integration tests for the full donation-to-withdrawal flow
- [ ] Perform gas optimization analysis

---

## 💻 Frontend Issues (Next.js)

### Phase 3: UI Foundation & Branding

#### Issue #9: Next.js 15+ App Router Setup
- [ ] Refine project structure (components, hooks, lib, providers)
- [ ] Implement Global Theme (Dark Mode with African vibrant accents: Gold/Green/Red)
- [ ] Setup Tailwind CSS 4 configurations and utility classes

#### Issue #10: Web3 Provider & Wallet Integration
- [ ] Integrate `Wagmi` and `Viem` for blockchain interactions
- [ ] Setup `ConnectKit` or `RainbowKit` for a premium wallet connection experience
- [ ] Implement "Switch Network" prompt for Base L2

### Phase 4: Campaign & User Experience

#### Issue #11: Campaign Discovery Dashboard
- [ ] Design and build `CampaignCard` component with progress bars
- [ ] Implement search and category filtering (e.g., Education, Health, Infrastructure)
- [ ] Add skeleton loaders for initial data fetching

#### Issue #12: Campaign Creation Wizard
- [ ] Build a multi-step form for creating new funding rounds
- [ ] Implement IPFS integration for project descriptions and cover images
- [ ] Add form validation (Zod) and preview mode

#### Issue #13: Donation Interface & Flow
- [ ] Create `DonateModal` with currency toggle (ETH/USDC)
- [ ] Implement real-time transaction status feedback (Pending/Success/Error)
- [ ] Add "Confetti" effect on successful donation

### Phase 5: Transparency & Admin Tools

#### Issue #14: Proof-of-Impact Gallery
- [ ] Implement a view for withdrawal requests showing IPFS-hosted proofs
- [ ] Create an image lightbox/viewer for receipts and project photos
- [ ] Link withdrawal events to project milestones

#### Issue #15: Admin Governance Dashboard
- [ ] Build interface for admins to submit withdrawal requests
- [ ] Build interface for community members to vote on approvals
- [ ] Implement "Execution" triggers for approved funds

#### Issue #16: Donor Profile & Impact Portfolio
- [ ] Create user profile page showing "Total Contributed" and "Projects Funded"
- [ ] Display individual impact badges based on milestones
- [ ] Implement contribution history list

### Phase 6: Performance & Polish

#### Issue #17: Optimization & Mobile Readiness
- [ ] Ensure 100% mobile responsiveness for all dashboards
- [ ] Implement SEO optimization (Metadata API)
- [ ] Add Error Boundary handling for contract failures

---

## 📊 Priority Levels

- **P0 (Critical)**: Smart Contract Core, Wallet Connection, Donation Flow
- **P1 (High)**: Withdrawal Logic, IPFS Integration, Discovery Dashboard
- **P2 (Medium)**: DAO Governance, User Profiles, Stats
- **P3 (Low)**: Analytics, Impact Badges, SEO

---

**Authored by: bbkenny <jouleself@gmail.com>**
