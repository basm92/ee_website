## Notes

To do:
  - In the course, we have a mid-term and an end-term. 
  - The course coordinator is responsible for assigning the students to the correct rooms according to surname distribution.
  - Tutor meetings every week
  - Q&A sessions?

To implement:
  - Event studies
  - Recapitulations in tutorials
  - Hand-out with short recaps as well
  - Interpretation of regression models and statistical output (in hand-out)


## Nieuwe master

- Handig om te weten wat de ambities zijn
- Economics & Data Analysis
    - Motivatie: Applied Data Science en Economics background
    - Gaan allemaal naar Erasmus
    - Focus op general econ & data analyse
    - Brug tussen economen en data scientists
    - Vanaf 26/27 van start

- Niet praktisch genoeg voor hun scriptie
    - Data set cleanen
    - Data sets mergen

- Everyone should have seen Diff-in-diff 
    - Most widely used research design across all disciplines
- What about IV?
    - Thoroughly understand IV/Late Not realistic

## New Concept Syllabus

- Stats 1 
- Stats 2
- LM 3
- TS 4 
  - model selection?
  - forecasting?
- Panel Data (FE) / Controls 5
- Binary Outcomes 6
- PO / Diff-in-diff 7
- Econometrics Hands-On 8

Bigger picture:
    - What after next year?

-Redesign last year:

- Also: fix a lot of stuff in lec6 binary outcomes



## Wolters Opzet

---

# Lecture 1

## Chapter 1: Introduction to Regression Analysis

*   **Motivation:** The lecture begins by establishing the starting points for empirical analysis in economics: economic theory and available data. It highlights that this course deals with observational data from non-controlled experiments.
*   **Key Questions:** Empirical economics aims to answer questions about causal effects, the magnitude of economic effects, prediction, and the precision of estimates.
*   **Types of Data:** The notes introduce three main types of data sets used in econometrics:
    *   **Cross-sectional data:** A sample of individuals (firms, households, etc.) at a single point in time.
    *   **Time-series data:** Observations on a single individual over multiple time periods.
    *   **Panel data:** A sample of individuals followed over time.

## Chapter 2: The First Stage of an Empirical Project (6 Steps)

This chapter outlines a systematic 6-step approach to starting an empirical analysis using linear regression.

*   **Step 1: Inspect Summary Statistics:** Before running a regression, it's crucial to examine descriptive statistics (mean, median, standard deviation) and correlations for the key variables to understand their distribution and relationships.
*   **Step 2: Estimate the Model:** This involves using a statistical package (like Stata) to estimate the parameters of the linear regression equation using Ordinary Least Squares (OLS). The interpretation of coefficients for different model specifications (e.g., log-level, level-log) is introduced.
*   **Step 3: Scrutinize the Estimates:** Check the statistical significance of the parameters using t-statistics and p-values. It is emphasized that statistically insignificant parameters cannot be interpreted.
*   **Step 4: Define the Population Model:** Write down the theoretical linear regression equation for the entire population, specifying the dependent variable, independent variables, and the error term.
*   **Step 5: State Assumptions for Causal Interpretation:** The critical "Zero Conditional Mean" assumption (`E(u|x) = 0`) is introduced. This assumption means that all other unobserved factors affecting the outcome are statistically independent of the included explanatory variables.
*   **Step 6: Evaluate Estimator Properties:** Determine if the parameter estimates are unbiased (accurate on average in small samples) or consistent (converge to the true value as the sample size grows).

## Chapter 3: Omitted Variables & Exogeneity

*   **Omitted Variable Bias:** This is a primary problem in regression analysis. If a relevant variable that is correlated with an included explanatory variable is omitted from the model, the Zero Conditional Mean assumption is violated, and the OLS estimator becomes biased.
*   **Exogeneity:** This is the key assumption for an unbiased OLS estimator. It requires that the unobserved factors in the error term (`u`) are unrelated to the explanatory variables. Two versions are presented:
    *   **Strong Assumption (Zero Conditional Mean):** `E(u | x) = 0`. Necessary for unbiasedness.
    *   **Weak Assumption (Zero Covariance):** `Cov(u, x) = 0`. Necessary for consistency.

## Chapter 4: The Mechanics of Ordinary Least Squares (OLS)

