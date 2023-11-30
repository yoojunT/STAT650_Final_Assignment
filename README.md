# STAT 650 - Final Project

- **Project title:** Investigating NWS forecasts for minimizing the uncertainties associated with occupational heat risk forecasting
- **Name:** Yoojun Kim
- **UIN:** 932002858

#### Submit files:
- Report (.html) - [Link](https://github.com/yoojunT/STAT650_Final_Assignment/blob/main/STAT650-Final_Report.html)
- Data files (.csv) - [Link](https://github.com/yoojunT/STAT650_Final_Assignment/tree/main/Data)
- **[All the Relevant Mateirals]** Github Repository - [Link](https://github.com/yoojunT/STAT650_Final_Assignment) <br>


## 1. Introduction
> **[Guideline]** </br>
> Provides the goal, objectives (research hypotheses) and background of the project. </br>
> Research interest/problem statement </br>
> Significance of the project </br>
> Theoretical background of the topic being addressed

### 1-1. Resarch Background 
Heat exposure poses a significant threat to occupational safety, underscoring the need for the timely risk assessments to protect the workforce. Such assessments are imperative for the implementation of preventative strategies, including promoting adequate hydration and ensuring that workers take sufficient breaks. A prevalent approach to assess the occupational heat risk involves the use of the Wet Bulb Globe Temperature (WBGT) index. **Despite its fundamental role in occupational safety management, its practical implementation is limited due to the challenge associated with timely data collection of globe temperature, which is crucial for calculating the outdoor WBGT index. This absence has hindered the deployment of proactive heat mitigation strategies.** </br>

To fill this knowledge gap, this research leverages the hourly forecast data updates from the National Weather Service (NWS) for enhancing the WBGT index. However, like all forecasting models, these predictions are subject to uncertainties that necessitate additional refinement. **Accordingly, this study will concentrate on the post-processing of heat radiation forecasts, identified as having a critical influence on the accuracy of WBGT predictions.**

- **Problem Statement**: Uncertanties of heat risk forecasts as detailed above.
- **Contribution/Significance:**  This methodological and knowledge enhancement in heat risk analysis aims to significantly aid practitioners in making informed decisions to mitigate potential heat-related hazards at jobsites. The contributions/significances are further elaborated in the conclusion section.

### 1-2. Research Hypotheses 
**This study centers on a detailed examination of three key research hypotheses, each aiming to deepen our understanding of the factors influencing WBGT forecasting:**
- **Research Hypothesis 1 (RH1)**: This hypothesis posits that errors in the Global Horizontal Irradiance (GHI) forecasts have the most substantial effect on the accuracy of WBGT forecasts. It suggests a direct and significant correlation between GHI forecast discrepancies and the reliability of WBGT predictions.
- **Research Hypothesis 2 (RH2)**: This hypothesis explores the variability of GHI forecast errors across different climatic regions. It proposes that the inaccuracies in GHI predictions are not uniform but vary significantly depending on the climate type, highlighting the need for region-specific analysis in meteorological modeling.
- **Research Hypothesis 3 (RH3)**: This hypothesis asserts that in the context of regression models, a multiple regression model, which incorporates relevant climate factors, is more effective than a basic linear regression model. It emphasizes the importance of a comprehensive approach that takes into account various climatic variables to enhance the predictive accuracy of WBGT forecasts.

### 1-3. Research Scopes
- **Modleing Scope**: Regarding the modeling approach, this project adheres to the assignment guidelines that need to use the models among 14 regression-based models addressed in the courserwork.
- **Temporal Scope**: This project focuses on analyzing summer weather data from the NWS for the period of June 1 to August 30, 2023, specifically between the hours of 9:00 AM and 6:00 PM. The selection of this timeframe aligns with standard working hours, which is critical for the research's primary objective of forecasting occupational heat risks while minimizing the diurnal effects of nighttime. The decision to target 3-hour-ahead forecasts at 12:00 PM and 3:00 PM stems from the NWS's capability to provide hourly forecasts up to 18 hours in advance, with each forecast hour having its unique uncertainty levels. This choice was reinforced by an Exploratory Data Analysis (EDA) indicating minimal variance in accuracy across different forecast times. Additionally, the specific focus on 12:00 PM and 3:00 PM aligns with observed variances in GHI and WBGT, thereby optimizing the research's scope to concentrate on comparing different regression models under the project's guidelines.
- **Spatial Scope**: This project concentrates on four distinct geolocations within the United States, each representing a different climate type. This strategic selection is primarily driven by the objectives of RH2 and RH3, which investigate the variability of GHI forecast errors in various climatic regions. These locations have been carefully chosen to provide a comprehensive understanding of how climate diversity influences forecasting accuracy. The specifics of these geolocations are detailed in the figure provided below.

![image.png](attachment:1abcb3c1-4f55-462d-a220-090ebcc04f04.png)

## 2. Data Description
> **[Guideline]** </br>
> Describes the source and characteristics of the data used. </br>
> Data collection method</br>
> Definition and type of variables</br>

### [2-1 Data Collection](https://github.com/yoojunT/STAT650_Final_Assignment/blob/main/Section%202-1%20Data%20Collection.ipynb)
This study systematically collects historical weather observation and forecast data from the [High-Resolution Rapid Refresh (HRRR)](https://rapidrefresh.noaa.gov/hrrr/) of the National Oceanic and Atmospheric Administration (NOAA), adhering to predefined temporal and spatial parameters. [This dataset provides hourly update date up to 18 hours across the United States with over 190 variables](https://mesowest.utah.edu/html/hrrr/zarr_documentation/html/zarr_variables.html). Among them, this project begins with the acquisition of raw data, represented as a 3 km-spatial resolution map of the United States, focusing on summer data for crucial climatic variables such as GHI, relative humidity (rh), air temperature (ta), air velocity (va), and cloud cover. The rational behind this selection is (1) the variables needed for WBGT calcuations and (2) cloud cover is strongly influential on GHI, and (3) considerable data size that each raw data only has one variable. Note that even with this decision, the data collection processing at this stage has taken more than 5 days. Subsequently, for each of the four specifically chosen locations, corresponding data are extracted, resulting in four distinct data frames that encompass historical climate data pertinent to each location. The final phase involves calculating the WBGT using a formula below. This calculated WBGT data is essential for the exploration of RH1, aimed at determining the impact of GHI forecast discrepancies on the accuracy of WBGT predictions, thereby contributing significantly to the study's overarching goal of enhancing heat risk assessment in occupational settings.


[WBGT (Ono and Tonouchi, 2014)](https://www.jstage.jst.go.jp/article/seikisho/50/4/50_147/_article/-char/en) = 0.735 * ta + 0.0374 * rh + 0.00292 * ta * rh + 7.619 * GHI - 4.557 * (GHI ^ 2) - 0.0572 * va - 4.

### 2-2 Exploratory Data Analysis (EDA)
> **[Guideline]** </br>
> Handle missing values, outliers, and any other data quality issues.</br>
> Transform variables if necessary (e.g., cleaning, normalization, encoding categorical variables).</br>
> Build a common dataset (may apply the dataset to the selected regression models).</br>
> Perform exploratory data analysis (EDA) to gain insights into the dataset characteristics.</br>
> Finding correlations, visualizing the data using different plots and charts, etc. that used in class

**[Independent Variable]**
- **ta_error**: errors of air temperature forecasts (Celsius) - Continuous quantitative variable
- **rh_error**: errors of relative humidity forecasts (%) - Continuous quantitative variable
- **va_error**: errors of air velocity forecasts (m/s) - Continuous quantitative variable
- **cloud_error**: errors of cloud cover forecasts (%) - Continuous quantitative variable

**[Dependent Variable]**
- **GHI_error**: errors of global horizontal irradiance forecasts (W/m²) - Continuous quantitative variable

**[Other Variable]**
- **WBGT_error**: errors of WBGT forecasts (Celsius) - Continuous quantitative variable

### [2-2-1 Heat Risk Forecsting Discrepancies](https://github.com/yoojunT/STAT650_Final_Assignment/blob/main/Section%202-2-1%20EDA_RMSE_MAE_Plots.ipynb)

In this study, forecast errors for each variable are first calculated by comparing them with observed data, and these errors are then quantified using Mean Absolute Error (MAE) and Root Mean Square Error (RMSE). The analysis reveals two significant findings. Firstly, although longer-range forecasts, like those made 18 hours ahead, generally tend to be less accurate than nearer-term forecasts (e.g., 1-hour ahead), we observed no notable difference in accuracy between 3-hour-ahead and 6-hour-ahead forecasts in the context of heat risk. Secondly, the forecasts for 12:00 PM and 3:00 PM consistently showed higher errors compared to those for 9:00 AM and 6:00 PM, coinciding with periods of lower heat radiation. Notably, GHI exhibited the greatest level of uncertainty among the variables, significantly impacting the WBGT trends. This aspect will receive further examination in RH1. Based on these insights, the study's temporal focus is refined to 3-hour-ahead forecasts at 12:00 PM and 3:00 PM, as detailed in Section 1-3.

![image.png](attachment:76059950-ed56-4027-b835-b1f8f862a38a.png)

### [2-2-2 Desciptive analysis](https://github.com/yoojunT/STAT650_Final_Assignment/blob/main/Section%202-2-2%20EDA_Multicollinearity.ipynb)
  
In line with the defined temporal scope, basic statistical analyses of the errors are illustrated in the figure below, which shows no missing values in the dataset. For this project, additional pre-processing steps, such as data cleaning and normalization, were not undertaken. This decision stems from the intent to utilize the ultimate regression model, as discussed in RH3, in real-world scenarios where such processing may not be feasible due to time constraints and practical application considerations. Moreover, to maintain consistency across different climate regions, the project has deliberately minimized further pre-processing, taking into account these practical aspects and the need for uniformity in variable treatment.

![image.png](attachment:6a9a4492-9012-4b50-9f80-73f8eda405b4.png)

### [2-2-3 Multicollinearity](https://github.com/yoojunT/STAT650_Final_Assignment/blob/main/Section%202-2-2%20EDA_Multicollinearity.ipynb)
For RH3, this project intends to employ a regression-based approac following the instructions. In this regard, multicollinearity is a critical factor in selecting suitable regression models.  The figure belowrepresents  that all variables in the datasets exhibit weak multicollinearity, as indicated by Variance Inflation Factors (VIF) below 10. This information is vital for both feature selection and model determination within the context of regression analysis. The low levels of multicollinearity among the variables not only validate the appropriateness of using regression models but also ensure the reliability and interpretability of the results derived from these models.
![image.png](attachment:6c320205-0be8-464c-a54d-d477fe2ea450.png)

## 3. Methodology
> **[Guideline]** </br>
> Provides a detailed explanation of the analytical methods used in the project.
> the statistical methods,
> modeling techniques used, and reasons for their selection
>
> **Model Evaluation and Selection**</br>
> Discuss the assumptions underlying each model and their applicability to the data.</br> 
> Test model assumptions for models</br>
> Implement multiple models using appropriate libraries or programming languages.</br>
> Find and explain the choice of parameters by variable selection approaches.</br>
>
> **Model Comparison**</br>
> After developing the model, evaluate its performance using appropriate metrics.</br>
> Include R-squared, mean squared error, root mean squared error, etc. for regression problems,</br>
> Include accuracy, precision, recall, F1 score, AUC-ROC, etc. for classification problems like logistic regression.</br>
> Try at least one other regression approach and compare the results.</br>
>
> **Model Improvement**</br>
> Apply techniques to improve model performance (if necessary), such as feature selection or regularization methods>

This study conducts a comprehensive analysis of three pivotal research hypotheses, each aimed at enhancing our understanding of the variables that influence WBGT forecasting. The hypotheses are RH1 (Impact of errors of GHI forecasts on errors of WBGT forecasts), RH2 (Errors of GHI forecasts associated with different climatic regions), and RH3 (Regression approach to esitmate errors of GHI forecasts). To address the unique objectives of each hypothesis, the project adopts distinct statistical methodologies: Pearson correlation analysis for RH1, one-way ANOVA for RH2, and regression models (both simple and multiple) for RH3. **The rationale for each model choice, along with their underlying assumptions, is outlined below:**

- **[RH 1 - Pearson Correlation](https://github.com/yoojunT/STAT650_Final_Assignment/blob/main/Section%204-1%20Research%20Hypothesis%201.ipynb)**: This method is chosen primarily for two reasons. Firstly, it assesses the linear relationship between independent and dependent variables, a critical factor in regression analysis. Secondly, since RH1 aims to ascertain the influence of GHI forecast errors on WBGT forecast errors, understanding their correlation and the significance of this relationship is essential. The assumptions for Pearson Correlation include normal distribution, homoscedasticity, independence of observations, and interval or ratio-level data. These assumptions are tested based on the number of sample sizes and both linearlity and multicollinearity are checked by EDA.

- **[RH 2 - One-way ANOVA test](https://github.com/yoojunT/STAT650_Final_Assignment/blob/main/Section%204-2%20Research%20Hypothesis%202.ipynb)**: The focus here is to identify statistical differences in GHI forecast errors among various climatic regions. This approach is underpinned by assumptions such as normal distribution of the sampled populations, homogeneity of variances, and independence of observations. These assumptions are tested based on the number of sample sizes and both linearlity and multicollinearity are checked by EDA.
 
- **[RH 3 - Regression models](https://github.com/yoojunT/STAT650_Final_Assignment/blob/main/Section%204-3%20Research%20Hypothesis%203.ipynb)**: Chosen to meet the specific needs of this hypothesis, simple and multiple regression models are utilized due to the absence of multicollinearity and confirmed linearity of the variables as established in RH1. Following the findings in RH2, different regression models are developed and compared for each climate region. Underlying assumptions for these models include linearity, independence of errors, multivariate normality, absence of multicollinearity, and homoscedasticity. To refine the models, various feature selection thresholds and alternative regression approaches, such as Least Absolute Shrinkage and Selection Operator (LASSO) and Ridge, are explored and evaluated. These assumptions are tested based on the number of sample sizes and both linearlity and multicollinearity are checked by EDA.

## 4. Results and Interpretation
> **[Guideline]**</br>
> Presents the findings of the analysis and interpretation of these results.</br>
> the performance of the models,</br>
> statistical significance (p-value),</br>
> Interpret coefficients of significant predictors in your best model, and</br>
> what these results imply

### [4-1 RH 1 - Pearson Correlation](https://github.com/yoojunT/STAT650_Final_Assignment/blob/main/Section%204-1%20Research%20Hypothesis%201.ipynb)

The figure presented below is a series of scatter plots illustrating the relationship between the dependent variable (GHI_error) and other variables across four distinct climate regions, which includes the WBGT_error variable. Notably, the P-values in all instances are below 0.05, indicative of a relatively strong linear relationship. In terms of correlation, va_error exhibits a weaker correlation in all regions except Texas, where the correlation values are nearly zero. In contrast, ta_error demonstrates the strongest correlation with GHI_error in each climate region. Most notably, the correlation coefficients between GHI_error and WBGT_error are 0.77, 0.77, 0.81, and 0.73 for Texas, Iowa, Nevada, and Seattle repectively with below 0.05. These correlations underscore a strong linear relationship between these two variables. This finding lends substantial support to RH1, emphasizing the significance of minimizing GHI forecast errors to ensure accurate heat risk forecasts.

![image.png](attachment:559906b5-7c6c-4dee-a045-3c27150a8aaf.png)

### [4-2 RH 2 - One-way ANOVA test](https://github.com/yoojunT/STAT650_Final_Assignment/blob/main/Section%204-2%20Research%20Hypothesis%202.ipynb)
The tables presented below display the results of a one-way ANOVA test conducted to examine the variations in GHI_error and ta_error across four distinct climate regions. Analyzing the outcomes of GHI_error comparisons reveals that although the P-values fall within a relatively narrow range, spanning from 0.09 to 0.4, none of them dip below the conventional significance threshold of 0.05. This suggests that, based on the available data, it is challenging to assert that there exist statistically significant differences in GHI errors among the various climate regions. In contrast, an examination of the ta_error results reveals that 4 out of 6 comparisons yield P-values below 0.05, accompanied by higher F-values. Considering the observed linear correlation between ta_error and GHI_error, ranging from 0.38 to 0.51, it becomes apparent that exploring a more diverse set of scenarios could potentially alter this conclusion. To sum up, within the sample population of this study, encompassing the summer months and four defined locations during specific hours, it remains challenging to establish statistically significant distinctions in GHI errors among the different climate regions.

![image.png](attachment:25d85e8c-7ac8-42b6-9d02-0f7912e00ab1.png)

### [4-3 RH 3 - Regression models](https://github.com/yoojunT/STAT650_Final_Assignment/blob/main/Section%204-3%20Research%20Hypothesis%203.ipynb)
This section introduces a comparison between two regression models: a simple regression model that utilizes the independent variable exhibiting the highest correlation with the dependent variable, and a multiple regression model that includes variables surpassing a 0.1 correlation threshold. The effect of modifying these correlation thresholds on model performance is also examined. Additionally, to further improve the model, the results of Lasso and Ridge regression methods, applied with different alpha values, are analyzed and compared. The train and test datasets are randomlay split with 0.7 and 0.3 ratios, respectively. The findings are presented in the tables below.
In the simple regression model analysis, 'ta_error' emerges as the independent variable with the highest correlation across three locations: 0.39 in Texas, 0.33 in Nevada, and 0.42 in Seattle. Conversely, for Iowa, 'cloud_error' shows the highest correlation among independent variables, at 0.49. Based on these findings, distinct simple regression models were developed and assessed. However, all models demonstrated limited performance, with their explainability particularly low, as indicated by R-squared values falling below 0.3. This suggests a potential need to incorporate additional independent variables to enhance the models' explanatory power through the use of multiple regression approaches.

![image.png](attachment:3e19bd7b-ee1e-4969-9a88-7485317200f4.png)
The table presented illustrates the outcomes of various multiple regression models. Notably, while Seattle's model incorporates three independent variables—ta_error, cloude_error, and rh_error—the models for the other three locations rely solely on ta_error and cloude_error. A comparison with simple regression results reveals an enhancement in performance metrics such as R squared, RMSE, and MAE for Iowa, Nevada, and Seattle, although Texas shows a marginal decline. These findings underscore the necessity of developing climate-specific regression models, highlighting that a universal model is not feasible for different climatic conditions. Overall, it is evident that the multiple regression models surpass the simple regression models in terms of performance.

![image.png](attachment:2edbdfb4-4b53-45a7-85fc-c021360e0765.png)

**[Model Improvement Plan 1]** - Different correlation thresholds on multiple regression model </br>
The below table details the impact of varying correlation thresholds on a multiple regression model. These thresholds, set between 0 and 1 at intervals of 0.1, continue until no independent variables remain. Despite altering the threshold from the initial 0.1, there is no observed improvement in model performance across all cases. However, it is important to note that these results could differ with alternative datasets. While the current dataset shows no enhancement, this approach may prove effective in other scenarios, particularly where more influential variables are present and issues of multicollinearity are mitigated. This suggests potential applicability in diverse data environments where similar trends are observed.

![image.png](attachment:68775451-3c22-4bcc-b043-eae80f441307.png)

**[Model Improvement Plan 2]** - Different regularizations </br>
This improvement plan involves utilizing different regularizations, specifically Lasso and Ridge regression models. Note that for the purpose of seeking potential improvement plan which is data-dependent, the underlying assumptions of Lasso and Ridge regression models are not addressed in this project. To assess the efficacy of this method, the alpha parameter is varied across a range of values: 0.001, 0.01, 0.1, 1, 10, 100, and 1000. Subsequent tables present the optimal results for each location, evaluated based on MAE, RMSE, and R squared metrics. When compared with the outcomes of the multiple regression analysis, there is a general improvement in R squared, MAE, and RMSE for most locations, except Texas where MAE and RMSE do not show enhancement. This underscores the importance of carefully analyzing the specific characteristics of each dataset before implementing such model improvement strategies, ensuring that the approach is tailored to the unique needs of the data.

![image.png](attachment:417d2618-b4be-4cc1-9fff-fa0702ce3824.png)

## 5. Conclusion 
> **[Guideline]**</br>
> Summarizes the main discoveries of the project and their implications.</br>
> Discuss whether the selecteds model met the expectations to conclude each hypothesis,</br>
> Discuss the limitations of the project, and</br>
> Suggest the possible directions for future research to overcome the limitation.

 #### **Summarizes the main discoveries of the project to conclude each hypothesis and their implications.**

- **[RH1]** In Section 4-1, a compelling linear correlation between GHI_error and WBGT_error is demonstrated, bearing significant practical implications for heat risk assessments. It highlights the necessity of meticulously accounting for GHI forecast errors, which play a pivotal role in enhancing the accuracy of heat risk predictions. From a theoretical perspective, the section also unveils linear relationships between GHI_error and other selected climatic variables. This discovery underscores the importance of considering a variety of climatic factors to more comprehensively understand GHI forecast errors across diverse climate regions. Additionally, confirming the linearity of these relationships is crucial for validating the assumptions underlying the use of regression models in RH3 analysis.

- **[RH2]** Section 4-2 reveals a crucial insight: there is no statistically significant difference in GHI_error across the four locations studied. However, this finding contrasts with other correlated variables, such as ta_error, which demonstrate significant differences when assessed with a P-value threshold of 0.05. This outcome emphasizes the importance of considering region-specific climate variable trends to gain a deeper understanding of GHI_error. Furthermore, these insights have implications for RH3, suggesting the need for distinct regression models tailored to each climate region. This approach acknowledges that different models, with their unique characteristics, are better suited to address specific climatic conditions. Consequently, the findings in RH3 support the idea that model selection and customization based on regional climate characteristics can lead to more accurate and effective modeling outcomes.

- **[RH3]** Section 4-3 conducts a comparative analysis between two regression models: a simple regression model and a multiple regression model. The results demonstrate that the multiple regression model consistently outperforms the simple regression model across all climate regions studied. Additionally, the section explores two types of model improvement strategies: (1) applying different thresholds for variable selection in multiple regression models, and (2) employing various regularization methods, such as LASSO and Ridge regression. The findings highlight that incorporating relevant climate variables can significantly enhance model performance, as evidenced by improvements in R squared, RMSE, and MAE, particularly in predicting GHI_error. This enhancement is crucial for improving the accuracy of heat risk forecasting. Furthermore, the varied model development outcomes across different climate regions underscore the importance of adopting climate-specific approaches. These approaches should meticulously account for the temporal and spatial dimensions of forecast results, ensuring that models are finely tuned to the unique characteristics of each region.

 #### **Limitations and possible directions for future research**

- The first limitation of this study lies in its temporal and spatial scope. While Section 1-3 provides a well-founded rationale for these boundaries, it is important to acknowledge that expanding the scope in terms of time and space could significantly enrich the study's findings. In particular, the incorporation of a more diverse range of climate regions warrants attention, as evidenced by the varying performances of region-specific regression models highlighted in the results. Addressing this aspect could enhance the scalability and applicability of the project, allowing for a more comprehensive understanding of the models' effectiveness across different environmental contexts. Such expansion would not only validate the current findings but also potentially reveal new insights into the dynamics of climate-related data analysis.

- The second limitation of this project is its exclusive focus on regression models by the project's requirements. This approach may overlook the potential benefits of alternative methodologies. Machine learning techniques, already employed in related research, could offer valuable insights and improvements for this purpose. Additionally, optimization methods like the Kalman filter present another viable alternative. The Kalman filter, in particular, is advantageous for its ability to minimize computational costs and its reduced sensitivity to outliers in the dataset. This is due to its unique mechanism of continuously updating its Kalman gain based on new data. Exploring these diverse approaches could significantly enhance the robustness and efficiency of the models, leading to more accurate and reliable forecasting outcomes.

- The third limitation of this study is the approach to splitting the training and testing datasets, which was done randomly without considering temporal factors. This was a necessary compromise due to project constraints for comparing the performance of regression models. However, since the data is time-series in nature, where more recent historical data often contains richer and more relevant information, this approach might not be ideal. For future enhancements, it is crucial to consider models specifically optimized for time-series analysis. Models such as the Autoregressive Integrated Moving Average (ARIMA) or machine learning algorithms like Long Short-Term Memory (LSTM) networks, which excel in handling data with pronounced temporal dynamics, could be more effective. Moreover, the study did not incorporate post-processing steps, a common practice in forecasting. Implementing these steps and employing time-series optimized models could substantially enhance the effectiveness and precision of heat risk predictions. Such advancements would not only improve predictive accuracy but also offer a more nuanced and comprehensive methodology for assessing heat risks over time.

## 6. Reference and Appendix
> **[Guideline]**</br>
> Reference: Lists all the sources cited in the report.</br>
> Appendix: Includes any additional tables, charts, code, or other relevant material, if necessary.</br>
> Python code: use the following steps to input your code as 

### 6-1 Reference
- [Ono, M. & Tonouchi, M. Estimation of wet-bulb globe temperature using generally measured meteorological indices. JAPANESE J. Biometeorol. 50, 147–157 (2014)](https://www.jstage.jst.go.jp/article/seikisho/50/4/50_147/_article/-char/en)
- [High-Resolution Rapid Refresh (HRRR) Website](https://rapidrefresh.noaa.gov/hrrr/) 
- [High-Resolution Rapid Refresh (HRRR) Variable Description Webiste](https://mesowest.utah.edu/html/hrrr/zarr_documentation/html/zarr_variables.html).

### 6-2 Appendix
- [All the relevant and additional materials uploaded in this Github Repository]()


### 6-3 Codes
All the codes are linked to the files shared in the Github. This format of code submission was confirmed by the instructor. Below is a list of shared codes:
- [Section 2-1 Data Collection](https://github.com/yoojunT/STAT650_Final_Assignment/blob/main/Section%202-1%20Data%20Collection.ipynb)
- [Section 2-2-1 EDA_RMSE_MAE_Plots](https://github.com/yoojunT/STAT650_Final_Assignment/blob/main/Section%202-2-1%20EDA_RMSE_MAE_Plots.ipynb)
- [Section 2-2-2 EDA_Multicollinearity](https://github.com/yoojunT/STAT650_Final_Assignment/blob/main/Section%202-2-2%20EDA_Multicollinearity.ipynb)
- [Section 4-1 Research Hypothesis 1](https://github.com/yoojunT/STAT650_Final_Assignment/blob/main/Section%204-1%20Research%20Hypothesis%201.ipynb)
- [Section 4-2 Research Hypothesis 2](https://github.com/yoojunT/STAT650_Final_Assignment/blob/main/Section%204-2%20Research%20Hypothesis%202.ipynb)
- [Section 4-3 Research Hypothesis 3](https://github.com/yoojunT/STAT650_Final_Assignment/blob/main/Section%204-3%20Research%20Hypothesis%203.ipynb)




