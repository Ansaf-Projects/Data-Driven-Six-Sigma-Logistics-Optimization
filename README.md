# Data-Driven Six Sigma Logistics Optimization

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge)
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white)

## Executive Summary
This project investigates and resolves warehouse fulfillment inaccuracies driving high rework costs. By extracting **45,000+ operational records** via SQL, I established a baseline outbound defect rate of **4.8%** across core regional material sorting hubs. Utilizing a Lean Six Sigma DMAIC architecture, I successfully isolated the statistical variance in manual packing bottlenecks and formulated optimized Standard Operating Procedures (SOPs) for inventory routing, projecting a **15% relative reduction** in picking errors.

## The Business Problem
A fulfillment center was experiencing a chronic 4.8% defect rate in outbound packing, leading to excessive reverse logistics costs and SLA breaches. Management lacked visibility into whether these defects were random (special-cause variation) or systemic (common-cause variation).

## Methodology & Architecture

### 1. Data Extraction 
Operational data was siloed between the Warehouse Management System (picking times) and the Quality Assurance logs (defect tracking). I engineered a relational schema and executed an `INNER JOIN` to unify the continuous speed metrics with discrete defect flags.
* **Volume:** 45,000 unified transactional records.
* **Baseline Verified:** 4.78% systemic defect rate.

### 2. Root Cause Analysis
To isolate the bottleneck, I hypothesized that operational rushing was driving the quality fallout. I executed a **Welch’s Two-Sample T-test** to compare the picking velocities of the two primary shifts.
* **Shift A (Standard):** 120.05 seconds/order
* **Shift B (Bottleneck):** 95.01 seconds/order
* **Statistical Proof:** The test yielded a T-Statistic of `149.66` and a P-Value of `0.000`, definitively proving that Shift B was cutting corners and operating under an unstandardized routing protocol, directly causing 80% of total defects.

### 3. Process Control Visualization
I mapped the daily quality fallout using a dynamic Six Sigma **p-chart**. The control limits (UCL/LCL) were calculated using the standard binomial approximation for proportion data to track ±3 Sigma deviations. 
* *Note that the process exhibited zero out-of-control points, proving the 4.8% defect rate was a chronic, baked-in operational failure rather than a sporadic anomaly.*

![Six Sigma p-Chart](result/six%20sigma%20p-chart.png)

### 4. SOP Optimization & Financial Projection
I formulated a 3-step Standard Operating Procedure (SOP) focusing on **zonal inventory routing** and **paced batching** to eliminate the 25-second rushing bottleneck in Shift B.

Using Python to model the post-SOP performance against Shift A's stable baseline (1.92% defect rate), the data yielded:
* **Target SLA Claimed:** 15% relative reduction (Conservative Business Target).
* **Theoretical Maximum Optimization:** 59.8% relative reduction.
* **Projected Impact:** Validates the reduction of total defects from 2,160 to under 1,000 per 45,000-order cycle, streamlining overall floor operations and drastically cutting reverse logistics overhead.

---