*   **The OLS Method:** OLS is an estimation method that finds the parameter values (β₀, β₁) that minimize the sum of the squared differences between the observed values and the predicted values (the sum of squared residuals).
*   **Normal Equations:** The minimization process results in a set of linear equations called the "normal equations," whose solution provides the OLS estimators.
*   **Key Properties of OLS:**
    *   The sum (and average) of the OLS residuals is zero.
    *   The covariance between the residuals and each of the explanatory variables is zero.
    *   The fitted (predicted) values lie on the estimated regression line.

## Chapter 5: Unbiased and Consistent Estimators

*   **Unbiasedness:** An estimator is unbiased if its expected value (the average of estimates over many random samples) is equal to the true population parameter. This is a small-sample property and relies on four key assumptions (MLR.1 - MLR.4), including the Zero Conditional Mean assumption.
*   **Consistency:** An estimator is consistent if its distribution collapses to the true parameter value as the sample size grows infinitely large. This is a large-sample property and relies on a weaker set of assumptions than unbiasedness (specifically, the zero covariance assumption instead of zero conditional mean).

## Chapter 6: Advanced Model Specification

*   **Quadratic Form:** To model non-linear relationships, squared terms of a variable can be added to the regression equation (e.g., `exper²`). In this case, the marginal effect of the variable is no longer constant and depends on its own level.
*   **Dummy Variables:** To incorporate qualitative data (e.g., gender), 0-1 indicator variables (dummies) are used. The coefficient on a dummy variable represents the average difference in the outcome compared to a reference group.
*   **Categorical Variables:** For variables with multiple categories (e.g., experience brackets), a set of dummy variables is created, with one category omitted as the reference group. F-tests are used to assess the joint significance of these categories.
*   **Interaction Terms:** The effect of one variable can be allowed to depend on another by including an interaction term (the product of two variables, e.g., `female * exper`). This allows for different slopes for different groups (e.g., different returns to experience for men and women).

---

# Lecture 2

### **Chapter 1: The Nature of Time Series**
*   **Time-series vs. Cross-sectional Data:** Time-series data has a logical temporal order and is not a random sample. A time-series dataset is a single realization of a stochastic process.
*   **Stata Commands:** The `tsset` command is used to declare a dataset as time-series. Stata provides operators like `L.` for lags, `F.` for leads, and `D.` for differences to easily work with time-series data.
*   **Error Terms:** In time-series regression, the error term is assumed to be identically and independently distributed (i.i.d.), meaning it has a zero expected value, constant variance, and no association between error terms across time (no autocorrelation). Violating the i.i.d. assumption leads to incorrect t-statistics and F-statistics.

### **Chapter 2: Interpretation of Dynamic Regression Models**
*   **Dynamic Models:** These models include lagged dependent and independent variables to capture the time-dependent effects of economic variables.
*   **Short-Run vs. Long-Run Effects:**
    *   The **contemporaneous (or short-run) effect** is the immediate impact of a change in an independent variable on the dependent variable within the same time period.
    *   The **long-run effect** captures the total change in the dependent variable over all periods resulting from a permanent change in an independent variable. It is calculated by considering the equilibrium values of the variables.

### **Chapter 3: Trends**
*   **Time Trends:** Many economic time series exhibit a tendency to grow over time. It is crucial to account for these trends to make valid causal inferences.
*   **Modeling Trends:**
    *   A **linear trend** is modeled by including a time variable (`t`) in a regression with a level dependent variable.
    *   An **exponential trend** is modeled by including a time variable (`t`) in a regression where the dependent variable is in logarithmic form.

### **Chapter 4: Seasonality**
*   **Seasonal Patterns:** Time series with daily, monthly, or quarterly observations may show regular patterns that repeat each year.
*   **Accounting for Seasonality:** Seasonal dummy variables can be added to a regression model to control for these effects. An F-test for the joint significance of these dummies is used to determine if seasonality is present.

### **Chapter 5: Spurious Regression**
*   **Definition:** A spurious regression occurs when two or more unrelated time series appear to have a statistically significant relationship simply because they both have a common trend.
*   **Solution:** Including a time trend variable in the regression equation can help to mitigate the risk of spurious regression by accounting for the unobserved trending variables that affect both the dependent and independent variables.

