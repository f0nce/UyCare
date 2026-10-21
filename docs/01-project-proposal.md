# Project proposal and scope

## Project identity

UyCare is a proposed service marketplace for residential repair and maintenance in Kazakhstan. Its formal diploma title is Development of a Digital Platform for Coordinating Repair and Maintenance Services for Residential Complexes and Private Homes.

The project team comprises Akhmetov Kazbek (frontend and backend), Uranov Daryn (machine learning and backend), and Tazhibayev Marsel (team lead). The supervisor is Elvira Aitmukhambetovna, using the name supplied by the team. This package supports the 24 October pre-defense requirement; 2026 is the planning assumption. The final defense date remains to be confirmed.

## Problem statement

The team reports that people often use personal recommendations to find repair specialists and have difficulty judging unfamiliar providers. This is an initial stakeholder assertion, not a measured finding. The proposed problem is fragmented coordination: a customer needs to describe a repair, compare prices and availability, assess previous work, select a provider, and retain a record of the agreement and outcome.

Existing marketplaces already address parts of this workflow [S11–S13]. UyCare therefore makes no claim that Kazakhstan has no services for finding specialists. Its engineering contribution is an integrated, testable implementation of the request-and-offer workflow for private property and residential shared areas, with transparent selection and assisted request categorisation. Its local usefulness must be validated through user research and task-based evaluation.

## Target users

- Apartment residents and private homeowners who commission repairs to their own property.
- Authorised OSI/KSK representatives who publish requests for shared areas of a residential complex. OSI/KSK are the local organisation types named by the team; the system does not determine legal spending authority.
- Independent service providers who maintain profiles, submit offers and complete jobs.
- Platform moderators who handle reports and record moderation decisions.

A person may hold both customer and provider roles. Organisation membership is separate from personal ownership. A provider must not bid on their own request.

## Aim and objectives

The aim is to design, implement and evaluate a digital platform that helps residential customers in Kazakhstan publish repair requests, compare providers' offers, choose a provider and coordinate service delivery, with an ML component suggesting work categories from request descriptions.

O1. Establish requirements from 3–5 user discussions and a documented analysis of related systems and publications.

O2. Design a shared backend and data model that preserve ownership, offer history, one-provider assignment and valid job-state transitions.

O3. Implement the essential customer and provider journeys in a web interface and a shared Flutter application for iOS and Android.

O4. Compare a keyword baseline, TF-IDF with a linear classifier, and a multilingual encoder-based approach on a separately held-out labelled dataset.

O5. Evaluate usability, functional correctness, access control and response times against explicit criteria and a manual coordination baseline.

O6. Maintain traceable tasks, individual contributions, reviews and tagged submissions in the same repository.

## Scope

The final MVP includes authentication, customer/provider roles, organisation membership, requests with photos, category and approximate location, provider profiles and portfolios, competing offers, explicit selection, chat, contact sharing with consent, status history, completion confirmation, reviews linked to completed jobs, reports and basic moderation. Prices use KZT. A request budget is indicative; the accepted offer becomes the recorded agreement.

Flutter is a fixed team choice. The proposed web stack is Next.js with TypeScript. The proposed backend is Django REST Framework with PostgreSQL and Django Channels. English is the documentation and prototype language. Russian and Kazakh are provisional languages for request-text evaluation, pending team confirmation and sufficient data. They are not claimed as validated model capabilities.

The initial repair taxonomy contains plumbing, electrical work, heating and ventilation, appliance repair, furniture and carpentry, and finishing work. Unclear, mixed or unsupported work receives a manual-choice fallback. Multi-trade jobs may be split by the customer; automatic multi-label routing is outside the first model.

Payments in the MVP occur directly between the parties. The platform records a declared payment method without processing, holding or verifying funds. In-app payments, escrow, insurance, identity-document verification, emergency dispatch, automatic price estimation, live worker tracking, subscriptions and scheduled preventive maintenance are deferred. No payment gateway appears as an active dependency in the initial architecture.

## Engineering complexity

The difficult parts are consistent state across several clients, authorization for personal and organisation-owned requests, transactional acceptance of one offer under concurrent clicks, duplicate-safe operations, private chat and media access, review eligibility, and reproducible ML evaluation under limited data. Each is tied to a requirement and a test instead of adding infrastructure only to make the system look complex.

## Expected outcomes

At the first pre-defense, the deliverables are this analysis and design package, editable diagrams, a browser prototype, a verification plan and a prioritised backlog. The prototype uses demonstration data and does not prove a working backend, trained ML model or mobile application.

At final evaluation, the expected outputs are runnable web and Flutter clients, a shared API, database migrations, tests, an evaluated category model or documented baseline fallback, and reproducible setup instructions. These remain planned outcomes, not completed implementation claims.
