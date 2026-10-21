# UX and prototype

## Prototype purpose

The portable prototype in prototype/index.html demonstrates the core marketplace flow with fictional people, offers and reviews. It runs in a browser without installation. All state is local to that browser; there is no real authentication, server, payment processor, trained ML model or external messaging. The visible demo notice remains present throughout the experience.

Private hosted preview: https://uycare-repair-prototype.sunnychime6.chatgpt.site. This is an owner-private preview, not an unrestricted committee link. The portable files provide a demonstration route independent of hosted sharing settings. Deployment and domain checks passed; full browser walkthrough and mobile viewport inspection remain manual verification items.

## Key scenarios

UC-01 Publish a request. A customer describes a repair, chooses a property context, supplies a city/district, reviews a category suggestion, enters a budget and publishes. Validation explains missing fields. The exact street address is intentionally absent from the public view.

UC-02 Compare offers. A customer opens a request and compares three fictional offers by total price, availability, portfolio and rating count. Sorting by price or rating changes the order. Opening a profile reveals clearly labelled demonstration portfolio material and reviews. Selection requires an explicit confirmation.

UC-03 Respond as a provider. The role switch opens a provider view. A provider inspects an open request and submits a price, schedule and scope. The new offer appears when returning to the customer view. This role switch is a demo control, not account authorization.

UC-04 Coordinate and complete. After acceptance, the customer can send local chat messages. The provider starts the work and marks it ready. The customer confirms completion and submits one review. The screen shows the job state and retained agreement.

UC-05 Handle exceptional states. A customer can cancel an open request; an assigned job supports a cancellation request and confirmation by the other demo role. Empty filters, invalid amounts, missing descriptions and duplicate reviews have explicit responses. A low-information category suggestion returns manual choice.

## Interaction decisions

Offers show scope inclusions so a lower quoted amount is not presented as automatically preferable. A review count accompanies ratings. Price and rating sorts are user-controlled. Category suggestions never submit a request or choose a provider automatically. Organisation-owned requests visibly show that context. English labels support the pre-defense discussion; production localisation remains a separate requirement decision.

## Demonstration script

Reset the demo. Inspect the sample request, open a provider profile and sort offers. Create a new request, switch to provider mode and send an offer, then switch back and accept it. Send a chat message. Switch to provider mode to start and mark the work ready, then return as customer to confirm and review. Demonstrate cancellation on a second request. Repeat the core screens at a mobile width.

The prototype is evidence of interaction design only. Its client-side restrictions do not satisfy server security requirements, and its rule-based category demo does not satisfy the ML quality gate. tests/prototype-checklist.md records what to inspect before a presentation.
