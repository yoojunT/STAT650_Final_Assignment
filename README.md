# STAT 650 - Final Project

### Submit files: python files [Link], data file (.csv; .xlsx) [Link], pdf [Link]

## 1. Project Title, Name, UIN
- **Project title:** Investigating the uncertanties assocated with 
- **Name:** Yoojun Kim
- **UIN:** 932002858

## 2. Introduction
> **[Guideline]** </br>
> Provides the goal, objectives (research hypotheses) and background of the project. </br>
> Research interest/problem statement </br>
> Significance of the project </br>
> Theoretical background of the topic being addressed

### 2-1. Resarch Background 
Heat exposure poses a significant threat to occupational safety, underscoring the need for the timely risk assessments to protect the workforce. Such assessments are imperative for the implementation of preventative strategies, including promoting adequate hydration and ensuring that workers take sufficient breaks. A prevalent approach to assess the occupational heat risk involves the use of the Wet Bulb Globe Temperature (WBGT) index. Despite its fundamental role in occupational safety management, its practical implementation is limited due to the challenge associated with timely data collection of globe temperature, which is crucial for calculating the outdoor WBGT index. This absence has hindered the deployment of proactive heat mitigation strategies. </br>

To fill this knowledge gap, this research leverages the hourly forecast data updates from the National Weather Service (NWS) for enhancing the WBGT index. However, like all forecasting models, these predictions are subject to uncertainties that necessitate additional refinement. Accordingly, this study will concentrate on the post-processing of heat radiation forecasts, identified as having a critical influence on the accuracy of WBGT predictions.

- **Problem Statement**: Uncertanties of heat risk Forecasts as detailed above.
- **Contribution/Significance:**  This methodological and knowledge enhancement in heat risk analysis aims to significantly aid practitioners in making informed decisions to mitigate potential heat-related hazards at jobsites. The contributions/significances are further elaborated in the conclusion section.

### 2-2. Research Hypotheses 
This study centers on a detailed examination of three key research hypotheses, each aiming to deepen our understanding of the factors influencing WBGT forecasting:
- **Research Hypothesis 1 (RH1)**: This hypothesis posits that errors in the Global Horizontal Irradiance (GHI) forecasts have the most substantial effect on the accuracy of WBGT forecasts. It suggests a direct and significant correlation between GHI forecast discrepancies and the reliability of WBGT predictions.
- **Research Hypothesis 2 (RH2)**: This hypothesis explores the variability of GHI forecast errors across different climatic regions. It proposes that the inaccuracies in GHI predictions are not uniform but vary significantly depending on the climate type, highlighting the need for region-specific analysis in meteorological modeling.
- **Research Hypothesis 3 (RH3)**: This hypothesis asserts that in the context of regression models, a multiplicative regression model, which incorporates relevant climate factors, is more effective than a basic linear regression model. It emphasizes the importance of a comprehensive approach that takes into account various climatic variables to enhance the predictive accuracy of WBGT forecasts.

### 2-3. Research Scopes
- **Modleing Scope**: Regarding the modeling approach, this project adheres to the assignment guidelines that need to use the models among 14 regression-based models addressed in the courserwork.
- **Temporal Scope**: This project focuses on analyzing summer weather data from the NWS for the period of June 1 to August 30, 2023, specifically between the hours of 9:00 AM and 6:00 PM. The selection of this timeframe aligns with standard working hours, which is critical for the research's primary objective of forecasting occupational heat risks while minimizing the diurnal effects of nighttime. The decision to target 3-hour-ahead forecasts at 12:00 PM and 3:00 PM stems from the NWS's capability to provide hourly forecasts up to 18 hours in advance, with each forecast hour having its unique uncertainty levels. This choice was reinforced by an Exploratory Data Analysis (EDA) indicating minimal variance in accuracy across different forecast times. Additionally, the specific focus on 12:00 PM and 3:00 PM aligns with observed variances in GHI and WBGT, thereby optimizing the research's scope to concentrate on comparing different regression models under the project's guidelines.
- **Spatial Scope**: This project concentrates on four distinct geolocations within the United States, each representing a different climate type. This strategic selection is primarily driven by the objectives of RH2 and RH3, which investigate the variability of GHI forecast errors in various climatic regions. These locations have been carefully chosen to provide a comprehensive understanding of how climate diversity influences forecasting accuracy. The specifics of these geolocations are detailed in the figure provided below.

![image.png](attachment:4a8ae91a-00b6-416c-ae17-ed1ff3d13c17.png)

## 3. Data Description
> **[Guideline]** </br>
> Describes the source and characteristics of the data used. </br>
> Data collection method</br>
> Definition and type of variables</br>

### 3-1 Data Collection
