# Glossary

## Core Framework Terms

### PEF (Primary-Entity / Execution-Variable / Final-Result)
The framework at the center of the story. A three-part decomposition of any purposeful behavior:
- **P (Primary Entity / 主体)**: Who is doing it. Must have a name, boundary, and unit.
- **E (Execution Variable / 变量)**: What it is done with. Must be shunted into controllable inputs (E_in) and uncontrollable environmental variables (E_out).
- **F (Final Result / 结果)**: What is obtained. Must be traceable to (P, E, t) — a specific subject at a specific time using specific variables.

### P/E/F Coordinate System
The conceptual framework through which the real world is projected. Like a two-dimensional plane — it captures certain aspects of reality (subject, variable, result) but loses depth (emotion, consciousness, free will, meaning, value).

### Five-Domain Isolation (五域隔离)
The PEF framework's structural design: P, E, F, π, and Audit are strictly isolated domains. No overstepping, no confusion. Each domain has its own rules, assertions, and verification mechanisms.

### π-Anchor (π锚)
A coordinate system using the digits of π as unforgeable coordinates. Each audit step is bound to a specific π digit position. Properties: infinite non-repeating, fully reproducible, stateless, anti-vector-collapse, globally consistent.

### π-Mod3 Phase Allocation (π-Mod3 相位分配)
Phase = (π_digit + Block_ID) mod 3. Uses π's infinite non-repeating property to distribute processing across three phases in a seemingly random but reproducible manner.

### Content-Bound π Scheduling (内容绑定π调度)
source_hash → SHA-256 → π digit offset. Binds scheduling to content identity, ensuring any node given the same source_hash calculates the same π offset without state synchronization.

### StateLedger (审计账本)
The audit ledger that records every step, every correction, every boundary admission. 16 pages by the end of the story. Each page corresponds to a hammer strike and its resulting correction.

### Runtime Assertions (运行时断言)
Mechanism that verifies every claim, flags every exaggeration, exposes every pretense at runtime. Part of the calibration device.

### Calibration Device (校正装置)
The system that runs five-domain isolation, StateLedger recording, and runtime assertion verification. Its true function (revealed in Chapter 9) is not to eliminate illusions, but to make shadows honest.

### Anti-Vector Collapse (防向量坍缩)
A hypothesized function of π: by forcing the system to use long digit slices of π, it prevents large models from compressing π into short approximations like 3.14. Marked as hypothetical function pending empirical verification.

### HLC (Hybrid Logical Clock)
A timekeeping mechanism that combines logical clocks with physical timestamps. Recommended in Chapter 6 for distributed environments where π-anchor's Newtonian absolute time assumption is insufficient.

## Philosophical Terms

### Laplace's Demon (拉普拉斯妖)
A hypothetical being that, knowing the position and momentum of every particle in the universe, could predict the entire future and retrodict the entire past. The architect's starting self-identification.

### Homunculus (小人)
A term from philosophy of mind referring to a "little person" inside the mind who does the actual perceiving/thinking, leading to infinite regress. In the story, π is the framework's homunculus — it's at the core but not inside the framework, its position is undeterminable.

### Plato's Cave (柏拉图洞穴)
The allegory of prisoners chained in a cave who see only shadows on the wall and mistake them for reality. One prisoner escapes, sees the real world, returns to tell the others, but they don't believe him. In the story, PEF is the cave, P/E/F is the wall, and the seven philosophers are those who escaped.

### Two-Dimensional Perfect Circle (二维纯圆)
A mathematically perfect circle existing in abstraction — every point equidistant from center, no thickness, no error. Represents the PEF framework's perfection without depth.

### Physical Pixel Circle (物理像素圆)
A circle made of physical pixels — jagged edges, tiny errors, thickness, physical substance. Represents reality's imperfection with depth.

### Gödel's Incompleteness Theorems (哥德尔不完备定理)
Any sufficiently powerful formal system contains true propositions that cannot be proven within the system. Used in the story to explain why π's existence as a foundation assumption cannot be proven within the PEF framework.

### Cogito Ergo Sum (我思故我在)
Descartes' foundational proposition: "I think, therefore I am." Challenged in Chapter 1 — it proves thinking exists, not that "I" exists as a substantial subject.

## Story Terms

### The Nine Hammers (九锤)
The nine sequential assaults on the architect's illusions:
1. Descartes' Ghost — Subject layer
2. Gödel's Loop — Logic/Completeness layer
3. Thor's Hammer — Verifiability/Sincerity layer
4. Turing's Crush — Choice/0-to-1 layer
5. Schrödinger's Cat — Physics/Quantum boundary layer
6. Einstein's Verdict — Time/π layer
7. Kant's Space — Space/mod layer
8. The Position of π — Core/Foundation assumption layer (π self-shattering)
9. The Shadow of the Cave — Shadow/Reality layer (shadow self-shattering)

### The Fade (褪色)
The system's gradual degradation — UI borders dissolve, inventory numbers drift, log hashes change meaning, microservice boundaries melt. Root cause revealed in Chapter 9 as the dishonesty of the shadow. Stops when the shadow becomes honest.

### Timestamp Shift (时间戳自变)
After each hammer, the StateLedger timestamp shifts by exactly one second. No modification is made. A recurring pattern that signals each hammer's completion and builds tension.

### Ashes (灰烬)
Shattered illusions become ashes. Preserved rather than deleted. Ashes are history, evidence, and proof of honesty. A framework that cleans up its ashes is a dishonest framework.

### Honest Observer (诚实的观测者)
The architect's final state. Knows he sees only shadows, knows their boundaries, knows their foundation assumptions, knows their vulnerabilities. But honestly reflects shadows — doesn't exaggerate, doesn't pretend, doesn't package simplicity with depth. This is not downgrading from Laplace's Demon; it is upgrading.

### Honesty Check: PASSED (诚实性检查：通过)
The final verdict on the monitoring dashboard. After nine hammers, eight layers all show "FAILED," but honesty shows "PASSED." The first and only "PASSED."
