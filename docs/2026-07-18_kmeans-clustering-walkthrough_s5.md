---
title: s5 — K-means clustering (first contact)
date: 2026-07-18
sessions: [s5]
concepts: [kmeans, pca]
type: notes
up: "[[MOC-m1-ml-fundamentals]]"
recap: "First-contact k-means from s5 + StatQuest — elbow to pick k, then the assign→mean loop to convergence, rebuilt unaided on a 9-student cgpa/iq dataset. PCA matrix-mapping from this session is pending the full session notes."
tags: [kmeans, clustering, unsupervised, s5]
---

# s5 — K-means clustering (first contact)

> **Recap:** first-contact [[kmeans]] — the elbow picks k, then the **assign→mean** loop runs to
> convergence. Rebuilt the whole algorithm unaided from the StatQuest video + lecture. The formal
> **PCA matrix-mapping** from this session (`Cv=λv` derivation, `X₀=X−mean(X)`, the 200-people
> example) is **pending** — to be mapped onto prior intuition once the full s5 notes arrive.

## The journey today

Reported k-means back **as first-time learning** (not recall), and rebuilt it correctly end-to-end:

1. **Pick k with the elbow** — plot [[kmeans|WCSS]] vs k, take the corner (here k=3). Caught the trap:
   lowest WCSS is a trap (k=n → WCSS=0, useless). ![[trap-log#^kmeans-wcss-min]]
2. **Init** centroids on random real points; re-run several times, keep lowest WCSS (dodges local minima —
   the same local-minimum risk as [[gradient-descent]]).
3. **ASSIGN** each point to its nearest centroid by Euclidean distance ([[vectors]]).
4. **MOVE** each centroid to the mean of its members.
5. **Repeat** until centroids stop moving (convergence).

Also nailed the decision boundary and one key correction:

- **cluster ≠ classify.** A [[ml-taxonomy|classifier]] sorts into KNOWN labels; k-means DISCOVERS
  groups that never had labels. ![[trap-log#^kmeans-classify]]

## Artifacts

- Full atom with the frame-by-frame walk + numpy twin: [[kmeans]]
- Interactive twin (elbow + synced numerical/sketch loop):
  [K-means walkthrough](../html/2026-07-18_kmeans-clustering-walkthrough_s5.html)
- Static frame images: `docs/attachments/kmeans_*.png`

## Still owed (pending the full s5 notes)

- [ ] **PCA matrix-mapping** — map prior intuition (covariance→eigen→PCA "20→3") onto the session's
      formal matrix notation: `var(vᵀx)=vᵀSv`, the Lagrangian → `Cv=λv` derivation, `cov(X)=X₀ᵀX₀/(n−1)`,
      the 200-people height/weight example. Reframe as an HTML that puts intuition ↔ matrix equations
      side by side (the exam's language). See [[pca]].