### **Chapter 6: Properties of OLS Estimators in Time-Series**
*   **Consistency:** For OLS estimates to be consistent in time-series analysis, several assumptions must hold:
    1.  The model must be linear.
    2.  There should be no perfect multicollinearity.
    3.  **Contemporaneous exogeneity** of explanatory variables is required.
    4.  All variables must be stationary.
    5.  All variables must be weakly dependent.

### **Chapter 7: Exogeneity in Time-Series Models**
*   **Strict Exogeneity:** The error term in a given period is independent of the explanatory variables in *all* time periods (past, present, and future). This is often a strong and incorrect assumption.
*   **Contemporaneous Exogeneity:** The error term in a given period is independent of the explanatory variables in the *current* period only.
*   **Violation of Strict Exogeneity:** Strict exogeneity is violated in models with lagged dependent variables or feedback mechanisms, where a past value of the dependent variable influences a current explanatory variable. In such cases, OLS estimates may be biased but can still be consistent if contemporaneous exogeneity holds.

### **Chapter 8: Weak Dependency**
*   **Definition:** A stationary time series is weakly dependent if the correlation between two observations in the series approaches zero as the time interval between them increases.
*   **Importance:** Weak dependency is a key assumption that allows for the application of the law of large numbers and the central limit theorem, which are necessary to prove the consistency of OLS estimators without requiring a random sample.
*   **Examples:** Autoregressive (AR(1)) and moving average (MA(1)) processes are examples of weakly dependent time series. A random walk is not weakly dependent.

### **Chapter 9: Implications of a Unit Root Model**
*   **Integrated Processes:**
    *   **I(0) Processes:** Weakly dependent (stationary) processes are integrated of order zero.
    *   **I(1) Processes:** Unit root processes, like a random walk, are integrated of order one. They are highly persistent.
*   **Transformations:** To use a highly persistent (I(1)) time series in regression analysis, it must be transformed into a weakly dependent (I(0)) series. This is typically done by taking the first difference of the series.

### **Chapter 10: Autocorrelation**
*   **Definition:** Autocorrelation (or serial correlation) occurs when the error terms in a regression model are correlated across different time periods.
*   **Consequences:** When autocorrelation is present, OLS estimators are still consistent (if other assumptions hold), but the standard formulas for their variances are incorrect. This leads to invalid t-tests and F-tests, often overestimating the statistical significance of variables.
*   **Testing for Autocorrelation:**
    *   **Durbin-Watson Statistic:** A test for first-order autocorrelation, valid only if all regressors are strictly exogenous.
    *   **Breusch-Godfrey Test:** A more general test for higher-order autocorrelation that is valid even with lagged dependent variables.

### **Chapter 11: Addressing Autocorrelation**
*   **Alternative Procedures:** If autocorrelation is detected, OLS should not be used. Instead, alternative estimation methods are available:
    *   **Prais-Winsten (FGLS):** An iterative procedure (Feasible Generalized Least Squares) that estimates the regression parameters while accounting for an AR(1) error structure.
    *   **Newey-West Standard Errors:** These are heteroskedasticity and autocorrelation consistent (HAC) standard errors that can be used to obtain valid t-statistics, provided the population regression is correctly specified.
    
---

# Lecture 4

Here is a summary of the lecture notes on Panel Data Analysis (I) by Prof. dr. Wolter Hassink.

### **Chapter 1: Introduction and Motivation**

*   **Motivation for Panel Data:** The lecture begins by motivating the use of panel data through the example of estimating the impact of the COVID-19 lockdown. To do this, researchers need data from the same individuals both before and during the event.
*   **Data Requirements:** This requires both a time series dimension (before and during) and a cross-sectional dimension (the same individuals or firms over time).
*   **Strength of Panel Data:** The notes assert that empirical analyses not based on panel data can be easily falsified.

### **Chapter 2: Advantages of Panel Data**

