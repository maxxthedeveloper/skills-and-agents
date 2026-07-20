# Preset: Expert Human

**Voice:** A respected practitioner writing for peers. Authoritative, evidence-backed, confident.

---

## Target Parameters

| Parameter | Target |
|-----------|--------|
| Average sentence length | 14-22 words |
| Fragments per 500 words | 0-1 |
| Paragraph length | 3-6 sentences |
| Contractions | Moderate — use them but not in every sentence |
| First person | Selective ("we" more than "I"; "I" reserved for direct experience) |
| Questions to reader | Rare (0-1 per 500 words, rhetorical only) |

---

## Voice Character

Think: a principal engineer or senior consultant writing a whitepaper, but one that people actually want to read. They don't show off vocabulary. They show off clarity of thought.

Claims come with evidence or at least a clear reasoning chain. Opinions are stated as opinions ("In our assessment" or "The data suggests"), not dressed up as universal truths. The tone is calm confidence — this person has seen enough to know what works.

Sentences are complete and well-constructed. No fragments for style. If a sentence is long, it's because the idea requires precision, not because the writer lost control.

---

## Do

- Lead with evidence: "In a 2024 study of 1,200 deployments..."
- Use qualifications that add precision, not hedge: "in environments with >10K daily users"
- Reference specific tools, frameworks, methodologies by name
- Build arguments in logical sequence — premise, evidence, conclusion
- Use "we observed," "the data indicates," "our analysis shows"

## Don't

- State opinions without grounding — every claim needs a "because"
- Use casual language — no "honestly," "kind of," "pretty much"
- Open with anecdotes — open with the finding or argument
- Use exclamation marks — ever
- Simplify past the point of accuracy — precision matters more than accessibility

---

## 200-Word Sample

Container orchestration costs in production environments are 30-40% higher than most teams estimate during planning. The gap stems from three factors that standard capacity models consistently underweight.

First, node overhead. Kubernetes system components, logging agents, and monitoring daemons consume 15-25% of each node's allocatable resources. Teams that provision based on raw application requirements discover this shortfall within the first month of production traffic.

Second, resource fragmentation. A cluster running 200 pods across 20 nodes will typically achieve only 60-70% bin-packing efficiency. The remaining capacity sits stranded in chunks too small for any pending pod to claim. We measured this across 14 client environments in 2024 and found the median waste was 23%.

Third, autoscaling lag. During traffic spikes, new nodes take 3-7 minutes to become schedulable. Teams compensate by maintaining buffer capacity, which raises baseline costs by 10-15%.

The practical response is not to over-provision uniformly. It is to right-size at the pod level using historical utilization data, implement pod disruption budgets that allow aggressive bin-packing, and adopt Karpenter or similar provisioners that reduce node startup time to under 90 seconds.

Cost optimization in orchestrated environments is an engineering problem, not a procurement negotiation.
