# Before/After: "The Case Against Premature Abstraction"

**Preset:** paul-graham | **Target length:** ~600 words

---

## BEFORE (Typical AI-Generated Blog Post)

# The Case Against Premature Abstraction: Why Less is More

In the ever-changing landscape of software development, abstraction is often considered one of the most powerful tools in a developer's arsenal. However, it's crucial to understand that not all abstraction is created equal. Let's dive deeper into why premature abstraction can be more harmful than the code duplication it aims to prevent.

## Understanding Premature Abstraction

Premature abstraction occurs when developers create abstract interfaces, generic solutions, or reusable components before they fully understand the problem domain. While abstraction is fundamentally a best practice, applying it too early can lead to several significant issues:

- **Unnecessary complexity:** Abstract layers add indirection that makes code harder to follow
- **Wrong abstractions:** Without enough concrete examples, you'll abstract over the wrong axis
- **Rigid architecture:** Premature abstractions often become load-bearing walls that are expensive to change
- **Slower development:** Teams spend time working around abstractions that don't fit their actual needs

## The Root Cause

It's worth noting that premature abstraction often stems from good intentions. Developers are taught that DRY (Don't Repeat Yourself) is a fundamental principle. Moreover, creating elegant abstractions feels intellectually satisfying. However, this pursuit of elegance can lead us astray.

The reality is that you need to see at least three concrete implementations before you can identify the right abstraction. This is sometimes called the "Rule of Three" — and it's a remarkably effective heuristic for avoiding premature abstraction.

## A Better Approach

Instead of reaching for abstraction at the first sign of duplication, consider this more measured approach:

1. **Write the concrete implementation first.** Get it working without worrying about reusability.
2. **Wait for the second use case.** When you need similar functionality, copy and modify. Yes, really.
3. **Abstract on the third occurrence.** By now, you've seen three concrete examples and can identify what actually varies versus what stays the same.

Additionally, when you do abstract, prefer simple function extraction over complex class hierarchies. The best abstraction is often just a well-named function.

## Conclusion

In summary, the best defense against premature abstraction is patience. By waiting until you have sufficient concrete examples, you'll create abstractions that actually serve your codebase rather than constrain it. Remember: duplication is far cheaper than the wrong abstraction. Embrace the messiness of concrete code — it's the foundation upon which good abstractions are eventually built.

---

## AFTER (Rewritten with blog-writer skill, paul-graham preset)

# The Case Against Premature Abstraction

I used to be the developer who abstracted everything on the second occurrence. Saw two similar functions? Time for a generic one. Two similar components? Time for a base class. I was proud of how DRY my code was. I was also the reason my team spent three days every time they needed to add a feature.

The problem with abstracting early is that you don't yet know what varies. You think you do. You look at two functions that share 80% of their logic and you think, obviously, the common part is the abstraction and the different parts are the parameters. But you're wrong about which 80% is common. You're always wrong about this, because you've only seen two examples.

Here's an analogy that might help. Imagine you see two animals — a dog and a cat — and you need to design an abstraction for "animal." You'd probably pick four legs, fur, tail, domesticated. Then you meet a snake. Your abstraction is useless.

That's what happens in code. You abstract over the pattern you've seen. Then the third use case arrives and it doesn't fit. Now you have three options, all bad: force the new case into the wrong abstraction, add a special case that makes the abstraction leaky, or rewrite the abstraction from scratch. Most teams pick option two. They keep picking option two. The abstraction accumulates special cases like barnacles until nobody understands what it does anymore.

Sandi Metz said it better than I can: "Duplication is far cheaper than the wrong abstraction." She's right. Three identical 20-line functions are annoying, but each one is self-contained and obvious. A single 40-line generic function with six parameters and four boolean flags is a puzzle box that takes an afternoon to understand every time someone opens it.

The rule I follow now is simple. I wait until I see the third instance. Not the second — the third. By then, the pattern is real. You can see what actually varies versus what stays constant. The abstraction isn't a guess anymore. It's an observation.

And when I do abstract, I reach for the smallest tool. Not a class hierarchy. Not a generic framework. Usually just a function. A well-named function with clear inputs and outputs. The kind of abstraction you can understand in thirty seconds.

The irony is that patient code — messy, duplicated, concrete code — produces better abstractions in the end. Because the abstractions are based on evidence, not prediction. And prediction, in software, is almost always wrong.

I still feel the itch to abstract early. Every developer does. But I've learned to treat that itch the way I treat most impulses: notice it, wait, and see if it still makes sense in a week.

It usually doesn't.

---

## What Changed

| Metric | Before | After |
|--------|--------|-------|
| Word count | 410 | 425 |
| Taboo phrases | 12 (ever-changing landscape, crucial to understand, dive deeper, fundamentally, moreover, it's worth noting, the reality is, additionally, in summary, embrace, remarkably, several significant) | 0 |
| Core idea | Split across headers (Understanding → Root Cause → Better Approach → Conclusion) | Single thread: "You're always wrong about which 80% is common, because you've only seen two examples." |
| Surprise | Restates known advice (Rule of Three) | The dog/cat/snake analogy makes abstract advice visceral; "option two barnacles" frames the real cost |
| Sentence length std dev | 3.5 (mechanical) | 7.8 (varied) |
| Avg sentence length | 17.8 words | 14.2 words |
| Specificity | Abstract ("several significant issues," "good intentions") | Concrete (Sandi Metz quote, "six parameters and four boolean flags," "three days every time") |
| Quotable line | None (closest: rephrased DRY principle) | "Three identical 20-line functions are annoying, but each one is self-contained and obvious." |
| Structure | Template with headers (Understanding → Root Cause → Approach → Conclusion) | Continuous prose, exploratory — follows the writer's thinking from personal experience to principle |
