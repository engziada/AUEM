# Graph Report - .  (2026-09-21)

## Corpus Check
- Corpus is ~16,622 words - fits in a single context window. You may not need a graph.

## Summary
- 31 nodes · 89 edges · 6 communities
- Extraction: 90% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 9 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Community 0
- Community 1
- Community 2
- Community 4

## God Nodes (most connected - your core abstractions)
1. `esc()` - 14 edges
2. `L()` - 14 edges
3. `base()` - 13 edges
4. `page_header()` - 11 edges
5. `page_unions()` - 7 edges
6. `paras()` - 6 edges
7. `icon()` - 6 edges
8. `page_index()` - 6 edges
9. `page_about()` - 6 edges
10. `page_membership()` - 6 edges

## Surprising Connections (you probably didn't know these)
- `base()` --calls--> `esc()`  [EXTRACTED]
  build.py → build.py  _Bridges community 2 → community 1_
- `hero()` --calls--> `esc()`  [EXTRACTED]
  build.py → build.py  _Bridges community 2 → community 4_
- `hero()` --calls--> `L()`  [EXTRACTED]
  build.py → build.py  _Bridges community 1 → community 4_

## Import Cycles
- None detected.

## Communities (6 total, 0 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.40
Nodes (8): addChips(), addMsg(), answer(), ask(), norm(), score(), t(), tokens()

### Community 1 - "Community 1"
Cohesion: 0.61
Nodes (8): base(), L(), page_activities(), page_contact(), page_governance(), page_header(), page_news(), page_objectives()

### Community 2 - "Community 2"
Cohesion: 0.70
Nodes (5): esc(), page_about(), page_membership(), page_unions(), paras()

### Community 4 - "Community 4"
Cohesion: 1.00
Nodes (3): hero(), icon(), page_index()

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `esc()` connect `Community 2` to `Community 1`, `Community 3`, `Community 4`?**
  _High betweenness centrality (0.031) - this node is a cross-community bridge._
- **Why does `L()` connect `Community 1` to `Community 2`, `Community 3`, `Community 4`?**
  _High betweenness centrality (0.031) - this node is a cross-community bridge._
- **Why does `base()` connect `Community 1` to `Community 2`, `Community 3`, `Community 4`?**
  _High betweenness centrality (0.025) - this node is a cross-community bridge._