*   **Control for Cohort Effects:** Panel data allows researchers to distinguish between age effects and cohort effects, which is not possible with single cross-sectional data. An example of homeownership rates by age demonstrates this.
*   **Analysis of Dynamics:** True panel data is necessary to estimate dynamic models, such as labor force turnover rates. Cross-sectional data can't distinguish between a static situation (e.g., the same 50% of females are always employed) and a dynamic one (e.g., there is a 50% turnover rate each year).
*   **Solving Omitted Variable Bias:** The primary statistical advantage is controlling for unobserved individual-specific effects (omitted variables). Panel data allows for the separation of the true relationship (within-individual variation) from spurious correlations caused by these unobserved factors.

### **Chapter 3: Main Features of Panel Models**

*   **Combining Cross-Section and Time Series:** Panel data models combine the features of cross-sectional data (many individuals, `N`) and time-series data (multiple time periods, `T`).
*   **The Individual-Specific Effect (`aᵢ`):** A key feature of panel models is the introduction of an individual-specific intercept, `aᵢ`, which captures all unobserved, time-invariant characteristics of an individual (e.g., a firm's management quality, an individual's innate ability).
*   **Key Econometric Issues:** The lecture outlines four main issues in panel data analysis:
    1.  Should each individual have their own intercept (`aᵢ`)?
    2.  Is this individual intercept (`aᵢ`) correlated with the other explanatory variables?
    3.  How should time-invariant variables be handled?
    4.  Are the explanatory variables strictly exogenous?

### **Chapter 4: The Individual-Specific Effect and Strict Exogeneity**

*   **Unobserved Heterogeneity:** The individual-specific effect (`aᵢ`) captures unobserved heterogeneity. If this effect is correlated with the explanatory variables (e.g., motivation and experience in a wage equation), standard OLS regression will produce biased results.
*   **Strict Exogeneity:** For unbiased estimates in many panel models, the assumption of *strict exogeneity* is required. This means the error term at a given time `t` must be uncorrelated with the explanatory variables from *all* time periods (past, present, and future).
*   **Violation of Strict Exogeneity:** This assumption is violated in models with:
    *   **Lagged dependent variables:** Where the outcome from the previous period (`y_t-1`) is used as a predictor.
    *   **Feedback mechanisms:** Where the independent variable is influenced by past values of the dependent variable.

### **Chapter 5: Between and Within Variation**

*   **Between Variation:** This is the variation *across* individuals at a given point in time (cross-sectional). For example, comparing the profits of Firm A and Firm B.
*   **Within Variation:** This is the variation *over time* for a single individual. For example, comparing the profits of Firm A in Time 1 and Time 2.
*   **Focus of Panel Data:** Economists are typically more interested in the *within variation* because it allows them to control for individual-specific effects and isolate the causal impact of variables that change over time.

### **Chapter 6: Classification of Panel Data Estimators**

*   **Two Key Questions:** The choice of estimation method depends on the answers to two questions:
    1.  Is the unobserved individual effect (`aᵢ`) correlated with the explanatory variables?
    2.  Are all explanatory variables strictly exogenous?
*   **Balanced vs. Unbalanced Panels:** A *balanced panel* has the same number of observations for every individual, while an *unbalanced panel* does not.

### **Chapter 7: The First-Difference (FD) Estimator**

*   **Purpose:** The FD estimator is used when the individual-specific effect (`aᵢ`) is correlated with the explanatory variables.
*   **Method:** It eliminates the unobserved effect (`aᵢ`) by taking the difference of the regression equation between two consecutive time periods. This removes all time-invariant variables from the model.
*   **Requirement:** The FD estimator requires the assumption of strict exogeneity for the explanatory variables to produce consistent estimates.
*   **Estimation in Practice:** The lecture provides an example using Stata, showing how to run the regression, check for autocorrelation in the differenced errors, and use clustered standard errors to correct for it.

### **Chapter 8: Pooled Ordinary Least Squares (OLS)**

*   **Purpose:** Pooled OLS is used when the individual-specific effect (`aᵢ`) is assumed to be *uncorrelated* with the explanatory variables.
*   **Method:** It treats the panel data as one large cross-section and applies OLS.
*   **Issue of Autocorrelation:** The presence of the time-invariant individual effect (`aᵢ`) in the error term induces serial correlation.
*   **Solution:** To obtain correct standard errors, Pooled OLS must be estimated with clustered standard errors (clustered by the individual unit) to correct for this autocorrelation.

## Lecture 5



